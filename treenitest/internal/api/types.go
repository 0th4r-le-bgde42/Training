package api

type NameStruct struct {
	English string `json:"english"`
	Kanji   string `json:"kanji"`
	Romaji  string `json:"romaji"`
}

type ZanpakutoStruct struct {
	Shikai       string `json:"shikai,omitempty"`
	Bankai       string `json:"bankai,omitempty"`
	Resurreccion string `json:"resurrección,omitempty"`
}

type StatsStruct struct {
	Race      string          `json:"race"`
	Birthday  string          `json:"birthday"`
	Gender    string          `json:"gender"`
	Height    string          `json:"height"`
	Weight    string          `json:"weight"`
	Zanpakuto ZanpakutoStruct `json:"Zanpakutō"`
}

type Charac struct {
	ID          string      `json:"id"`
	Slug        string      `json:"slug"`
	Name        NameStruct  `json:"name"`
	Description string      `json:"description"`
	Stats       StatsStruct `json:"stats"`
}

type CharacterSearchResponse struct {
	Results []Charac `json:"results"`
}

type Credits struct {
	Name string `json:"name"`
	Description string `json:"description"`
	Supports []string `json:"supports"`
	Author string `json:"author"`
	Contact string `json:"contact"`
}