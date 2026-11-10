package cmd

import (
	"encoding/json"
	"fmt"
	"net/url"
	"sort"
	"strings"

	"treenitest/internal/api"
	"treenitest/internal/cache"

	"github.com/spf13/cobra"
)

var (
	limitFlag int
	sortFlag bool
	tailFlag bool
)

var listCmd = &cobra.Command {
	Use: "list [category]",
	Short: "list categories",
	Args: cobra.ExactArgs(1),
	PostRun: func(cmd *cobra.Command, args []string) {
		limitFlag = 0
		sortFlag = false
		tailFlag = false
	},
	RunE: func(cmd *cobra.Command, args []string) error {
		category := strings.ToLower(args[0])
		endpoint := "/" + url.PathEscape(category)

		data, err := api.FetchEndpoint(endpoint)
		if err != nil {
			return err
		}

		var res map[string][]string
		if err := json.Unmarshal(data, &res); err != nil {
			return fmt.Errorf("format de réponse invalide : %w", err)
		}

		noms, ok := res[category]
		if !ok {
			return fmt.Errorf("aucune donnée trouvée pour '%s'", category)
		}
		cache.SetCategory(category, noms)

		if sortFlag {
			sort.Strings(noms)
		}

		total := len(noms)

		result := noms
		if limitFlag > 0 && limitFlag < total {
			if tailFlag {
				result = noms[total-limitFlag:]
			} else {
				result = noms[:limitFlag]
			}
		}

		fmt.Printf("\n=== %s (%d trouvés / %d) ===\n", strings.ToUpper(category), len(result), total)
		for _, nom := range result {
			fmt.Printf("  • %s\n", nom)
		}

		return nil
	},
}

func init() {
	RootCmd.AddCommand(listCmd)
	listCmd.Flags().IntVarP(&limitFlag, "limit", "l", 0, "Nombre max d'éléments à afficher (0 = tous)")
	listCmd.Flags().BoolVarP(&sortFlag, "sort", "s", false, "Trier par ordre alphabétique")
	listCmd.Flags().BoolVarP(&tailFlag, "tail", "t", false, "Afficher les derniers éléments au lieu des premiers")
}