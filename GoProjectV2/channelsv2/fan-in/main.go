package main

import "sync"

func fusionner(entrees ...<-chan string) <-chan string {
	sortie := make(chan string)
	var wg sync.WaitGroup

	for _, entree := range entrees {
		wg.Add(1)
		go func(c <-chan string) {
			defer wg.Done()
			for v := range c {
				sortie <- v
			}
		}(entree)
	}
	go func() {
		wg.Wait()
		close(sortie)
	}()
	return sortie
}

func main() {
	var web chan string
	fusionner(web)
}
