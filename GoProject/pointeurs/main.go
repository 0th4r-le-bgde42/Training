package main

import "fmt"

type Compte struct {
	Solde int
}

func crediterValeur(c Compte, montant int) { c.Solde += montant } // sur une copie
func crediterPointeur(c *Compte, montant int) { c.Solde += montant } // sur l'original

func main() {
	x := 42
	p := &x
	fmt.Println(*p)
	*p = 100
	fmt.Println(x)

	c := Compte{Solde: 50}
	crediterValeur(c, 10)
	fmt.Println(c.Solde)
	crediterPointeur(&c, 10)
	fmt.Println((c.Solde))
}