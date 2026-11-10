package cmd

import (
	"encoding/json"
	"fmt"
	"net/url"
	"strings"
	"sync"
	"sort"
	"strconv"

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
			Day int
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
                    cleanBday := strings.ToLower(strings.ReplaceAll(bday, ",", " "))
                    words := strings.Fields(cleanBday)

                    matched := false
                    if len(strings.Fields(query)) > 1 {
                        if len(words) >= 2 && (words[0]+" "+words[1] == query || words[1]+" "+words[0] == query) {
                            matched = true
                        }
                    } else {
                        for _, w := range words {
                            cleanW := strings.TrimRight(w, "stndrh")
                            if w == query || cleanW == query {
                                matched = true
                                break
                            }
                        }
                    }

                    if matched {
						dayVal := 0
						for _, w := range words {
							cleanNum := strings.TrimRight(w, "stndrh")
							if d, err := strconv.Atoi(cleanNum); err == nil && d >= 1 && d <= 31 {
								dayVal = d
								break
							}
						}

						mu.Lock()
						matches = append(matches, Match{
							Name:     perso.Name.English,
							Race:     strings.ToUpper(r),
							Birthday: bday,
							Day:      dayVal,
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

		sort.Slice(matches, func(i, j int) bool {
			if matches[i].Day == matches[j].Day {
				return matches[i].Name < matches[j].Name
			}
			return matches[i].Day < matches[j].Day
		})

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