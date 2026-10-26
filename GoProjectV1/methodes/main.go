package main

import "fmt"


type Compteur struct {
	n int
}

func (c *Compteur) Increment() { c.n++ } // Recepteur pointeur

func (c Compteur) Valeur() int { return c.n } // Recepteur valeur


type Celsius float64

func (c Celsius) EnFahrenheit() float64 {
	return float64(c)*9/5 + 32
}


type Rectangle struct {
	Largeur float64
	Hauteur float64
}

func (c Rectangle) Aire() float64 {
	return c.Largeur*c.Hauteur
}

func (c *Rectangle) Agrandir(f float64) {
	c.Hauteur *= f
	c.Largeur *= f
}

func main() {
	c := Compteur{}
	c.Increment()
	c.Increment()
	c.Increment()
	c.Increment()
	fmt.Println(c.Valeur())

	t := Celsius(37)
	fmt.Printf("%.1f°F\n", t.EnFahrenheit())

	rect := Rectangle{Largeur: 3, Hauteur: 4}
	fmt.Println(rect)
	fmt.Println(rect.Aire())
	rect.Agrandir(2)
	fmt.Println(rect)
	fmt.Println(rect.Aire())

}