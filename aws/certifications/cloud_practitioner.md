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
: Captial expenditures are upfront purchases toward fixed assets.

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
- they are fault tolerant
- they provide high availability


Note:
In order to be considered fault tolerant an application would have to span across multiple availability zones.

Note:
If an application running across multiple availability zones goes down it could be because the entire region is down.

Exam Tips

- A Region is global and is made up of multiple Availability Zones
- An Availability Zone is made up of multiple data centers
- Multiple availability zone deployments provide high availability and fault tolerance


## Cloud Foundations and Compute

## Storage, Networking, and Databases

## Deployment, Migration, and AI

## Monitoring, Security, and Pricing

## Exam Preparation

## Resources

