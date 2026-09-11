package main

import "fmt"

func compteur() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {
	f := func(nom string) {
		fmt.Println("Salut", nom)
	}
	f("Julien")
	func(x int) {
		x = x*2
		fmt.Println("Valeur :", x)
	}(42)
	compte := compteur()
	fmt.Println(compte())
	fmt.Println(compte())
	fmt.Println(compte())
	fmt.Println(compte())
}