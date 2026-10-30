package main

import (
	"fmt"
	"sync"
)

type cache struct {
	mu sync.RWMutex
	m  map[string]int
}

func (c *cache) lire(cle string) (int, bool) {
	c.mu.RLock()
	defer c.mu.RUnlock()
	v, ok := c.m[cle]
	return v, ok
}

func (c *cache) ecrire(cle string, val int) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.m[cle] = val
	fmt.Println(c.m[cle])
}

func test_wgGo() {
	var wg sync.WaitGroup
	for i := 1; i <= 3; i++ {
		wg.Go(func() {
			fmt.Println("tâche", i)
		})
	}
	wg.Wait()
}

func test_dataraces() {
	// fmt.Printf("-- avec datarace --\n")
	// compteur := 0
	// var gw sync.WaitGroup
	// for i := 0; i < 100; i++ {
	// 	gw.Go(func ()  {
	// 		for j := 0; j < 1000; j++ {
	// 			compteur++
	// 		}
	// 	})
	// }
	// gw.Wait()
	// fmt.Println("compteur =", compteur, "(attendu 100000)")

	fmt.Printf("\n-- sans datarace --\n")
	compteur2 := 0
	var mu sync.Mutex
	var gw2 sync.WaitGroup
	for i := 0; i < 100; i++ {
		gw2.Go(func() {
			for j := 0; j < 1000; j++ {
				mu.Lock()
				compteur2++
				mu.Unlock()
			}
		})
	}
	gw2.Wait()
	fmt.Println("compteur =", compteur2, "(attendu 100000)")
}

var (
	once   sync.Once
	config string
)

func chargerConfig() {
	fmt.Println("Chargement initial...")
	config = "config chargee"
}

func main() {
	fmt.Printf("--- test wg.Go ---\n")
	test_wgGo()

	fmt.Printf("\n--- test race/Mutex ---\n")
	test_dataraces()

	fmt.Printf("\n--- RWMutex ---\n")
	cle := "test"
	val := 42
	fmt.Println("cle :", cle, "/ val :", val)
	c := cache{m: map[string]int{cle: val}}
	fmt.Println(c.lire(cle))
	fmt.Println(c.lire("pipi"))
	c.ecrire(cle, val)

	once.Do(chargerConfig)
	once.Do(chargerConfig)

	fmt.Println(config)
	valeurUnique := sync.OnceValue(func() int {
		fmt.Println("calcul couteux execute")
		return 42
	})
	fmt.Println(valeurUnique(), valeurUnique(), valeurUnique())
}
