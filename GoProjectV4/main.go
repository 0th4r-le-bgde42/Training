package main

import (
	"os"

	"github.com/spf13/cobra"
)


var verbose bool

func main() {
	root := &cobra.Command{
		Use: "scan",
		Short: "scan inspect local and distant target",
	}
	root.PersistentFlags().BoolVarP(&verbose, "verbose", "v", false, "complete output")

	if err := root.Execute(); err != nil {
		os.Exit(1)
	}
}