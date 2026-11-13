package main

import (
	_ "embed"
	"encoding/json"
	"fmt"
	"net"
	"os"
	"os/signal"
	"serverTreenity/internal/protocol"
	"sort"
	"strings"
	"sync"
	"syscall"
)

//go:embed test_data.json
var testData []byte

type Store struct {
	mu sync.RWMutex
	topics map[string]map[string]any
}

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s <ipc-identifier>\n", os.Args[0])
		os.Exit(1)
	}
	socketPath := os.Args[1]

	store := &Store{
		topics: make(map[string]map[string]any),
	}
	if err := json.Unmarshal(testData, &store.topics); err != nil {
		fmt.Fprintf(os.Stderr, "Erreur de lecture de test_data.json : %v\n", err)
		os.Exit(1)
	}

	_ = os.Remove(socketPath)
	listener, err := net.Listen("unix", socketPath)
	if err != nil {
		fmt.Printf("Erreur creation serveur: %v\n", err)
		os.Exit(1)
	}
	defer listener.Close()
	defer os.Remove(socketPath)

	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-sigChan
		listener.Close()
		os.Remove(socketPath)
		os.Exit(0)
	}()

	fmt.Printf("Serveur en ecoute sur %s...\n", socketPath)

	for {
		conn, err := listener.Accept()
		if err != nil {
			break
		}

		go handleClient(conn, store)
	}
}

func handleClient(conn net.Conn, store *Store) {
	defer conn.Close()

	var req protocol.Request
	if err := json.NewDecoder(conn).Decode(&req); err != nil {
		return
	}

	var resp protocol.Response

	switch req.Action {
	case "list":
		store.mu.RLock()
		for topicName := range store.topics {
			if req.Prefix == "" || strings.HasPrefix(topicName, req.Prefix) {
				resp.Topics = append(resp.Topics, topicName)
			}
		}
		fmt.Println("oui j'ai fait un truc")
		store.mu.RUnlock()
		sort.Strings(resp.Topics)

		if req.Offset > 0 {
			if req.Offset >= len(resp.Topics) {
				resp.Topics = []string{}
			} else {
				resp.Topics = resp.Topics[req.Offset:]
			}
		}
	
	default:
		resp.Error = fmt.Sprintf("Action inconnue : %s", req.Action)
	}

	_ = json.NewEncoder(conn).Encode(resp)
}