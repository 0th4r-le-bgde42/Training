package main

import (
	// "bufio"
	// "fmt"
	// "net"
	// "os"
	"serverTreenity/client/cmd"
)

func main() {
	// pid := os.Getegid()
	// if len(os.Args) < 3 {
	// 	fmt.Println("Usage: ./client <ipc-identifier> <message>")
	// 	os.Exit(1)
	// }

	// socketPath := os.Args[1]
	// commande := os.Args[2]

	// conn, err := net.Dial("unix", socketPath)
	// if err != nil {
	// 	fmt.Printf("impossible de joindre le serveur (%s) : %v\n", socketPath, err)
	// 	os.Exit(1)
	// }
	// defer conn.Close()

	// _, err = fmt.Fprintf(conn, "[%d] %s\n", pid, commande)
	// if err != nil {
	// 	fmt.Printf("Erreur d'envoi : %v\n", err)
	// 	os.Exit(1)
	// }

	// reponse, err := bufio.NewReader(conn).ReadString('\n')
	// if err != nil {
	// 	fmt.Printf("Erreur lecture reponse: %v\n", err)
	// 	os.Exit(1)
	// }

	// fmt.Printf("[Client] Reponse du serveur : %s", reponse)
	cmd.Execute()
}