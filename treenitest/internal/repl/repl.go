package repl

import (
	"fmt"
	"io"
	"strings"

	"github.com/chzyer/readline"
	"treenitest/internal/cache"
	"treenitest/internal/cmd"
)

type DynamicCompleter struct{}

func (c *DynamicCompleter) Do(line []rune, pos int) (newLine [][]rune, length int) {
	str := string(line[:pos])
	tokens := strings.Fields(str)

	if len(tokens) == 0 || (len(tokens) == 1 && !strings.HasSuffix(str, " ")) {
		prefix := ""
		if len(tokens) == 1 {
			prefix = tokens[0]
		}
		var candidates [][]rune
		commands := []string{"list", "char", "birthday", "bday", "credits", "help", "exit"}
		for _, cmdName := range commands {
			if strings.HasPrefix(cmdName, prefix) {
				candidates = append(candidates, []rune(strings.TrimPrefix(cmdName, prefix)))
			}
		}
		return candidates, len(prefix)
	}

	command := tokens[0]

	if command == "list" {
		races := []string{"shinigami", "humans", "quincy", "arrancar"}
		prefix := ""
		if len(tokens) == 2 && !strings.HasSuffix(str, " ") {
			prefix = tokens[1]
		}
		var candidates [][]rune
		for _, r := range races {
			if strings.HasPrefix(r, prefix) {
				candidates = append(candidates, []rune(strings.TrimPrefix(r, prefix)))
			}
		}
		return candidates, len(prefix)
	}

	if command == "char" {
		knownRaces := map[string]bool{
			"shinigami": true, "humans": true, "quincy": true, "arrancar": true,
		}

		if len(tokens) == 1 || (len(tokens) == 2 && !strings.HasSuffix(str, " ")) {
			prefix := ""
			if len(tokens) == 2 {
				prefix = tokens[1]
			}
			var candidates [][]rune
			for r := range knownRaces {
				if strings.HasPrefix(r, prefix) {
					candidates = append(candidates, []rune(strings.TrimPrefix(r, prefix)))
				}
			}
			return candidates, len(prefix)
		}

		targetRace := strings.ToLower(tokens[1])
		var pool []string
		var prefix string

		if knownRaces[targetRace] {
			pool = cache.GetCategory(targetRace)
			prefix = strings.TrimPrefix(str, tokens[0]+" "+tokens[1])
			prefix = strings.TrimLeft(prefix, " ")
		} else {
			pool = cache.GetAllNames()
			prefix = strings.TrimPrefix(str, tokens[0])
			prefix = strings.TrimLeft(prefix, " ")
		}

		var candidates [][]rune
		for _, name := range pool {
			if strings.HasPrefix(strings.ToLower(name), strings.ToLower(prefix)) {
				suffix := name[len(prefix):]
				candidates = append(candidates, []rune(suffix))
			}
		}
		return candidates, len(prefix)
	}

	return nil, 0
}

func Start() {
	rl, err := readline.NewEx(&readline.Config{
		Prompt:          "\033[36mbleach >\033[0m ",
		HistoryFile:     "/tmp/bleach_history.tmp",
		AutoComplete:    &DynamicCompleter{},
		InterruptPrompt: "^C",
		EOFPrompt:       "exit",
	})
	if err != nil {
		fmt.Printf("Erreur readline : %v\n", err)
		return
	}
	defer rl.Close()

	for {
		line, err := rl.Readline()
		if err == readline.ErrInterrupt {
			continue
		} else if err == io.EOF {
			break
		}

		line = strings.TrimSpace(line)
		if line == "" {
			continue
		}
		if line == "exit" || line == "quit" {
			break
		}

		args := strings.Fields(line)
		cmd.RootCmd.SetArgs(args)
		if err := cmd.RootCmd.Execute(); err != nil {
			fmt.Printf("Erreur : %v\n", err)
		}
	}
}