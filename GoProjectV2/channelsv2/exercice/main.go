package main

import (
	"fmt"
	"time"
)

func interroger(nom string, latence time.Duration, resultats chan<- string) {
	time.Sleep(latence)
	resultats <- fmt.Sprintf("%s: ok", nom)
}

func main() {
	res := make(chan string, 2)

	go interroger("facturation", 80*time.Millisecond, res)
	go interroger("stock", 400*time.Millisecond, res)

	delai := time.After(200 * time.Millisecond)
	recu := 0

	for recu < 2 {
		select {
		case reponse := <-res:
			fmt.Println("recu:", reponse)
			recu++
		case <-delai:
			fmt.Printf("timeout: %d service(s) hors delai\n", 2-recu)
			return
		}
	}
}
