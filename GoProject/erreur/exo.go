package main

import (
	"errors"
	"fmt"
	"strings"
)

var ErrVide = errors.New("entree vide")

func normaliser(s string) (string, error) {
	if strings.TrimSpace(s) == "" {
		return "", fmt.Errorf("normaliser: %w", ErrVide)
	}
	return strings.ToLower(strings.TrimSpace(s)), nil
}

func main() {
	_, err := normaliser("   ")
	if errors.Is(err, ErrVide) {
		fmt.Println("rejeter: l'entree est vide")
	}
	v, _ := normaliser("  Bonjour  ")
	fmt.Printf("noraliserL %q", v)
}