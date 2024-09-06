# Elastic Kubernetes Service (EKS)

## Setup or preparation steps

### Step 1. Create an AWS account

### Step 2. Create a VPC

### Step 3. Create an IAM role with Security Group

You have to create an AWS user (IAM role) with a list of permissions (Security Group)

### Step 4. Create Cluster Control Plane of the Cluster

Meaning the master nodes

You create the cluster with the IAM role you created in step 3

choose region and VPC for your cluster

set security for your cluster

YOu can use that with the AWS Management console or the AWS CLI


Once the cluster is created you create the worker nodes and connect them to the cluster



Setting up EKS (Elastic Kubernetes Service) clusters for both development and production environments in the US East (N. Virginia) region is a good idea, especially if you’re aiming to gain hands-on experience with Kubernetes in a cloud environment. Here are some considerations:

1.	Isolation of Environments: Having separate clusters for development and production is a best practice. It allows you to test and iterate in your development environment without impacting your production workloads.
2.	Cost Considerations: Running multiple clusters can get expensive, especially in a cloud environment. Keep an eye on your costs, particularly if you plan on using larger instances or adding many resources. You might consider using smaller instance types or spot instances for the development cluster to save on costs.
3.	Region Selection: US East (N. Virginia) is a popular and well-supported AWS region with low latency and access to most AWS services. It’s a solid choice for both development and production clusters.
4.	Learning Opportunities: Setting up both clusters will give you experience with managing Kubernetes across different environments, deploying applications, scaling, monitoring, and handling updates. It’s an excellent way to deepen your understanding of Kubernetes and cloud infrastructure.
5.	Security and IAM Management: Make sure to implement proper security practices, such as role-based access control (RBAC), least privilege IAM roles, and network security policies, to protect both clusters.
6.	CI/CD Pipelines: This setup also provides an opportunity to work with CI/CD pipelines that deploy to both development and production clusters, giving you practical experience in continuous delivery in a cloud-native environment.

Overall, this approach aligns well with your goals, and it’s a valuable project that can enhance your skills in cloud computing and Kubernetes.



## Minimizing Cost

Minimizing costs while running EKS clusters can be achieved through several strategies:

1. Use Spot Instances for Development:

   •	Spot Instances: These offer significant savings (up to 90%) compared to On-Demand instances. They are ideal for non-critical workloads or development environments where interruptions are acceptable.
   •	Spot Instance Automation: Use Spot Instance interruption handling to ensure your workloads can recover automatically if an instance is terminated.

2. Right-Sizing Your Instances:

   •	Smaller Instance Types: Use smaller instance types (e.g., t3.micro or t3.small) for non-production environments.
   •	Cluster Autoscaler: Implement the Kubernetes Cluster Autoscaler to automatically scale down unused nodes, reducing costs during off-peak hours.

3. Use Fargate for Development:

   •	AWS Fargate: Consider using Fargate for your development cluster, which eliminates the need to manage EC2 instances. You only pay for the resources your containers use, which can be more cost-effective for small-scale or intermittent workloads.

4. Optimize Resource Requests and Limits:

   •	Pod Resource Requests/Limits: Ensure that the resource requests and limits for your pods are appropriately set to avoid over-provisioning. Over-provisioning leads to unnecessary costs as it may result in underutilized nodes.

5. Scheduled Scaling:

   •	Scheduled Scaling: If your workload has predictable patterns, use scheduled scaling to adjust the number of nodes during non-peak hours, reducing costs when demand is low.

6. Idle Resource Cleanup:

   •	Cleanup Unused Resources: Regularly clean up unused resources such as idle load balancers, persistent volumes, and other services that continue to incur charges.

7. Leverage AWS Savings Plans and Reserved Instances:

   •	Savings Plans: If you have predictable workloads, consider using AWS Savings Plans or Reserved Instances, which offer up to 72% discount compared to On-Demand pricing.
   •	Reserved Instances: Commit to Reserved Instances for your production environment if you expect it to run continuously.

8. Use Managed Node Groups Wisely:

   •	Managed Node Groups: Use managed node groups in EKS to handle provisioning and lifecycle management of EC2 instances, ensuring that you only pay for what you need.

9. Monitor and Optimize with Cost Management Tools:

   •	AWS Cost Explorer: Use AWS Cost Explorer to monitor and analyze your spending, identify trends, and optimize accordingly.
   •	Kubecost: Consider using tools like Kubecost, which provide visibility into your Kubernetes costs, helping you to optimize resources and reduce waste.

10. Leverage Free Tier and Credits:

    •	AWS Free Tier: Utilize the AWS Free Tier if you’re eligible, particularly for smaller environments or new projects.
    •	AWS Credits: If you have AWS credits (e.g., from promotions or events), apply them to your account to offset costs.

By implementing these strategies, you can effectively minimize the costs associated with running EKS clusters while still gaining valuable experience and maintaining a robust development and production environment.