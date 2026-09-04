package utils

import (
	"fmt"
	"strings"
	"strconv"
	"math/rand"
)

func GetGretting(name string) string {
	return "Bonjour " + name + ". Bienvenue dans Go.\n"
}

func Calc() {
	var a, b int
	fmt.Print("Entrez le premier nombre : ")
	fmt.Scanln(&a)
	fmt.Printf("Entrez le deuxieme nombre : ")
	fmt.Scanln(&b)

	fmt.Println("Addition :", a+b)
	fmt.Println("Soustraction :", a-b)
	fmt.Println("Multiplication :", a*b)
	if a != 0 && b != 0{
		fmt.Println("Division :", a/b)
	} else {
		fmt.Println("Division par 0 impossible")
	}
	fmt.Println("Modulo :", a%b)
}

func Days() {
	var day string
	fmt.Println("\nEntrez un jour de la semaine : ")
	fmt.Scanln(&day)
	clean_day := strings.ToLower(day)
	switch clean_day {
		case "lundi":
			fmt.Println("Debut de la semaine")
		case "mardi", "mercredi":
			fmt.Println("Millieu de semaine")
		case "jeudi", "vendredi":
			fmt.Println("Presque le weekend")
		default:
			fmt.Println("C'est le weekend !")
	}
}

func CheckInt(prompt string) int {
	var input string
	for {
		fmt.Scanln(&input)
		val, err := strconv.Atoi(input)
		if err == nil {
			return val
		}
		fmt.Printf("Erreur: %s n'est pas un entier valide.\n", prompt)
	}
}

func Devinette(name string) {
	num := rand.Intn(100) + 1
	var input string
	var mode string

	fmt.Println("Lancement de la Devinette,\nrentre un nombre entre 1 et 100 et essaye de trouver le bon!\nIndice: 'Le sens de la vie'")

	for {
		fmt.Print("\nMais d'abord, choisis un mode: 'infini' ou 'limite' : \n")
		fmt.Scanln(&mode)

		if mode == "infini" || mode == "limite" {
			break
		} else {
			fmt.Println("Je n'ai pas compris, reessaye avec une bonne commande.")
		}
	}

	if mode == "limite" {
		var attempt string
		fmt.Print("Tu veux comien d'essaies : ")
		var attempt_int int = CheckInt(attempt)
		for attempt_int > 0 {
			fmt.Print("\nChoisis un nombre entier : ")
			var val int = CheckInt(input)
			attempt_int--

			if val == num {
				fmt.Printf("Bien vue, le nombre attendu etait bien %d!\n", num)
				Relance(name)
				return
			} 
			if attempt_int == 0 {
				fmt.Printf("Dommage, tu n'as pas reussi a trouver...\nLe nombre etait %d\n", num)
				Relance(name)
				return
			} 
			if val < num {
				fmt.Printf("Et non, le chiffre est trop petit..\nPlus que %d essaies\n", attempt_int)
			} else {
				fmt.Printf("Et non, le chiffre est trop grand..\nPlus que %d essaies\n", attempt_int)
			}
		}
	} else if mode == "infini" {
		try := 0
		devine := false
		for !devine {
			fmt.Println("\nChoisis un nombre entier : ")
			var val int = CheckInt(input)
			try++

			if val == num {
				fmt.Printf("Bien vue, le nombre attendu etait bien %d!\nTu as trouve en %d essaies.\n", num, try)
				devine = true
				Relance(name)
				return
			} else if val < num {
				fmt.Println("Et non, le chiffre est trop petit..")
			} else {
				fmt.Println("Et non, le chiffre est trop grand..")
			}
		}
	}
}

func Relance(name string) {
	for {
		var choice string
		fmt.Print("\nVeut tu relancer une partie? [Oui/Non] : ")
		fmt.Scanln(&choice)

		if choice == "Oui" || choice == "oui" {
			Devinette(name)
			return
		} else if choice == "Non" || choice == "non" {
            fmt.Printf("A bientot %s !\n", name)
            return
		} else {
			fmt.Printf("Je n'ai pas compris, reessaye avec une bonne commande.\n")
		}
	}
}