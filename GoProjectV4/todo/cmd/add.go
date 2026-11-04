package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var urgent bool

var addCmd = &cobra.Command{
	Use: "add [text]",
	Short: "Ajouter une tache",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		texte := args[0]

		taches, err := ChargerTaches()
		if err != nil {
			fmt.Println("Erreur lecture stockage :", err)
			return
		}

		nouvelle := Tache{
			Texte: texte,
			Urgent: urgent,
			Fait: false,
		}
		taches = append(taches, nouvelle)

		if err := SaveTaches(taches); err != nil {
			fmt.Println("Erreur sauvegarde binaire :", err)
			return
		}

		statut := "U"
		if urgent {
			fmt.Printf("%s%s%s Tache enregistree : %s\n", ColorRed, statut,ColorReset, texte)
		} else {
			fmt.Printf("%s Tache enregistree : %s\n", statut, texte)
		}
	},
}

func init() {
	rootCmd.AddCommand(addCmd)
	addCmd.Flags().BoolVarP(&urgent, "urgent", "u", false, "Marquer la tache comme prioritaire")
}