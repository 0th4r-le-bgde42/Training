package api

import "fmt"

func FindCharacter(name string) (*Charac, error) {
	races := []string{"shinigami", "humans", "quincy", "arrancar"}

	for _, race := range races {
		perso, err := FetchCharacter(race, name)
		if err == nil && perso != nil && perso.Name.English != "" {
			return perso, nil
		}
	}

	return nil, fmt.Errorf("personnage '%s' introuvable dans aucune catégorie", name)
}