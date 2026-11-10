package api

import (
	"encoding/json"
	"net/url"
	"strings"
)

// FindCharacter scanne les listes de noms des 4 catégories pour trouver tous les persos correspondants
func FindCharacter(name string) ([]*Charac, error) {
	q := strings.ToLower(strings.TrimSpace(name))
	races := []string{"shinigami", "humans", "quincy", "arrancar"}

	type target struct {
		race string
		name string
	}

	var toFetch []target
	seen := make(map[string]bool)

	// Étape 1 : On récupère les listes de noms de chaque race et on filtre
	for _, race := range races {
		data, err := FetchEndpoint("/" + url.PathEscape(race))
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

		for _, n := range names {
			lower := strings.ToLower(n)

			// Vérifie si le mot cherché est dans le nom (ex: "kurosaki" dans "Karin Kurosaki")
			matched := false
			for _, w := range strings.Fields(lower) {
				if w == q {
					matched = true
					break
				}
			}
			if !matched && strings.Contains(lower, q) {
				matched = true
			}

			if matched && !seen[lower] {
				seen[lower] = true
				toFetch = append(toFetch, target{race: race, name: n})
			}
		}
	}

	// Étape 2 : On va chercher la fiche complète de chaque perso qui a matché
	var results []*Charac
	for _, t := range toFetch {
		perso, err := FetchCharacter(t.race, t.name)
		if err == nil && perso != nil && perso.Name.English != "" {
			results = append(results, perso)
		}
	}

	return results, nil
}