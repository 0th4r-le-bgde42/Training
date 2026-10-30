package main

import (
	"GoProject/debut/utils"
	"fmt"
)

func main() {
	var name string
	fmt.Println("Hello world!")
	fmt.Print("Entrez votre nom : ")
	fmt.Scanln(&name)
	message := utils.GetGretting(name)
	fmt.Printf("\n%s\n", message)
	// utils.Calc()
	// utils.Days()
	utils.Devinette(name)
}
