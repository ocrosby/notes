# create-stack

## Overview

The `create-stack` command creates a stack as specified in the template. After the call completes
successfully, the stack creation starts. You can check the status of
the stack through the [DescribeStacks](./describe-stacks.md) operation.


### SYNOPSIS

```text
create-stack
--stack-name <value>
--template-body <value>
[--template-body <value>]
[--template-url <value>]
[--parameters <value>]
[--disable-rollback | --no-disable-rollback]
[--rollback-configuration <value>]
[--timeout-in-minutes <value>]
[--notification-arns <value>]
[--capabilities <value>]
[--resource-types <value>]
[--role-arn <value>]
[--on-failure <value>]
[--stack-policy-body <value>]
[--stack-policy-url <value>]
[--tags <value>]
[--client-request-token <value>]
[--enable-termination-protection | --no-enable-termination-protection]
[--retain-except-on-create | --no-retain-except-on-create]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```


## References

- [Commands Index](../index.md)
