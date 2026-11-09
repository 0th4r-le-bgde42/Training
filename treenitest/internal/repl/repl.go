package repl

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"treenitest/internal/cmd"
)

func Start() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("=== Bleach Interactive CLI ===")

	for {
		fmt.Print("bleach > ")
		if !scanner.Scan() {
			fmt.Println("\nFermeture.")
			break
		}

		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			continue
		}
		if line == "exit" {
			fmt.Println("Goodbye !")
			break
		}

		args := strings.Fields(line)

		cmd.RootCmd.SetArgs(args)
		if err := cmd.RootCmd.Execute(); err != nil {
			fmt.Printf("Erreur : %v\n", err)
		}
	}
}