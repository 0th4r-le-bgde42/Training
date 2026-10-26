package tmain

import (
	"errors"
	"fmt"
	"os"
)

func BrutError() {
	f, err := os.Open("config.yaml")
	if err != nil {
		fmt.Println("Erreur: ", err)
		return
	}
	defer f.Close()
}

var ErrIntrouvable = errors.New("ressource introuvable")

func charger(id int) error {
	if id == 0 {
		return fmt.Errorf("charger id=%d: %w", id, ErrIntrouvable)
	}
	return nil
}

type ErrValidation struct{ Champ string }
func (e *ErrValidation) Error() string { return "champ invalide: " + e.Champ}

func tmain() {
	BrutError()
	fmt.Println(charger(0))
	err := charger(0)
	fmt.Println(errors.Is(err, ErrIntrouvable))

	err2 := fmt.Errorf("wrap: %w", &ErrValidation{Champ: "id"})
	var ev *ErrValidation
	if errors.As(err2, &ev) {
		fmt.Println("champ en cause:", ev.Champ)
	}
}