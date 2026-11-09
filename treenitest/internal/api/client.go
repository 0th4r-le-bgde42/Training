package api

import (
	"fmt"
	"io"
	"net/http"
)

const BaseURL = "https://bleach-api-8v2r.onrender.com/characters"

func FetchEndpoint(endpoint string) ([]byte, error) {
	fullURL := BaseURL + endpoint

	resp, err := http.Get(fullURL)
	if err != nil {
		return nil, fmt.Errorf("joining server impossible: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("API Error: status code %d\n", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("Error in reading data: %w", err)
	}

	return body, nil
}