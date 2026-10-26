package main

import (
	"encoding/json"
	"fmt"
)

// Struct classique
type Personne struct {
	nom		string
	age		int
	actif	bool
}

// Champs exportes et tags JSON
type User struct {
	Name string `json:"name"`
	Email string `json:"email,omitempty"`
	admin bool
}

// Fonction Constructeur
func NewPersonne(nom string, age int) *Personne {
	return &Personne{
		nom:	nom,
		age: 	age,
		actif:	true,
	}
}

// Composer par embedding
type Adresse struct {
	Ville	string
	CP		string
}

type Client struct {
	Nom	string
	Adresse
}

// Struct imbriquees
type Commande struct {
	ID		string
	Client	Client
}


func main() {
	p1 := Personne{"Louis", 28, true}
	p2 := Personne{
		nom: "Bob",
		age: 25,
	}
	p3 := Personne{nom: "Charlie"}
	p4 := &Personne{nom: "Diana", age: 35}
	fmt.Println(p1, p2, p3, p4)

	p2.age = 26
	fmt.Println(p2.age)
	p4.nom = "Diana Smith"
	fmt.Println(p4.nom)

	u := User{Name: "Bob", admin: true}
	b, _ := json.Marshal(u)
	fmt.Println(string(b))

	c := Client{Nom: "ACME", Adresse: Adresse{Ville: "Paris", CP: "75001"}}
	fmt.Println(c.Ville)
	fmt.Println(c.Adresse.CP)
	
	co := Commande{ID: "1234", Client: c}
	fmt.Println(co.Client.Adresse.CP)
	fmt.Println(co.Client.Nom)

	fmt.Println(Personne{"Al", 1, true} == Personne{"Al", 1, true})
	fmt.Println(Personne{"Be", 1, true} == Personne{"Al", 1, true})

	// Struct anonyme ou vide
	point := struct{X, Y int}{X: 1, Y: 2}
	set := map[string]struct{}{"a": {}, "b": {}}
	fmt.Println(point.X, point.Y)
	_, present := set["a"]
	println(present)
}