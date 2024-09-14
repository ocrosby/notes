# AWS Notes

## Overview

- Basics of AWS
- Shared REsponsibility Model
- Account Creation
- Global Infrastructure
- Permissions
- AWS Identity
- Access Management

### What is AWS?

Amazon Web Services (AWS) is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services form data centers globally.


### The Shared Responsibility Model

### The AWS Account

### Introduction to the AWS Console

### AWS Service Categories

### AWS Icons and Diagrams

## AWS Identity and Access Management

## AWS Network Services

- VPC
- Route 53

## AWS Compute Services

- EC2
- Lambda

## AWS Storage Services

- EBS
- S3

## AWS Database Services

- RDS
- DynamoDB

## AWS High Availability Services

## AWS Analytics Services

## AWS Management Tools

## AWS Monitoring and Automation Tools

## AWS Security Services

## AWS Developer Services

## AWS Billing and Cost Management


## Six Pillars of the AWS Well Architected Framework

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability


Most widely used service categories:

- Compute
- Storage
- Databases
- Networking
- Security

The AWS global infrastructure is composed of regions and availability zones. A region is a physical 
location in the world where AWS has multiple data centers. Availability zones are isolated locations 
within a region that are engineered to be isolated from failures in other availability zones.

the aws infrastructure is built around regions
22 regions worldwide

resources in one region are not automatically replicated to other regions

each region has multiple availability zones
each availability zone is a fully isolated partition of the AWS infrastructure

- there are currently 69 availability zones worldwide
- availability zones consist of discrete data centers
- they are designed for fault isolation
- they are interconnected with other availability zones by using high-speed private networking
- you choose your availability zones
- AWS recommends replicating data and resources across availability zones for resliliency


Example

Region eu-west-1
- availability zone eu-west-1a
    - data center 1
    - data center 2
    - data center 3
- availability zone eu-west-1b
- availability zone eu-west-1c

while deploying workloads in a region make sure you are using multiple availability zones for resiliency

an availability zone is the most granular level of the AWS infrastructure
the data center is the most granular level of the availability zone


## Compute Services

Elastic Compute Cloud (EC2)
EC2 Auto Scaling
Amazon Elastic Container 
ECR (Elastic Container Registry)
Elastic Beanstalk (EB)
AWS Lambda (Serverless)
Elastic Kubernetes Service (EKS)
Fargate (Compute Engine for Amazon ECS)


### Instance Types

               | General Purpose    | Compute Optimized | Memory Optimized    | Storage Optimized        | Accelerated Computing |
Instance Types | a1, m4, m5, t2, t3 | c4, c5            | r4, r5, x1, z1      | i3, h1, d2               | p2, p3, g3, g4, f1    |
Use Cases      | Broad              | High Performance  | In-memory databases | Distributed file systems | Machine Learning      |

Compute Optimized: c4, c5



To read more [click here](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc).

## Resources

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/)
