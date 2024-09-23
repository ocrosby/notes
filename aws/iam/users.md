# Users

Users are entities that can interact with AWS services. Users can be created, updated, and deleted.

## Creating a User

To create a user, you must have the necessary permissions to create users. The following example shows how to 
create a user using the AWS Management Console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. In the navigation pane, choose **Users**, and then choose **Add user**.
3. Enter a name for the user.
4. Choose the type of access for the user. You can choose **Programmatic access** to allow the user to interact with 
   AWS services programmatically, or you can choose **AWS Management Console access** to allow the user to interact with 
   AWS services using the AWS Management Console.
5. Choose **Next: Permissions**.
6. Choose the permissions policy that defines the permissions for the user. For example, you can choose **AdministratorAccess**
   to grant full access to AWS services.
7. Choose **Next: Tags**.
8. Add tags to the user if needed.
9. Choose **Next: Review**.
10. Review the user details, and then choose **Create user**.

Here's an example of a cloudformation template to create a user:

```yaml
Resources:
  MyUser:
    Type: AWS::IAM::User
    Properties:
      UserName: my-user
```

In this example, the user is created with the name `my-user`.

To create a user using the AWS CLI, you can use the `create-user` command. Here's an example:

```bash
aws iam create-user --user-name my-user
```

In this example, the user is created with the name `my-user`.
