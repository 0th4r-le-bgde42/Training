package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var urgent bool

var addCmd = &cobra.Command{
	Use: "add [text]",
	Short: "Ajouter une tache",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		texte := args[0]
		prefix := "[ ]"
		if urgent {
			prefix = "[URGENT]"
		}

		ligne := fmt.Sprintf("%s %s\n", prefix, texte)

		f, err := os.OpenFile("todos.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			fmt.Printf("Erreur d'ecriture : %v\n", err)
			return
		}
		defer f.Close()

		if _, err := f.WriteString(ligne); err != nil {

			fmt.Printf("Erreur d'enregistrement : %v\n", err)
			return
		}

		fmt.Printf("Tache enregistree : %s", ligne)
	},
}

func init() {
	rootCmd.AddCommand(addCmd)
	addCmd.Flags().BoolVarP(&urgent, "urgent", "u", false, "Marquer la tache comme prioritaire")
}