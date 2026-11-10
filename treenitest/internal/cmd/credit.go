package cmd

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"treenitest/internal/api"

	"github.com/spf13/cobra"
)

const BaseURL = "https://bleach-api-8v2r.onrender.com"

var creditCmd = &cobra.Command {
	Use: "credits",
	Short: "Display API credits",
	Run: func(cmd *cobra.Command, args []string) {
		resp, err := http.Get(BaseURL)
		if err != nil {
			fmt.Printf("joining server impossible: %v", err)
			os.Exit(1)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusOK {
			fmt.Printf("API Error: status code %d\n", resp.StatusCode)
			os.Exit(1)
		}

		body, err := io.ReadAll(resp.Body)
		if err != nil {
			fmt.Printf("Error in reading data: %v", err)
			os.Exit(1)
		}

		var credits api.Credits
		if err := json.Unmarshal(body, &credits); err != nil {
			fmt.Printf("erreur de décodage JSON : %v", err)
			os.Exit(1)
		}

		fmt.Println("Name :", credits.Name)
		fmt.Println("Description :", credits.Description)
		fmt.Println("Supprots : [", strings.Join(credits.Supports, ", "), "]")
		fmt.Println("Author :", credits.Author)
		fmt.Println("Contact :", credits.Contact)
	},
}

func init() {
	RootCmd.AddCommand(creditCmd)
}