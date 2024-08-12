# Kubernetes

To learn Kubernetes I have installed minikube on my local machine.

## Overview

We package applications into containers describe them in a declarative manifest file and give them to Kubernetes.

Kubernetes automates the distribution and scheduling of application containers across a cluster in a more efficient way.

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


Kubernetes is the defacto standard for container orchestration. It is a platform for automating the deployment, 
scaling, and operations of application containers across clusters of hosts.


## Kubernetes Architecture

Kubernetes is a container orchestration platform that automates the deployment, scaling, and management of 
containerized applications.

* Control Plane Nodes
* Worker Nodes
* Pods (the most fundamental and atomic unit of scheduling in Kubernetes)
* Services
* Deployments
* The API and API Server

### Control Plane Nodes

The control plane is the brain of the Kubernetes cluster. It is responsible for managing the cluster and

* Scheduling applications
* Maintaining applications' desired state
* Scaling applications
* Rolling out new updates
* Monitoring applications
* Rolling back updates
* Exposing applications to the outside world


### Worker Nodes

Worker nodes are the machines that run the applications. They are responsible for

### Pods

A pod is the smallest and simplest Kubernetes object. It is a group of one or more containers that are deployed together on the same host.


### Services

A service is an abstraction that defines a logical set of pods and a policy by which to access them. Services enable a loose coupling between dependent applications.

### Deployments

A deployment is a higher-level concept that manages a ReplicaSet. It provides declarative updates to pods and ReplicaSets.


### The API and API Server

The API server is a component of the Kubernetes control plane that exposes the Kubernetes API. The API server is the front end for the Kubernetes control plane.


## Kubernetes Objects

Kubernetes objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster.

* Pods
* Services
* Namespaces
* Deployments
* ConfigMaps
* Secrets
* Persistent Volumes
* Persistent Volume Claims
* StatefulSets
* DaemonSets
* Jobs
* CronJobs
* Ingress
* Network Policies
* Resource Quotas
* Limit Ranges
* Horizontal Pod Autoscalers
* Pod Disruption Budgets
* Custom Resource Definitions
* Role-Based Access Control
* Service Accounts
* ClusterRoles
* ClusterRoleBindings
* RoleBindings
* Pod Security Policies
* Storage Classes
* Volume Snapshots
* Volume Snapshot Classes
* Volume Attachments


## Kubernetes Commands



## FAQ

### How to access the Kubernetes dashboard?

```bash
minikube dashboard
```

This will open the Kubernetes dashboard in your default browser.


## Setting up ArgoCD

It's a good practice to create a separate namespace for ArgoCD.

```bash
kubectl create namespace argocd
```

kubectl will respond with

```bash
namespace/argocd created
```

Install ArgoCD using the following command:

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

This command will deploy all the necessary components for ArgoCD in your Minikube cluster.

### Expose the ArgoCD Server

Since Minikube doesn't have an external load balancer, you can use port-forwarding to access the ArgoCD server.

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

This command forwards your local port 8080 and the ArgoCD server's port 443.  You can now access the ArgoCD web UI
at https://localhost:8080.


The default username is admin.  To retrieve the initial admin password run the following command:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

This command will output the initial admin password.

Note: Copy everything before the '%' character.


To reset the admin password from the UI, click on `User Info` and then click the `Update Password` button.


At this point ArgoCD should be successfully running in your Minikube instance, and you'll be able to start deploying
applications and managing your Kubernetes clusters through the ArgoCD interface.





