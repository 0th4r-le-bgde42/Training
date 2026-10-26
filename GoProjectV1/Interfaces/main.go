package main

import (
	"fmt"
	"strings"
)

type Notifier interface {
	Notifier(message string) string
}

type Console struct{}
func (Console) Notifier(m string) string { return "console: " + m }

type Email struct{ Dest string }
func (e Email) Notifier(m string) string {
	return fmt.Sprintf("email->%s: %s", e.Dest, strings.ToUpper(m))
}


func alerter(n Notifier, msg string) string {
	return n.Notifier(msg)
}


type MonErreur struct{}
func (*MonErreur) Error() string { return "boum"}

func mauvais() error {
	var p *MonErreur
	return p
}

func main() {

	fmt.Println(alerter(Console{}, "disque plein"))
	fmt.Println(alerter(Email{Dest: "ops@x"}, "disque plein"))

	// var n Notifier = Email{Dest: "a@b"}
	var n Notifier = Console{}
	switch v := n.(type) {
	case Email:
		fmt.Println("c'est un Email pour", v.Dest)
	case Console:
		fmt.Println("C'est une Console")
	}

	fmt.Println(mauvais() == nil)
}