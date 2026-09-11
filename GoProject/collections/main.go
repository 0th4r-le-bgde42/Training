package main

import (
	"fmt"
	"sort"
)



func main() {
	var tab [3]int = [3]int{1, 2, 3} // taille fixe
	sli := []int{1, 2, 3} // taille variable
	sli = append(sli, 4)
	fmt.Println(tab, sli)

	s := make([]int, 0, 2)
	fmt.Printf("len=%d cap=%d\n", len(s), cap(s))
	for i := 1; i <= 3; i++ {
		s = append(s, i)
		fmt.Printf("apres append(%d): len=%d cap=%d\n", i, len(s), cap(s))
		// la len de s grandit jusqu'a 2 avec une capacite max atteinte,
		// mais make realloue un tableau plus grand pour acceuilir le troisieme element
		// len=0 dap=2
		// apres append(1): len=1 cap=2
		// apres append(2): len=2 cap=2
		// apres append(3): len=3 cap=4
	}


	base := []int{10, 20, 30, 40}
	vue := base[1:3]
	vue[0] = 99
	fmt.Println(base)
	// ici on a modifier toute la base alors qu'on ne voulait toucher que le vue
	// [10, 20, 30, 40] devient [10 99 12 40]
	// on fait alors
	base2 := []int{10, 20, 30, 40}
	indep := make([]int, 2)
	copy(indep, base2[1:3])
	indep[0] = 99
	fmt.Println(base2, indep)
	// on a donc [10 20 30 40] [99 30]
	// un sous-slice partage la mémoire de son parent.
	// Dès qu'on doit modifier une portion sans toucher l'original, utiliser copy.


	stock := map[string]int{"pommes": 5, "poires": 3}
	stock["bananes"] = 7

	if n, ok := stock["pommes"]; ok { // le second retour 'ok' verifie existance de la cle, faut 'false' si absent
		fmt.Println("pommes en stock:", n)
	}
	delete(stock, "poires") // supprime de map

	stock["peches"] = 2
	stock["abricots"] = 1
	cles := make([]string, 0, len(stock))
	for k := range stock {
		cles = append(cles, k)
	}
	sort.Strings(cles)
	for _, k := range cles {
		fmt.Printf("%s: %d\n", k, stock[k])
	}

	fmt.Println("\nexercice d'application: ")
	compteur()
}

func compteur() {
	phrase := []string{"go", "est", "simple", "go", "est", "rapide", "go"}
	compte := map[string]int{}

	for _, mot := range phrase {
		compte[mot]++
	}
	fmt.Println(compte)
	fmt.Println("'go' apparait", compte["go"], "fois")
}