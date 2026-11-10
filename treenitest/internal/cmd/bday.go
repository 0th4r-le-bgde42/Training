package cmd

import (
	"encoding/json"
	"fmt"
	"net/url"
	"strings"
	"sync"

	"github.com/spf13/cobra"
	"treenitest/internal/api"
)

var birthdayCmd = &cobra.Command{
	Use:     "birthday [mois ou date]",
	Aliases: []string{"bday"},
	Short:   "Cherche les personnages nés à une date ou un mois précis (ex: birthday august ou birthday august 31)",
	Args:    cobra.MinimumNArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		query := strings.ToLower(strings.TrimSpace(strings.Join(args, " ")))
		fmt.Printf("Recherche des personnages nés le/en '%s'...\n", query)

		races := []string{"shinigami", "humans", "quincy", "arrancar"}

		type Match struct {
			Name     string
			Race     string
			Birthday string
		}

		var matches []Match
		var mu sync.Mutex
		var wg sync.WaitGroup

		for _, race := range races {
			data, err := api.FetchEndpoint("/" + url.PathEscape(race))
			if err != nil {
				continue
			}

			var raw map[string][]string
			if err := json.Unmarshal(data, &raw); err != nil {
				continue
			}

			names, ok := raw[race]
			if !ok {
				continue
			}

			for _, name := range names {
				wg.Add(1)
				go func(r, n string) {
					defer wg.Done()

					perso, err := api.FetchCharacter(r, n)
					if err != nil || perso.Stats.Birthday == "" {
						return
					}

					bday := strings.TrimSpace(perso.Stats.Birthday)
					if strings.Contains(strings.ToLower(bday), query) {
						mu.Lock()
						matches = append(matches, Match{
							Name:     perso.Name.English,
							Race:     strings.ToUpper(r),
							Birthday: bday,
						})
						mu.Unlock()
					}
				}(race, name)
			}
		}

		wg.Wait()

		if len(matches) == 0 {
			fmt.Printf("Aucun personnage trouvé pour '%s'.\n", query)
			return nil
		}

		fmt.Printf("\n=== RÉSULTATS POUR '%s' (%d trouvé(s)) ===\n", strings.ToUpper(query), len(matches))
		for _, m := range matches {
			fmt.Printf("  • %-26s [%-9s] : %s\n", m.Name, m.Race, m.Birthday)
		}

		return nil
	},
}

func init() {
	RootCmd.AddCommand(birthdayCmd)
}