package cmd

import (
	"fmt"
	"strings"

	"github.com/spf13/cobra"
	"treenitest/internal/api"
)

var (
	flagZanpakuto bool
	flagShikai    bool
	flagBankai    bool
	flagBirthday  bool
	flagRace      bool
)

var charCmd = &cobra.Command{
	Use:   "char [race optionnelle] [nom]",
	Short: "Affiche la fiche ou des attributs précis d'un personnage",
	Args:  cobra.MinimumNArgs(1),
	PostRun: func(cmd *cobra.Command, args []string) {
		flagZanpakuto = false
		flagShikai = false
		flagBankai = false
		flagBirthday = false
		flagRace = false
	},
	RunE: func(cmd *cobra.Command, args []string) error {
		knownRaces := map[string]bool{
			"shinigami": true,
			"humans":    true,
			"quincy":    true,
			"arrancar":  true,
		}

		var perso *api.Charac
		var err error

		if len(args) >= 2 && knownRaces[strings.ToLower(args[0])] {
			perso, err = api.FetchCharacter(args[0], strings.Join(args[1:], " "))
		} else {
			persos, err := api.FindCharacter(strings.Join(args, " "))
			if err != nil || len(persos) == 0 {
				return fmt.Errorf("personnage introuvable")
			}
			if len(persos) == 1 {
				perso = persos[0]
			} else {
				fmt.Printf("\nPlusieurs personnages correspondent :\n")
				for i, p := range persos {
					fmt.Printf("  [%d] %-25s (%s)\n", i+1, p.Name.English, p.Stats.Race)
				}
				fmt.Printf("\nChoisis un numéro (1-%d) : ", len(persos))
				var choice int
				if _, err := fmt.Scanln(&choice); err != nil || choice < 1 || choice > len(persos) {
					return fmt.Errorf("sélection annulée")
				}
				perso = persos[choice-1]
			}
		}

		if err != nil {
			return err
		}

		hasFilter := flagZanpakuto || flagShikai || flagBankai || flagBirthday || flagRace

		if hasFilter {
			printFiltered(perso)
		} else {
			printFull(perso)
		}

		return nil
	},
}

func printFiltered(c *api.Charac) {
	fmt.Printf("[%s]\n", c.Name.English)

	if flagRace {
		fmt.Printf("  • Race        : %s\n", c.Stats.Race)
	}
	if flagBirthday {
		fmt.Printf("  • Birthday    : %s\n", c.Stats.Birthday)
	}
	if flagZanpakuto {
		if c.Stats.Zanpakuto.Resurreccion != "" {
			fmt.Printf("  • Resurr.     : %s\n", c.Stats.Zanpakuto.Resurreccion)
		} else if c.Stats.Zanpakuto.Shikai != "" {
			fmt.Printf("  • Zanpakutō   : %s\n", c.Stats.Zanpakuto.Shikai)
		} else {
			fmt.Println("  • Zanpakutō   : Inconnu / Aucun")
		}
	}
	if flagShikai {
		fmt.Printf("  • Shikai      : %s\n", c.Stats.Zanpakuto.Shikai)
	}
	if flagBankai {
		fmt.Printf("  • Bankai      : %s\n", c.Stats.Zanpakuto.Bankai)
	}
}

func printFull(c *api.Charac) {
	fmt.Println("==================================================")
	fmt.Printf("Nom       : %s (%s)\n", c.Name.English, c.Name.Kanji)
	if c.Name.Romaji != "" {
		fmt.Printf("Romaji    : %s\n", c.Name.Romaji)
	}
	fmt.Printf("ID / Slug : %s (%s)\n", c.ID, c.Slug)
	fmt.Println("--------------------------------------------------")
	fmt.Println("[ STATS ]")
	fmt.Printf("  • Race      : %s\n", c.Stats.Race)
	fmt.Printf("  • Genre     : %s\n", c.Stats.Gender)
	fmt.Printf("  • Anniv     : %s\n", c.Stats.Birthday)
	if c.Stats.Zanpakuto.Shikai != "" {
		fmt.Printf("  • Shikai    : %s\n", c.Stats.Zanpakuto.Shikai)
	}
	if c.Stats.Zanpakuto.Bankai != "" {
		fmt.Printf("  • Bankai    : %s\n", c.Stats.Zanpakuto.Bankai)
	}
	if c.Stats.Zanpakuto.Resurreccion != "" {
		fmt.Printf("  • Resurr.   : %s\n", c.Stats.Zanpakuto.Resurreccion)
	}
	if c.Description != "" {
		fmt.Println("--------------------------------------------------")
		fmt.Println("[ BIO ]")
		fmt.Println(c.Description)
	}
	fmt.Println("==================================================")
}

func init() {
	charCmd.Flags().BoolVarP(&flagRace, "race", "r", false, "Affiche la race")
	charCmd.Flags().BoolVarP(&flagBirthday, "birthday", "b", false, "Affiche l'anniversaire")
	charCmd.Flags().BoolVarP(&flagZanpakuto, "zanpakuto", "z", false, "Affiche le nom du Zanpakutō / Resurrección")
	charCmd.Flags().BoolVarP(&flagShikai, "shikai", "s", false, "Affiche uniquement le Shikai")
	charCmd.Flags().BoolVarP(&flagBankai, "bankai", "B", false, "Affiche uniquement le Bankai")

	RootCmd.AddCommand(charCmd)
}