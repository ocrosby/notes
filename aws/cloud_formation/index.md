# Cloud Formation Templates

AWS CloudFormation is a service that helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like EC2 instances or Amazon RDS DB instances), and CloudFormation takes care of provisioning and configuring those resources for you.

You can utilize the AWS cli to create a stack from a template as follows:

```bash
aws cloudformation create-stack --stack-name myteststack --template-body file://template.yaml
```
