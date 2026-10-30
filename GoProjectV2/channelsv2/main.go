package main

import (
	"fmt"
	"time"
)

func main() {
	debut := time.Now()
	ch := make(chan string)

	go func() {
		time.Sleep(300 * time.Millisecond)
		ch <- "coffee ready"
	}()

	fmt.Printf("[%.0f ms] waiting on channel\n", time.Since(debut).Seconds()*1000)
	message := <-ch
	fmt.Printf("[%.0f ms] received: %s\n\n", time.Since(debut).Seconds()*1000, message)

	ch1 := make(chan int, 3)

	ch1 <- 1
	ch1 <- 2
	fmt.Printf("apres 2 envois: len=%d cap=%d\n", len(ch1), cap(ch1))

	fmt.Println("recu:", <-ch1)
	fmt.Printf("apres 1 reception: len=%d cap=%d\n", len(ch1), cap(ch1))
	ch1 <- 12
	ch1 <- 13
	fmt.Printf("apres 2 envois supplementaires: len=%d cap=%d\n", len(ch1), cap(ch1))
	fmt.Println("recu:", <-ch1)
	fmt.Printf("apres 1 reception: len=%d cap=%d\n\n", len(ch1), cap(ch1))

	fmt.Printf("Fermeture de channels\n")
	ch2 := make(chan int, 2)
	ch2 <- 10
	ch2 <- 20
	close(ch2)

	v1, ok1 := <-ch2
	fmt.Printf("v=%d of=%t\n", v1, ok1)
	v2, ok2 := <-ch2
	fmt.Printf("v=%d of=%t\n", v2, ok2)
	v3, ok3 := <-ch2
	fmt.Printf("v=%d of=%t\n\n", v3, ok3)

	fmt.Printf("Select Usage\n")
	api := make(chan string)
	cache := make(chan string)

	go func() {
		time.Sleep(200 * time.Millisecond)
		api <- "reponse de l'API"
	}()
	go func() {
		time.Sleep(20 * time.Millisecond)
		cache <- "reponse du cache"
	}()

	select {
	case reponse := <-api:
		fmt.Println("gagnant:", reponse)
	case reponse := <-cache:
		fmt.Println("gagnant:", reponse)
	}
}
