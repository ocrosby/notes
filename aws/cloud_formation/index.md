# Cloud Formation Templates

## Overview

AWS CloudFormation is a service that helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like EC2 instances or Amazon RDS DB instances), and CloudFormation takes care of provisioning and configuring those resources for you.


With CloudFormation, you declare all your resources and dependencies in a template file. The template
defines a collection of resources as a single unit called a **stack**.  Cloudformation creates and deletes
all member resources of the stack together and manages all dependencies between the resources for you.

Stack
: A stack is a collection of AWS resources that you can manage as a single unit. 

> **Note:** In other words, you can create, update, or delete a collection of resources by creating, updating, or deleting stacks.

## Using the CLI

Display the AWS cloudformation help menu:

```bash
aws cloudformation help
```

### AWS CLI cloudformation Commands

- [activate-organizations-access](./commands/activate-organizations-access.md)
- [activate-type](./commands/activate-type.md)
- [batch-describe-type-configurations](./commands/batch-describe-type-configurations.md)
- [cancel-update-stack](./commands/cancel-update-stack.md)
- [continue-update-rollback](./commands/continue-update-rollback.md)
- [create-change-set](./commands/create-change-set.md)
- [create-generated-template](./commands/create-generated-template.md)
- [create-stack](./commands/create-stack.md)
- [create-stack-instances](./commands/create-stack-instances.md)
- [create-stack-set](./commands/create-stack-set.md)
- [deactivate-organizations-access](./commands/deactivate-organizations-access.md)
- [deactivate-type](./commands/deactivate-type.md)
- [delete-change-set](./commands/delete-change-set.md)
- [delete-generated-template](./commands/delete-generated-template.md)
- [delete-stack](./commands/delete-stack.md)
- [delete-stack-instances](./commands/delete-stack-instances.md)
- [delete-stack-set](./commands/delete-stack-set.md)
- [deploy](./commands/deploy.md)
- [deregister-type](./commands/deregister-type.md)
- [describe-account-limit](./commands/describe-account-limit.md)
- [describe-change-set](./commands/describe-change-set.md)
- [describe-change-set-hooks](./commands/describe-change-set-hooks.md)
- [describe-generated-template](./commands/describe-generated-template.md)
- [describe-organizations-access](./commands/describe-organizations-access.md)
- [describe-publisher](./commands/describe-publisher.md)
- [describe-resource-scan](./commands/describe-resource-scan.md)
- [describe-stack-drift-detection-status](./commands/describe-stack-drift-detection-status.md)
- [describe-stack-events](./commands/describe-stack-events.md)
- [describe-stack-instance](./commands/describe-stack-instance.md)
- [describe-stack-resource](./commands/describe-stack-resource.md)
- [describe-stack-resource-drifts](./commands/describe-stack-resource-drifts.md)
- [describe-stack-resources](./commands/describe-stack-resources.md)
- [describe-stack-set](./commands/describe-stack-set.md)
- [describe-stack-set-operation](./commands/describe-stack-set-operation.md)
- [describe-stacks](./commands/describe-stacks.md)
- [describe-type](./commands/describe-type.md)
- [describe-type-registration](./commands/describe-type-registration.md)
- [detect-stack-drift](./commands/detect-stack-drift.md)
- [detect-stack-set-drift](./commands/detect-stack-set-drift.md)
- [estimate-template-cost](./commands/estimate-template-cost.md)
- [execute-change-set](./commands/execute-change-set.md)
- [get-generated-template](./commands/get-generated-template.md)
- [get-stack-policy](./commands/get-stack-policy.md)
- [get-template-summary](./commands/get-template-summary.md)
- [import-stacks-to-stack-set](./commands/import-stacks-to-stack-set.md)
- [list-change-sets](./commands/list-change-sets.md)
- [list-exports](./commands/list-exports.md)
- [list-generated-templates](./commands/list-generated-templates.md)
- [list-imports](./commands/list-imports.md)
- [list-resource-scan-related-resources](./commands/list-resource-scan-related-resources.md)
- [list-resource-scans](./commands/list-resource-scans.md)
- [list-stack-instance-resource-drifts](./commands/list-stack-instance-resource-drifts.md)
- [list-stack-instances](./commands/list-stack-instances.md)
- [list-stack-resources](./commands/list-stack-resources.md)
- [list-stack-set-auto-deployment-targets](./commands/list-stack-set-auto-deployment-targets.md)
- [list-stack-set-operation-results](./commands/list-stack-set-operation-results.md)
- [list-stack-set-operations](./commands/list-stack-set-operations.md)
- [list-stack-sets](./commands/list-stack-sets.md)
- [list-stacks](./commands/list-stacks.md)
- [list-type-registrations](./commands/list-type-registrations.md)
- [list-type-versions](./commands/list-type-versions.md)
- [list-types](./commands/list-types.md)
- [package](./commands/package.md)
- [publish-type](./commands/publish-type.md)
- [record-handler-progress](./commands/record-handler-progress.md)
- [register-publisher](./commands/register-publisher.md)
- [register-type](./commands/register-type.md)
- [rollback-stack](./commands/rollback-stack.md)
- [set-stack-policy](./commands/set-stack-policy.md)
- [set-type-configuration](./commands/set-type-configuration.md)
- [set-type-default-version](./commands/set-type-default-version.md)
- [signal-resource](./commands/signal-resource.md)
- [start-resource-scan](./commands/start-resource-scan.md)
- [stop-stack-set-operation](./commands/stop-stack-set-operation.md)
- [test-type](./commands/test-type.md)
- [update-generated-template](./commands/update-generated-template.md)
- [update-stack](./commands/update-stack.md)
- [update-stack-instances](./commands/update-stack-instances.md)
- [update-stack-set](./commands/update-stack-set.md)
- [update-termination-protection](./commands/update-termination-protection.md)
- [validate-template](./commands/validate-template.md)
- [wait](./commands/wait.md)

 
## References

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
- [AWS CloudFormation User Guide](https://s3.cn-north-1.amazonaws.com.cn/aws-dam-prod/china/pdf/cfn-ug.pdf)

