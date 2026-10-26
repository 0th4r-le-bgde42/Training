package main

import (
	"fmt"
	"strconv"
)

func somme(num ...int) (somme int, nbr_arg int) {
	if len(num) == 0 {
		return
	}

	for _, n := range num {
		somme += n
	}

	return somme, len(num)
}

func moyenne(num ...int) float64 {
	sum, total_arg := somme(num...)
	if total_arg == 0 {
		return 0.0
	}
	return float64(sum) / float64(total_arg)
}

func inputArg() []int {
	var nums []int
	var input string

	fmt.Println("Entrz vos nombres un par un, ou entrer 'q pour terminer la selection : ")
	for {
		fmt.Print("> ")
		fmt.Scanln(&input)

		if input == "q" || input == "Q" {
			break
		}
		val, err := strconv.Atoi(input)
		if err != nil {
			fmt.Println("Veuillez entrer un entier valide ou 'q'.")
			continue
		}
		nums = append(nums, val)
	}
	return nums
}

func main() {
	n1 := inputArg()
    fmt.Printf("Moyenne de %v : %.2f", n1, moyenne(n1...))
}