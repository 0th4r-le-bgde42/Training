package cmd

import (
	"bufio"
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var listCmd = &cobra.Command{
	Use: "list",
	Short: "Affiche les taches",
	Run: func(cmd *cobra.Command, args []string) {
		f, err := os.Open("todos.txt")
		if err != nil {
			if os.IsNotExist(err) {
				fmt.Println("Aucune tache enregistree pour le moment")
				return
			}
			fmt.Printf("Erreur de lecture : %v\n", err)
			return
		}
		defer f.Close()

		fmt.Println("--- Vos Taches ---")
		scanner := bufio.NewScanner(f)
		num := 1
		for scanner.Scan() {
			fmt.Printf("%d. %s\n", num, scanner.Text())
			num++
		}

		if err := scanner.Err(); err != nil {
			fmt.Printf("Erreur pendant la lecture: %v\n", err)
		}
	},
}

func init() {
	rootCmd.AddCommand(listCmd)
}