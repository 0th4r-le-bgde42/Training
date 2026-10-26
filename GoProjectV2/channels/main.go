package main

import (
	"fmt"
	"sync"
)


func sommer(nombres []int, resultats chan <- int, wg *sync.WaitGroup) {
	defer wg.Done()
	s := 0
	for _, n := range nombres {
		s += n
	}
	resultats <- s
}

func result() int{
	nombres := []int{1, 2, 3, 4, 5, 6, 7, 8}
	resultats := make(chan int, 2)
	var wg sync.WaitGroup

	milieu := len(nombres) / 2
	wg.Add(2)
	go sommer(nombres[:milieu], resultats, &wg)
	go sommer(nombres[milieu:], resultats, &wg)

	wg.Wait()
	close(resultats)

	total := 0
	for partiel := range resultats {
		total += partiel
	}

	return total
}

func add() int{
	val := []int{1,2,3,4,5,6,7,8}

	ch := make(chan int, 2)
	compenser := 0
	moyenne := len(val) / 2
	var wg sync.WaitGroup

	for i := moyenne; i <= len(val); i += moyenne{
		wg.Add(1)
		go func(l []int){
			defer wg.Done()
			total := 0
			for _, pipi := range l{
				total += pipi
			}
			ch <- total
		}(val[compenser:i])
		compenser = moyenne
	}

	wg.Wait()
	close(ch)

	final := 0
	for midable := range ch{
		final += midable
	}

	return final
}

func main(){
	// --- test channels 1 ---
	ch := make(chan int)
	go func() { ch <- 42 }()
	v := <-ch
	fmt.Printf("--- Test channels 1 ---\n")
	fmt.Println(v)


	// --- test channels 2 ---
	jobs := make(chan int, 5)
	res := make(chan int, 5)
	var wg sync.WaitGroup

	for w := 1; w <= 3; w++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := range jobs {
				res <- j * j
			}
		}()
	}

	for i := 1; i <= 5; i++ {
		jobs <- i
	}
	close(jobs)

	wg.Wait()
	close(res)

	total := 0
	for r := range res {
		total += r
	}
	fmt.Printf("\n--- Test channels 2 ---\n")
	fmt.Printf("%d\n", total)


	fmt.Printf("\n-- Ex moi/mschappe --\n%d\n", add())
	fmt.Printf("\n-- Ex Stephane --\n%d\n", result())
}