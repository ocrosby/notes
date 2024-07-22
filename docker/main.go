package main

import (
    "fmt"
    "github.com/go-redis/redis"
)

func main() {
    client := redis.NewClient(&redis.Options{
        Addr: "localhost:6379",
        Password: "",
        DB: 0,
    })

    // Normally you should read the address and the password from a config file or environment variables.

    pong, err := client.Ping().Result()
    if err != nil {
        fmt.Println(err.Error())
        return
    }

    fmt.Println(pong)

    type Person struct {
        Name string         `json:"name"`
        Age int             `json:"age"`
        Occupation string `json:"occupation"`
    }

    jsonString, err := json.Marshal(Person{
        Name: "Elliot",
        Age: 25,
        Occupation: "Software Developer",
    })

    // This sets the value of the key "name" to "Elliot" and sets the expiration time to 0
    // Setting expiration time to 0 means that the key will never expire.
    err = client.Set("person", "Elliot", 0).Err()

    if err != nil {
        fmt.Println("Failed to set value in the redis instance: %s", err.Error())
        return
    }

    val, err := client.Get("person").Result()
    if err != nil {
        fmt.Println("Failed to get value from the redis instance: %s", err.Error())
        return
    }

    fmt.Printf("value retrieved from redis: %s\n", val)
}
