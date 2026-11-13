package cmd

import (
	"fmt"
	"os"
	"strings"

	"github.com/spf13/cobra"
)

var (
	IPCIdentifier string
	PrefixFlag string
	OffsetFlag int
	RawFlag bool
)

var rootCmd = &cobra.Command{
	Use: "tree_nity <ipc-identifier> <commande> [flags]",
	Short: "Client CLI pour interagir avec le serveur tree_nity",
}

func Execute() {
	args := os.Args[1:]

	if len(args) == 0 || args[0] == "-h" || args[0] == "--help" {
		if err := rootCmd.Execute(); err != nil {
			os.Exit(1)
		}
		return
	}

	if strings.HasPrefix(args[0], "-") {
		fmt.Fprintf(os.Stderr, "Erruer : l'ipc-identifier doit etre le premier argument (recu '%s')\n", args[0])
		os.Exit(1)
	}

	IPCIdentifier = args[0]
	rootCmd.SetArgs(args[1:])

	if err := rootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}

func init() {
	rootCmd.PersistentFlags().StringVarP(&PrefixFlag, "prefix", "p", "", "Filtrer les resultats par prefixe")
	rootCmd.PersistentFlags().IntVarP(&OffsetFlag, "offset", "o", 0, "Ignorer les N premier resultats")
	rootCmd.PersistentFlags().BoolVarP(&RawFlag, "raw", "r", false, "Affichr la sortie brute sans formatage")
}