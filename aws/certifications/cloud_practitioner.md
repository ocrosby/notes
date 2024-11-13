# AWS Certified Cloud Practitioner

## Overview

CLF-C02 Preparation

## Prerequisites

- General computing concepts

## Table of Contents

- About the Exam
- Cloud Foundations and Compute
- Storage, Networking, and Databases
- Deployment, Migration, and AI
- Monitoring, Security, and Pricing
- Exam Preparation

## About the Exam

- What Makes a Cloud Practitioner?
- What to Expect
- Updates from CLF-C01 to CLF-C02

### What Makes a Cloud Practitioner?

This exam is a foundational certification, then there are Associate certifications:

- Solutions Architect - Associate
- Developer - Associate
- SysOps Administrator - Associate

These are more role based.  You should walk into these certifications with some experience.

Next are the Professional certifications:

- DevOps Engineer - Professional
- Solutions Architect - Professional

These are also role based but validate more advanced skills.

You should have 2 years of prior AWS experience to walk into these exams.

Finally, there are Specialty certifications:

- Advanced Networking - Specialty
- Data Anlytics - Specialty
- Database - Specialty
- Machine Learning - Specialty
- Security - Specialty
- SAP on AWS - Specialty

### What to Expect

- 65 questions (Multiple Choice/Response)
- 90 minutes
- $100


You can schedule it at a Pearson VUE Testing Center
Proctored Online


### Updates from CLF-C01 to CLF-C02

#### CLF-C01

- APIS
- Cost Explorer
- AWS Cost and Usage Report
- AWS Command Line Interface (CLI)
- Elastic Load Balancers
- Amazon EC2 instance types (for example, Reserved, On-Demand, Spot)
- AWS global infrastructure (for example, AWS Regions, Availability Zones)
- Infrastructure as Code (IaC)
- Amazon Machine Images (AMIs)
- AWS Management Console
- AWS Marketplace
- AWS Professional Services
- AWS Personal Health Dashboard
- Security Groups
- AWS Service Catalog
- AWS Service Health Dashboard
- Service quotas
- AWS software development kits (SDKs)
- AWS Support Center
- AWS Support tiers
- Virtual private networks (VPNs)


#### CLF-C02

- APIS
- Benefits of migrating to the AWS Cloud
- AWS Cloud Adoption Framework (AWS CAF)
- AWS Compliance
- Compute
- Cost Management
- Databases
- Amazon EC2 instance types (for example, Reserved, On-Demand, Spot)
- AWS global infrastructure (for example, AWS Regions, Availability Zones)
- Infrastructure as Code (IaC)
- AWS Knowledge Center
- Machine Learning
- Management and governance
- Migration and data transfer
- Network services
- AWS Partner Network
- AWS Prescriptive Guidance
- AWS Pricing Calculator
- AWS Professional Services
- AWS re:Post
- Security
- AWS Security Blog
- AWS Security Center
- AWS shared responsibility model
- AWS Solutions Architects
- Storage
- AWS Support Center
- AWS Support plans
- AWS Well-Architected Framework


### What is the cloud?

- AWS has thousands of services scattered across the globe in [data centers](https://aws.amazon.com/compliance/data-center/data-centers/).
- AWS maximizes the use of their servers with virtualization.  
    * Virtualization lets you divide hardware resources on a single physical server into smaller units like a loaf of bread.

Cloud computing is the delivery of computing services over the internet.

Kinds of services

- Compute (EC2) 
- Storage (S3)
- Networking (VPC)
- Databases (RDS)
- Development, Messaging, and Deployment (The Code Family)
- Migration and Transfer (Migration Hub)
- Artificial Intelligence and Machine Learning (SageMaker, Rekognition)
- Auditing, Monitoring, and Logging (Trusted Advisor)
- Security, Compliance, and Governance (IAM, KMS)
- Pricing, Billing, and Support (Cost Explorer, Pricing Calculator)


[Overview of Amazon Web Services - Whitepaper](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-overview/aws-overview.pdf)
 
Make sure to read this very important whitepaper that you should read in full before the exam and then review the day before the exam.  
It contains a list of all the services in AWS broken into categories.


### Exam Tips

Learn the service categories.  For example EC2 is a compute service, VPC is a networking service.
Read the AWS Services Whitepaper.

## Introducing Cloud Computing and Deployment Models

- CapEx vs. OpEx
- Could Computing Advantages and Benefits
- Cloud Computing Models
- Cloud Deployment Models
- Exam Tips


Capital Expenditures (CapEx)
: Capital expenditures are upfront purchases toward fixed assets.

Operating Expenses (OpEx)
: Operating expenses are funds used to run day-to-day operations.


The Six Advantages of Cloud Computing

1. Global in Minutes
2. No Data Center Spend
3. Economies of Scale (Pay for what you use)
4. Speed and Agility
5. Stop Guessing Capacity
6. CapEx for Variable Expense

Benefits:

- High Availability
- Elasticity
- Agility
- Durability 


Cloud Computing Models

- Infrastructure as a Service (IaaS)
- Software as a Service (SaaS)
- Platform as a Service (PaaS)

Cloud Deployment Models

- Private Cloud (on premises)
- Public Cloud (AWS)
- Hybrid Cloud (mix of both)


Exam Tips

- Understand the six advantages of the cloud
- Understand cloud benefits and terminology
- Know computing models IaaS, SaaS, and PaaS
- Know the deployment models, Private, Public, and Hybrid
- Know that Hybrid deployments are supporting by AWS Direct Connect

Exploring Regions and Availability Zones

- AWS Regions
- Region Charachteristics
- AWS Availability Zones
- Availability Zone Characteristics
- Exam Tips

An AWS Region is a Physical Location

Example the Ohio and North Virginia regions reside under th US East geographic location.

Region Characteristics

- Regions are fully independent and isolated (if one goes down the others are not affected)
- Regions are resource and service specific (resources would have to be recreated in another region)
- AWS Regions consist of multiple Availability Zones
- AWS Availability Zones consist of one or more physically separate data centers


AWS defines an availability zone as one or more discrete data centers with redundant power, networking, and 
connectivity in an AWS region.


Availability Zone Characteristics

- each connected via low latency links
- they are fault-tolerant
- they provide high availability


Note:
In order to be considered fault-tolerant an application would have to span across multiple availability zones.

Note:
If an application running across multiple availability zones goes down it could be because the entire region is down.

Exam Tips

- A Region is global and is made up of multiple Availability Zones
- An Availability Zone is made up of multiple data centers
- Multiple availability zone deployments provide high availability and fault tolerance


Revieiwing Edge Locations and Local Zones

Latency Explained

Latency
: The time that passes between a user request and the resulting response

Local Zones place AWS services closer to end-users.

Local Zones are extensions of AWS regions that are geographically close to large populations.


Edge Locations can help to reduce latency.  They aren't used to launch resources but to cache content.


There are more edge locations than regions and availability zones.


Note: Local zones can be used to ensure millisecond latency.

Note: Edge locations can be utilized to lower lateny on a website that is available on multiple continents.

Edge locations are a feature of the CloudFront CDN.


Exam Tips


## Introducing the Frameworks

### Cloud Adoption Framework

The Cloud Adoption Framework (CAF) focuses on using AWS to digitally transform and accelerate business outcomes.

Several Pieces

Perspectives and Foundational Capabilities

#### Security Perspective

**Security**

- Governance
- Assurance
- Application

**Protection**

- Infrastructure
- Data


**Management**

- Identity and Access Management (IAM)
- Vulnerability

#### Business Perspective

**Management**

- Strategy
- Portfolio
- Innovation
- Product

**Data**

- Monetization
- Science

**Business Insight**


#### Perspectivies and Foundational Capabilities

Operations

**Management**

- Event (AIOps)
- Incident and Problem
- Change and Release
- Performance and Capacity
- Configuration
- Patch
- Availability and Continuity
- Application

**Observability**

Governance

**Management**

- Program and Benefits Benefits
- Risk
- Cloud Financial
- Application Portfolio

**Data**

- Governance
- Curation

People

**Transformation**

- Leadership
- Workforce

**Organization**

- Design
- Alignment

**Cloud Fluency**

**Change Acceleration**

**Culture Evolution**

The Cloud Adoption Framework has four domains.

Cloud Transformation Domains.

Domain 1 - Technology

- Migrate and Modernize

Domain 2 - Process

- Digitize, automate, and optimize

Domain 3 - Organization

- Reminagine orchestration

Domain 4 - Product

- Reimagine your business model


Cloud Transformation Journey Phases

**Envision**

Benefits to business outcomes

**Align**

Gaps across perspectives

**Launch**

Deliver initiatives with value

**Scale**

Expand sutainable initiatives


### AWS Well-Architected Framework

[Deep Dive - Course](https://learn.acloud.guru/course/cf52e1dc-2d84-4f01-a9cb-6c010c748790/overview)


Six Pillars of the AWS Well-Architected Framework

- Security
- Cost Optimization
- Performance Efficiency
- Operational Excellence
- Reliability
- Sustainability

Security focuses on protection of data, systems, and any assets used by your workload.
Cost Optimization focuses on the ongoing process of maintaining costs in the cloud.
Performance Efficiency focuses on the ability to use computing resources efficiently to meet requirements.
Operational Excellence focuses on creating applications that successfully support your workload.
Reliability focuses on architecting a workload to be consistent and able to recover quickly.
Sustainability focuses on environmental impacts like energy efficiency and resource consumption.


General Design Principles

- Stop guessing your capacity needs
- Test Systems ad Production Scale
- Consider Evolutionary Architectures
- Automate with Architectural Experimentation in Mind
- Drive Architectures Using Data
- Improve Through Game Days

Exam Tips

- Understand the CAF Perspectiives and the Cloud Transformation Journey Phases (Envision, Align, Launch, Scale)
- Know how those phases encompass the domains and perspectivies
- Know the benefits of using that framework
- Understand the benefits of using the Cloud Adoption Framework
- Understand the Well-Architected Framework pillars, design principles, and how they apply in the real world.

### Meeting the AWS Management Console and Accessing AWS

- The AWS Management Console
- Root User
- The AWS Command Line Interface (CLI)

### Root User

There can be multiple users in an AWS account but there is only one root user.

The root user has full access to all AWS services and resources in the account.

The root user is the only user that can perform certain tasks like closing an account.

The root user should not be used for everyday tasks.


When you create an AWS account your first step should be to enable MFA on the root account.

Create a new user or group in IAM for day to day tasks.

### The AWS Command Line Interface (CLI)

The AWS CLI is a tool that allows you to interact with AWS services from the command line.

The AWS CLI is available for Windows, Mac, and Linux.

The AWS CLI is a powerful tool that can be used to automate tasks.

The AWS CLI is a great way to interact with AWS services without using the AWS Management Console.


#### Command Line Interface

Manage resources from a terminal session


#### Application Code

Access from application code with SDKs using programmatic calls

#### Software Development Kits (SDKs)

Access from programming languages (Java, Python, C#, and more).


### Exam Tips

- The root user should be protected by MFA.
- The root user has power that no other user has.
- The CLI and SDKs are other options to manage AWS resources.


#### Platform Perspective

**Architecture and Engineering**

- Platform
- Data

**Continuous Integration/Continuous Delivery (CI/CD)**

**Modern Application Development**

**Provisioning and Orchestration**



#### Incident Response


#### Threat Detection



### AWS Well-Architected Framework

- An Edge Location ensures low latency by placing content closer to users.
- There are more Edge Locations than Regions and Availability Zones.
- A Local Zone is an extension of a Region enabling things like real-time gaming and video streaming.

## Cloud Foundations and Compute

## Storage, Networking, and Databases

## Deployment, Migration, and AI

## Monitoring, Security, and Pricing

## Exam Preparation

- Know the Service Categories
- Know the Six Advantages of Cloud Computing (Global in Minutes, No Data Center Spend, Economies of Scale, Speed and Agility, Stop Guessing Capacity, CapEx for Variable Expense)
- Cloud Benefits (High Availability, Elasticity, Agility, Durability)
- Know the Cloud Computing Models (IaaS, SaaS, PaaS)
- Know the Cloud Deployment Models (Private, Public, Hybrid)
- Understand that Regions are made up of two or more Availability Zones
- Understand that Availability Zones are made up of multiple data centers
- Understand that Multi-AZ deployments provide high availability and fault tolerance
- Low Latency is good and Edge Locations provide that as an extension of Cloud Front
- Local Zone's are an extension of a Region and provide low latency for things like real-time gaming and video streaming
- Remember that Teh Cloud Adoption Framework has phases and domains
- Remember that the Well-Architected Framework has six pillars (Security, Cost Optimization, Performance Efficiency, Operational Excellence, Reliability, Sustainability)
- 

## Resources

