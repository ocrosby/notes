# Roles

A role is an AWS Identity and Access Management (IAM) entity that defines a set of permissions for making AWS service 
requests. Roles are not associated with a specific user or group. Instead, roles are assumed by trusted entities, such 
as users, applications, or AWS services.

## Creating a Role

To create a role, you must have the necessary permissions to create roles. The following example shows how to create a
role using the AWS Management Console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. In the navigation pane, choose **Roles**, and then choose **Create role**.
3. Choose the trusted entity that can assume the role. For example, you can choose **AWS service** to allow an AWS 
   service to assume the role.
4. Choose the permissions policy that defines the permissions for the role. For example, you can choose **AmazonS3FullAccess**
   to grant full access to Amazon S3.
5. Enter a name for the role, and then choose **Create role**.
6. To use the role, you must assume the role. For example, you can assume the role using the AWS Management Console, the
   AWS CLI, or the AWS SDKs.
7. After you assume the role, you can make AWS service requests using the permissions defined in the role.
8. To delete the role, you must first detach any policies attached to the role. Then, you can delete the role.
9. To delete the role, choose the role in the IAM console, and then choose **Delete role**.
10. Confirm that you want to delete the role.

Here's an example of a cloudformation template to create a role:

```yaml
Resources:
  MyRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: MyPolicy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action: s3:*
                Resource: '*'
```

In this example, the role allows an EC2 instance to assume the role and has full access to Amazon S3.

To create a role using the AWS CLI, you can use the `create-role` command. Here's an example:

```bash
aws iam create-role --role-name MyRole --assume-role-policy-document file://trust-policy.json
```

In this example, the `trust-policy.json` file contains the trust policy document that defines the trusted entity that

The trust policy JSON file should look something like this:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

The `create-role` command creates a role named `MyRole` that allows an EC2 instance to assume the role.

## Deleting a Role

To delete a role, you must first detach any policies attached to the role. Then, you can delete the role. 

Here's an example of detatching the previously created policy:

```bash
aws iam detach-role-policy --role-name MyRole --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```

Here's an example of how to delete a role using the AWS CLI:

```bash
aws iam delete-role --role-name MyRole
```
