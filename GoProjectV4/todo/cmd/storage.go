package cmd

import (
	"encoding/gob"
	"os"
)

const fichierStorage = "taches.bin"

type Tache struct {
	Texte string
	Urgent bool
	Fait bool
}

func ChargerTaches() ([]Tache, error) {
	f, err := os.Open(fichierStorage)
	if err != nil {
		if os.IsNotExist(err) {
			return []Tache{}, nil
		}
		return nil, err
	}
	defer f.Close()

	var taches []Tache
	dec := gob.NewDecoder(f)
	if err := dec.Decode(&taches); err != nil {
		return nil, err
	}
	return taches, nil
}

func SaveTaches(taches []Tache) error {
	f, err := os.Create(fichierStorage)
	if err != nil {
		return err
	}

	defer f.Close()
	enc := gob.NewEncoder(f)
	return enc.Encode(taches)
}