package api

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
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

func FetchCharacter(race, name string) (*Charac, error) {
	cleanRace := strings.ToLower(strings.TrimSpace(race))

	firstName := strings.ToLower(strings.Fields(strings.TrimSpace(name))[0])

	endpoint := fmt.Sprintf("/%s/%s", url.PathEscape(cleanRace), url.PathEscape(firstName))

	data, err := FetchEndpoint(endpoint)
	if err != nil {
		return nil, err
	}

	var resp CharacterSearchResponse
	if err := json.Unmarshal(data, &resp); err != nil {
		return nil, fmt.Errorf("erreur de décodage JSON : %w", err)
	}

	if len(resp.Results) == 0 {
		return nil, fmt.Errorf("aucun résultat pour '%s' (%s)", firstName, cleanRace)
	}

	return &resp.Results[0], nil
}