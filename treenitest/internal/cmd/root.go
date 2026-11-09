package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var RootCmd = &cobra.Command{
	Use: "Bleach",
	Short: "Bleach API Interactive Explorer",
	// SilenceErrors: true,
	// SilenceUsage: true,
}

func Execute() {
	if err := RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}