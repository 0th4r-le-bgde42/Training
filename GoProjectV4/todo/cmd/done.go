package cmd

import (
	"fmt"
	"strconv"

	"github.com/spf13/cobra"
)

var doneCmd = &cobra.Command{
	Use: "done [id]",
	Short: "Indiquer qu'une tache a ete faite",
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		id, err := strconv.Atoi(args[0])
		if err != nil {
			fmt.Println("Erreur: l'ID doit etre un nombre valide.")
			return
		}

		taches, err := ChargerTaches()
		if err != nil {
			fmt.Println("Erreur lecture stockage :", err)
			return
		}

		taches[id-1].Fait = true
		if err := SaveTaches(taches); err != nil {
			fmt.Println("Erreur sauvegarde binaire :", err)
			return
		}

		fmt.Printf("Tache finalisee.")
	},
}

func init() {
	rootCmd.AddCommand(doneCmd)
	doneCmd.Flags().Int("id", 0, "id de la tache")
}