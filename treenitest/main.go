package main

import (
	"os"
	"treenitest/internal/cmd"
	"treenitest/internal/repl"
)

func main() {
	if len(os.Args) > 1 {
		if err := cmd.RootCmd.Execute(); err != nil {
			os.Exit(1)
		}
		return
	}

	repl.Start()
}