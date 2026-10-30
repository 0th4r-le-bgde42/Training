package main

import (
	"fmt"
	"strings"
	"sync"
	"time"
)

func signals() {
	arret := make(chan struct{})
	var wg sync.WaitGroup

	for i := 1; i <= 3; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			for {
				select {
				case <-arret:
					fmt.Printf("worker %d : arret demande\n", id)
					return
				default:
					time.Sleep(50 * time.Millisecond)
				}
			}
		}(i)
	}

	time.Sleep(150 * time.Millisecond)
	close(arret)
	wg.Wait()
	fmt.Printf("tous les workers sont arretes\n\n")
}

func produire(lignes []string) <-chan string {
	sortie := make(chan string)
	go func() {
		defer close(sortie)
		for _, ligne := range lignes {
			sortie <- ligne
		}
	}()
	return sortie
}

func filtrerErreurs(entree <-chan string) <-chan string {
	sortie := make(chan string)
	go func() {
		defer close(sortie)
		for ligne := range entree {
			if strings.HasPrefix(ligne, "ERROR") {
				sortie <- ligne
			}
		}
	}()
	return sortie
}

func main() {
	signals()

	journal := []string{
		"INFO démarrage du service",
		"ERROR connexion refusée sur 5432",
		"INFO requête traitée",
		"ERROR timeout upstream",
	}

	for erreur := range filtrerErreurs(produire(journal)) {
		fmt.Println("alerte:", erreur)
	}
}
