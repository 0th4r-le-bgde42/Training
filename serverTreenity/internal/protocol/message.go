package protocol

type Request struct {
	Action string `json:"action"`
	Prefix string `json:"prefix,omitempty"`
	Offset int `json:"offset,omitempty"`
}

type Response struct {
	Topics []string `json:"topics"`
	Error string `json:"error,omitempty"`
}