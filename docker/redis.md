# Redis

Pulling the redis image

```Shell
docker pull redis
```

Running a Redis container

```Shell
docker run --name redist-test-instance -p 6379:6379 -d redis
```

This command will create a new Redis container with the name `redis-test-instance` and expose the default Redis port `6379`.
It also runs in detached mode.


```Go
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
    
    // This sets the value of the key "name" to "Elliot" and sets the expiration time to 0
    // Setting expiration time to 0 means that the key will never expire.
    err = client.Set(context.Background(), "name", "Elliot", 0).Err()
    
    if err != nil {
        fmt.Println("Failed to set value in the redis instance: %s", err.Error())
        return
    }
    
    val, err := client.Get(context.Background(), "name").Result()
    if err != nil {
        fmt.Println("Failed to get value from the redis instance: %s", err.Error())
        return
    }
    
    fmt.Printf("value retrieved from redis: %s\n", val)
}

```


# References

- [Begginner's Guide to Redis with Go! - Video](https://www.youtube.com/watch?v=1C3Ym_JjkMw)
