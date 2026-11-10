package cmd

import (
	"bytes"
	_ "embed"
	"fmt"
	"image"
	_ "image/jpeg"
	_ "image/png"
	"net/http"
	"os"
	"strings"

	"github.com/spf13/cobra"
	"golang.org/x/term"
	"treenitest/internal/api"
)

//go:embed assets/images.jpeg
var fallbackImageBytes []byte
var customWidthFlag int

var avatarCmd = &cobra.Command{
	Use:   "avatar [race optionnelle] [nom ou slug]",
	Short: "Affiche l'avatar d'un personnage avec résolution adaptée au terminal",
	Args:  cobra.MinimumNArgs(1),
	PostRun: func(cmd *cobra.Command, args []string) {
		customWidthFlag = 0 // Reset obligatoire pour le REPL
	},
	RunE: func(cmd *cobra.Command, args []string) error {
		knownRaces := map[string]bool{
			"shinigami": true,
			"humans":    true,
			"quincy":    true,
			"arrancar":  true,
		}

		var race, slug string

		// ==========================================
		// C'EST CE BLOC CI-DESSOUS QUI REMPLACE L'ANCIENNE RÉCUPÉRATION DU PERSO :
		// ==========================================
		var targetPerso *api.Charac

		if len(args) >= 2 && knownRaces[strings.ToLower(args[0])] {
			race = strings.ToLower(args[0])
			slug = strings.ToLower(strings.Join(args[1:], "-"))
		} else {
			targetName := strings.Join(args, " ")
			persos, err := api.FindCharacter(targetName)
			if err != nil || len(persos) == 0 {
				showFallback(fmt.Sprintf("Désolé, aucun personnage trouvé pour '%s'...", targetName))
				return nil
			}

			// Un seul trouvé : on le prend direct
			if len(persos) == 1 {
				targetPerso = persos[0]
			} else {
				// Plusieurs membres trouvés (ex: famille Kurosaki) -> menu de choix
				fmt.Printf("\nPlusieurs personnages correspondent à '%s' :\n", targetName)
				for i, p := range persos {
					fmt.Printf("  [%d] %-25s (%s)\n", i+1, p.Name.English, p.Stats.Race)
				}
				fmt.Printf("\nChoisis un numéro (1-%d) : ", len(persos))

				var choice int
				_, scanErr := fmt.Scanln(&choice)
				if scanErr != nil || choice < 1 || choice > len(persos) {
					fmt.Println("Sélection annulée ou invalide.")
					return nil
				}
				targetPerso = persos[choice-1]
			}

			// Formatage de la race pour l'URL d'avatar
			rawRace := strings.ToLower(string(targetPerso.Stats.Race))
			switch {
			case strings.Contains(rawRace, "human"):
				race = "humans"
			case strings.Contains(rawRace, "soul"), strings.Contains(rawRace, "shinigami"):
				race = "shinigami"
			case strings.Contains(rawRace, "quincy"):
				race = "quincy"
			case strings.Contains(rawRace, "arrancar"), strings.Contains(rawRace, "hollow"):
				race = "arrancar"
			default:
				race = "humans"
			}

			slug = targetPerso.Slug
			if slug == "" {
				slug = strings.ReplaceAll(strings.ToLower(targetPerso.Name.English), " ", "-")
			}
		}
		// ==========================================
		// FIN DU BLOC
		// ==========================================

		// La suite reste inchangée :
		avatarURL := fmt.Sprintf("https://bleach-api-8v2r.onrender.com/avatar/%s/%s", race, slug)
		fmt.Printf("Chargement de l'avatar (%s)...\n", avatarURL)

		resp, err := http.Get(avatarURL)
		if err != nil || resp.StatusCode != http.StatusOK {
			if resp != nil {
				resp.Body.Close()
			}
			showFallback(fmt.Sprintf("Désolé, aucun avatar disponible pour '%s' sur l'API...", slug))
			return nil
		}
		defer resp.Body.Close()

		img, _, err := image.Decode(resp.Body)
		if err != nil {
			showFallback("Désolé, erreur lors de la lecture de l'avatar...")
			return nil
		}

		targetWidth := getOptimalWidth(customWidthFlag)
		renderImageToTerminal(img, targetWidth)
		return nil
	},
}

func showFallback(msg string) {
	fmt.Println()
	fmt.Printf("\033[33m%s\033[0m\n", msg)
	fmt.Println("Mais pas d'inquiétude, Chad veille au grain :")
	fmt.Println()

	img, _, err := image.Decode(bytes.NewReader(fallbackImageBytes))
	if err != nil {
		fmt.Println("[Erreur chargement image fallback]")
		return
	}

	targetWidth := getOptimalWidth(customWidthFlag)
	renderImageToTerminal(img, targetWidth)
}

func getOptimalWidth(userWidth int) int {
	// Si l'utilisateur a passé un flag -w valide, on lui obéit directement
	if userWidth > 0 {
		return userWidth
	}

	termWidth, _, err := term.GetSize(int(os.Stdout.Fd()))
	if err != nil || termWidth <= 0 {
		return 80
	}

	// Calcul automatique par défaut
	optimal := (termWidth * 85) / 100
	if optimal > 160 {
		optimal = 160
	}
	if optimal < 40 {
		optimal = termWidth - 4
	}
	return optimal
}

func renderImageToTerminal(img image.Image, targetWidth int) {
	bounds := img.Bounds()
	srcW := bounds.Dx()
	srcH := bounds.Dy()
	if srcW == 0 || srcH == 0 {
		return
	}

	targetHeight := (srcH * targetWidth) / (srcW * 2)

	for y := 0; y < targetHeight; y += 2 {
		for x := 0; x < targetWidth; x++ {
			srcX := bounds.Min.X + (x * srcW / targetWidth)
			srcY1 := bounds.Min.Y + (y * srcH / targetHeight)
			srcY2 := bounds.Min.Y + ((y + 1) * srcH / targetHeight)

			r1, g1, b1, a1 := img.At(srcX, srcY1).RGBA()
			r2, g2, b2, a2 := img.At(srcX, srcY2).RGBA()

			if a1 < 32768 && a2 < 32768 {
				fmt.Print(" ")
				continue
			}

			topR, topG, topB := uint8(r1>>8), uint8(g1>>8), uint8(b1>>8)
			botR, botG, botB := uint8(r2>>8), uint8(g2>>8), uint8(b2>>8)

			fmt.Printf("\033[38;2;%d;%d;%dm\033[48;2;%d;%d;%dm▀\033[0m", topR, topG, topB, botR, botG, botB)
		}
		fmt.Println()
	}
}

func init() {
	avatarCmd.Flags().IntVarP(&customWidthFlag, "width", "w", 0, "Largeur personnalisée en colonnes (ex: -w 120)")
	RootCmd.AddCommand(avatarCmd)
}