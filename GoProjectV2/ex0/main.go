package main

import (
	"fmt"
	"sync"
)

type compteurMots struct {
	mu sync.Mutex
	m map[string]int
}

func (c *compteurMots) ajouter(mot string) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.m[mot]++
}

func main() {
	c := &compteurMots{m : make(map[string]int)}
	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Go(func() {
			for j := 0; j < 1000; j++ {
				c.ajouter("go")
			}
		})
	}
	wg.Wait()

	fmt.Println("go:", c.m["go"])
}