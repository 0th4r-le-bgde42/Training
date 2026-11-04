package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var urg bool
var done bool

var listCmd = &cobra.Command{
	Use: "list",
	Short: "Affiche les taches",
	Run: func(cmd *cobra.Command, args []string) {
		taches, err := ChargerTaches()
		if err != nil {
			fmt.Println("Erreur lors de la lecture du fichier binaire (fichier corrumpu ?) :", err)
			return
		}

		if len(taches) == 0 {
			fmt.Println("Aucune tache enregistree.")
			return
		}

		fmt.Println("--- Vos Taches ---")
		for i, t := range taches {
			flag := "U"
			if urg {
				if t.Urgent == true {
					fmt.Printf("%d. %s%s%s %s\n", i+1,ColorRed, flag, ColorReset, t.Texte)
				}
			}else if done {
				if !t.Fait {
					if t.Urgent{
						fmt.Printf("%d. %s%s%s %s\n", i+1,ColorRed, flag, ColorReset, t.Texte)
					} else {
						fmt.Printf("%d. %s %s\n", i+1, flag, t.Texte)
					}
				}
			} else if t.Urgent {
				fmt.Printf("%d. %s%s%s %s\n", i+1,ColorRed, flag, ColorReset, t.Texte)
			} else if t.Fait {
				fmt.Printf("%d. %sD%s %s\n", i+1, ColorGreen, ColorReset, t.Texte)
			} else {
				fmt.Printf("%d. %s %s\n", i+1, flag, t.Texte)
			}
		}
	},
}

func init() {
	rootCmd.AddCommand(listCmd)
	listCmd.Flags().BoolVarP(&urg, "urgent", "u", false, "liste les taches urgentes")
	listCmd.Flags().BoolVarP(&done, "done", "d", false, "liste les taches non terminees")
}