package api


type NameStruct struct {
	Kanji string `json:"Kanji"`
	Romaji string `json:"romaji"`
}

type Zanpakt struct {
	Resurrección string `json:"resurrección"`
}

type StatsStruct struct {
	Race string `json:"race"`
	Birthday string `json:"birthday"`
	Gender string `json:"gender"`
	Zanpakuto Zanpakt `json:"Zanpakuto"`
}

type Charac struct {
	Name NameStruct `json:"name"`
	Description string `json:"description"`
	Stats StatsStruct `json:"stats"`
}


// type RespHumans struct {
// 	Humans []string `json:"humans"`
// }

// type RespShinigami struct {
// 	Shinigami []string `json:"shinigami"`
// }