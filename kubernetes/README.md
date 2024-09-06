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


The cluster is made up of one or more control plane nodes and a bunch of workers.

The control plane is the brains of the cluster.  The workers is where we run our user or business apps.

We take the app code and containerize it.  We take that and wrap it in a Pod.  We then wrap that pod in a deployment.

We define all of this in a Kubernetes YAML file.

We give the file to Kubernetes and it makes it all happen.

### Control Plane Nodes

H/A means high availability.  It means that if one of the control plane nodes goes down, the other one can take over.

The control plane is responsible for making sure that the desired state of the cluster matches the actual state.

Select an odd number and stick them in different failure domains that are connected by fast reliable networks.

For the most part 3 control plane nodes is the magic number.  If you are super serious about it, you can go to 5.
Any more than that is overkill.


Services that make up the control plane

* kube-apiserver


The kube-apiserver is the front end for the Kubernetes control plane.  It is designed to scale horizontally.
When we send a command to the control plane, it goes through the kube-apiserver.
When we get a response back, it comes back through the kube-apiserver.

Other control plane services all talk to each other via the kube-apiserver.

- exposes the API (REST)
- Consumes JSON/YAML


* Cluster store
- Persists cluster state & config
- Based on etcd
- Distributed across all control plane nodes
- Super critical to cluster operations
- Performance is critical


* kube-controller-manager
- Controller of controllers

Node controller
Deployment controller
Endpoints controller

* kube-scheduler
- Watches API Server for work
- Assigns tasks to worker nodes

Affinity/Anti-affinity
Constraints
Taints
Resources

Note: In managed Kubenretes in the cloud the contorl plane nodes are managed for you.


### Worker Nodes

Worker nodes are the machines that run the applications. They are responsible for


Simpler than control plane nodes

- kubelet
- kube-proxy
- Container runtime

The kubelet is the main kubernetes agent that runs on every node
You can start with a windows or a linux node
installing the kubnlet registeres the node with the cluster
Work on a kubernetes cluster is done in pods
A pod is one or more containers packaged together in a single unit of deployment
It needs a container runtime. the container runtime is the software that is responsible for running containers
on most modern clusters, they are using containerd
Lookup gVisor and kata containers
container runtimes take care of the low level start and stop containers


The kube-proxy is a network proxy that runs on each node in the cluster
Pod IP addresses
if you are running multiple pods they are all using the same POD IP address


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





