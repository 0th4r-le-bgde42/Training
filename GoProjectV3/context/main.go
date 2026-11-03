package main

import (
	"context"
	"fmt"
	"time"
)

type Context interface {
	Done()
	Err() error
	Deadline() (deadline time.Time, ok bool)
	Value(key any) any
}

// func withCancel() {
// 	ctx, cancel := context.WithCancel(context.Background())
// 	defer cancel()

// 	go func ()  {
// 		select {
// 		case <-ctx.Done():
// 			fmt.Println("Travail annule :", ctx.Err())
// 			return
// 		case <-time.After(5*time.Second):
// 			fmt.Println("Travail termine")
// 		}
// 	}()

// 	time.Sleep(1*time.Second)
// 	cancel()
// }

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	go func ()  {
		select {
		case <-ctx.Done():
			fmt.Println("Travail annule :", ctx.Err())
			return
		case <-time.After(5*time.Second):
			fmt.Println("Travail termine")
		}
	}()

	time.Sleep(1*time.Second)
	cancel()
}