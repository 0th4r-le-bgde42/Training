package main

import (
	"context"
	"fmt"
)


var taille int

type Film struct {
	Title string `json:"title"`
	OGtitle string `json:"original_title"`
	Time int `json:"running_time"`
	Date int `json:"release_date"`
}

func fetchFilm(ctx context.Context, name string) (Film, error) {
	url := fmt.Sprintf("https://ghibliapi.vercel.app/films")
}

func main() {
	taille = 12
	fmt.Printf("taille du pipi: %d", taille)
}
