package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("Value has been checked")
	it := 0
	randVal := rand.Intn(100)
	for i := 0; i < 10; i++ {
		
		fmt.Println("Values", randVal)

	}

}
