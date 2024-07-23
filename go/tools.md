# Tools

If you want to create a repo with command line utilities
to be utilized from go

```Text
my-tools/
├── cmd/
│   └── example/
│       ├── main.go  # Entry point for the example command
│       └── ...      # Other Go files for the command
├── pkg/
│   └── ...          # Shared packages used by your commands
├── go.mod           # Go module file
└── README.md        # Project README
```

A basic example of what main.go inside the cmd/example directory might look like.

```Go
// Path: cmd/example/main.go
package main

import (
    "fmt"
    "github.com/spf13/cobra"
)

func main() {
    var rootCmd = &cobra.Command{
        Use:   "example",
        Short: "Example is a CLI tool for demonstration",
        Long:  `Example is a demonstration CLI tool built with Cobra.`,
        Run: func(cmd *cobra.Command, args []string) {
            fmt.Println("Example command executed")
        },
    }

    if err := rootCmd.Execute(); err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
}
```

