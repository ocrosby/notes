# Kubernetes

To learn Kubernetes I have installed minikube on my local machine.

## Installation

1. Install minikube

```bash
brew install minikube
```

Note: This installes zsh completions to '/opt/homebrew/share/zsh/site-functions'.


2. Specify a Virtualization Driver

When running on Apple Silicon, you can use Docker as the minikube driver.

To set docker as the default driver for Minikube, run:

```bash
minikube config set driver docker
```

You will be warned that these changes will take effect upon a minikube delete and then a minikube start.


3. Start minikube

```bash
minikube start
```

This configures kubectl to use "minikube" cluster and "default" namespace by default.


## FAQ

### How to access the Kubernetes dashboard?

```bash
minikube dashboard
```

This will open the Kubernetes dashboard in your default browser.


