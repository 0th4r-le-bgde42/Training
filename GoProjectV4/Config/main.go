package main

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/BurntSushi/toml"
	"gopkg.in/yaml.v2"

	"GoProjectV4/todo/cmd"
)

type Serveur struct {
	Hote string `yaml:"hote" toml:"hote"`
	Port int `yaml:"port" toml:"port"`
}

type Config struct {
	Serveur Serveur `yaml:"serveur" toml:"serveur"`
	LogLevel string `yaml:"log_level" toml:"log_level"`
}

type Perso struct {
	Nom string
	Age int
	Status string
}

func chargerYAML(chemin string) (Config, error) {
	var cfg Config
	data, err := os.ReadFile(chemin)
	if err != nil {
		return cfg, err
	}
	if err := yaml.Unmarshal(data, &cfg); err != nil {
		return cfg, err
	}
	return cfg, nil
}

func ChargerTOML(chemin string) (Config, error) {
	var cfg Config
	if _, err := toml.DecodeFile(chemin, &cfg); err != nil {
		return cfg, err
	}
	return cfg, nil
}

func chargerJSON(chemin string) ([]Perso, error) {
	var p []Perso
	data, err := os.ReadFile(chemin)
	if err != nil {
		return nil, err
	}
	if err := json.Unmarshal(data, &p); err != nil {
		return nil, err
	}
	return p, nil
}

func main() {
	yaml, err := chargerYAML("Config/config.yaml")
	if err != nil {
		fmt.Println("Il y a une erreur: ", err)
	} else {
		fmt.Println("YAML complet :", yaml)
	}

	toml, err := ChargerTOML("config.toml")
	if err != nil {
		fmt.Println("Il y a une erreur: ", err)
	} else {
		fmt.Println("TOML: ", toml)
	}

	j, err := chargerJSON("config.json")
	for _, json := range j {
		if err != nil {
			fmt.Println("Il y a une erreur: ", err)
		} else {
			fmt.Println("JSON :", json)
			if json.Status == "Admin" {
				fmt.Printf("%sNom: %s, Age: %d%s\n",cmd.ColorRed, json.Nom, json.Age, cmd.ColorReset)
			} else {
				fmt.Printf("Nom: %s, Age %d\n", json.Nom, json.Age)
			}
		}
	}
}