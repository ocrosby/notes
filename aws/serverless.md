# Serverless

## Setup

* Install the AWS CLI
* Install the SAM CLI


Note: The template file describes everything needed ot run the functions in AWS: the API paths to expose, the permissions required, and wht services it depends on.


Connect your machine with the AWS account

> aws configure

Building the project
> cd your-serverless-project
> sam build

Start the development environment

> sam local start-api

Here SAM creates a local HTTP server that hosts all your functions.

Alternatively, you can run

> sam local start-lambda

coupled with

> sam local invoke

This invokes specific serverless functions.  In most cases, you'll need to provide an event payload during the invocation, which you can generate with

> sam local generate-event

Check out the [Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html#serverless-getting-started-hello-world-test-locally)



## References

* [CloudFormation Templates](https://aws.amazon.com/cloudformation/)

