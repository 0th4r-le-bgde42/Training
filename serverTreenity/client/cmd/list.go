package cmd

import (
	"fmt"
	"serverTreenity/client/ipc"
	"serverTreenity/internal/protocol"

	"github.com/spf13/cobra"
)

var listCmd = &cobra.Command{
	Use: "list",
	Short: "Liste les noms des topics presents sur le serveur",
	Args: cobra.NoArgs,
	RunE: func(cmd *cobra.Command, args []string) error {
		resp, err := ipc.SendRequest(IPCIdentifier, protocol.Request{
			Action: "list",
			Prefix: PrefixFlag,
			Offset: OffsetFlag,
		})
		if err != nil {
			return err
		}

		if RawFlag {
			for _, topic := range resp.Topics {
				fmt.Println(topic)
			}
			return nil
		}

		if len(resp.Topics) == 0 {
			fmt.Println("Aucun topics trouve.")
			return nil
		}

		fmt.Printf("Topics disponibles (%d) :\n", len(resp.Topics))
		for _, topic := range resp.Topics {
			fmt.Printf("  - %s\n", topic)
		}

		return nil
	},
}

func init() {
	rootCmd.AddCommand(listCmd)
}