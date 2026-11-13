package ipc

import (
	"encoding/json"
	"fmt"
	"net"
	"serverTreenity/internal/protocol"
)

func SendRequest(socketPath string, req protocol.Request) (protocol.Response, error) {
	var resp protocol.Response

	conn, err := net.Dial("unix", socketPath)
	if err != nil {
		return resp, fmt.Errorf("Serveur injoignable (%s) : %w", socketPath, err)
	}
	defer conn.Close()

	if err := json.NewEncoder(conn).Encode(req); err != nil {
		return resp, fmt.Errorf("Erreur d'envoi : %w", err)
	}

	if err := json.NewDecoder(conn).Decode(&resp); err != nil {
		return resp, fmt.Errorf("Erreur de lecture : %w", err)
	}

	if resp.Error != "" {
		return resp, fmt.Errorf("Erreur serveur : %s", resp.Error)
	}

	return resp, nil
}