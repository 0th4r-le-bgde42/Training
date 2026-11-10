package cache

import (
	"strings"
	"sync"
)

var (
	mu   sync.RWMutex
	data = make(map[string][]string)
)

func SetCategory(race string, names []string) {
	mu.Lock()
	defer mu.Unlock()
	data[strings.ToLower(race)] = names
}

func GetCategory(race string) []string {
	mu.RLock()
	defer mu.RUnlock()
	return data[strings.ToLower(race)]
}

func GetAllNames() []string {
	mu.RLock()
	defer mu.RUnlock()

	var all []string
	for _, names := range data {
		all = append(all, names...)
	}
	return all
}