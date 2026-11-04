package cmd

import (
	"fmt"
	"slices"
	"strconv"

	"github.com/spf13/cobra"
)

var Force bool
var AllDone bool
var All bool

var removeCmd = &cobra.Command{
	Use: "remove [id]",
	Short: "Retire une tache de la liste",
	Args: cobra.MaximumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		taches, err := ChargerTaches()
		if err != nil {
			fmt.Println("Erreur lecture stockage :", err)
			return
		}
		if len(taches) <= 0 {
			fmt.Println("Il n'y a aucune tache a supprimer")
			return
		}

		if All {
			taches = nil
			fmt.Println("Toute la todo liste a ete supprime.")

			if err := SaveTaches(taches); err != nil {
				fmt.Println("Erreur sauvegarde binaire :", err)
				return
			}

			return

		} else if AllDone {
			var restante []Tache

			for _, t := range taches {
				if !t.Fait {
					restante = append(restante, t)
				}
			}

			taches = restante
			if err := SaveTaches(taches); err != nil {
				fmt.Println("Erreur sauvegarde binaire :", err)
				return
			}

			fmt.Println("Toutes les taches terminees ont ete supprimees.")
			return

		} else {
			if len(args) == 0 {
				fmt.Println("Erreur: MErci de preciser l'id de la tache a supprimer")
				return
			}

			id, err := strconv.Atoi(args[0])
			if err != nil {
					fmt.Println("Erreur: l'ID doit etre un nombre valide.")
					return
				}
			index := id -1

			if index < 0 || index >= len(taches) {
				fmt.Println("Erreur: cet ID de tache n'existe pas")
				return
			}

			cible := taches[index]
			if !cible.Fait && !Force {
				fmt.Println("Erreur: la tache n'est pas terminee. Utilise -f pour forcer la suppression.")
				return
			}

			taches = slices.Delete(taches, index, index+1)

			if err := SaveTaches(taches); err != nil {
				fmt.Println("Erreur sauvegarde binaire :", err)
				return
			}

			fmt.Printf("Tache n.%d '%s' supprimee avec succes.\n", id, cible.Texte)
		}
	},
}

func init() {
	rootCmd.AddCommand(removeCmd)
	removeCmd.Flags().BoolVarP(&Force, "force", "f", false, "Force le retirement d'une tache pas encore faite.")
	removeCmd.Flags().BoolVarP(&All, "all", "a", false, "Supprime toute la liste")
	removeCmd.Flags().BoolVarP(&AllDone, "alldone", "d", false, "Supprime les taches marque comme faite.")
}