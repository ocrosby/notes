# Groups

Groups are collections of users. Groups can be created, updated, and deleted.

## Creating a Group

To create a group, you must have the necessary permissions to create groups. The following example shows how to 
create a group using the AWS Management Console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. In the navigation pane, choose **Groups**, and then choose **Create group**.
3. Enter a name for the group.
4. Choose **Next: Permissions**.
5. Choose the permissions policy that defines the permissions for the group. For example, you can choose **AmazonS3FullAccess**
   to grant full access to Amazon S3.
6. Choose **Next: Tags**.
7. Add tags to the group if needed.
8. Choose **Next: Review**.
9. Review the group details, and then choose **Create group**.

Here's an example of a cloudformation template to create a group:

```yaml
Resources:
  MyGroup:
    Type: AWS::IAM::Group
    Properties:
      GroupName: my-group
```

In this example, the group is created with the name `my-group`.

To create a group using the AWS CLI, you can use the `create-group` command. Here's an example:

```bash
aws iam create-group --group-name my-group
```

In this example, the group is created with the name `my-group`.


## Add Users to a Group

To add users to a group, you must have the necessary permissions to add users to groups. The following example shows how to
add users to a group using the AWS Management Console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. In the navigation pane, choose **Groups**.
3. Select the group that you want to add users to.
4. Choose the **Users** tab.
5. Choose **Add users to group**.
6. Select the users to add to the group.
7. Choose **Add users**.

Here's an example of a cloudformation template to add a user to a group:

```yaml
Resources:
  MyUser:
    Type: AWS::IAM::User
    Properties:
      UserName: my-user

  MyGroup:
    Type: AWS::IAM::Group
    Properties:
      GroupName: my-group

  MyUserGroupMembership:
    Type: AWS::IAM::UserToGroupAddition
    Properties:
      GroupName: my-group
      Users:
        - !Ref MyUser
```

In this example, the user `my-user` is added to the group `my-group`.

## Removing Users from a Group

To remove users from a group, you must have the necessary permissions to remove users from groups. The following example
shows how to remove users from a group using the AWS Management Console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. In the navigation pane, choose **Groups**.
3. Select the group that you want to remove users from.
4. Choose the **Users** tab.
5. Select the users to remove from the group.
6. Choose **Remove users from group**.
7. Confirm that you want to remove the users from the group.


In this example, the user `my-user` is removed from the group `my-group`.

To remove a user from a group using the AWS CLI, you can use the `remove-user-from-group` command. Here's an example:

```bash
aws iam remove-user-from-group --group-name my-group --user-name my-user
```

In this example, the user `my-user` is removed from the group `my-group`.


## Deleting a Group

To delete a group, you must first remove any users from the group. Then, you can delete the group. The following 
example shows how to delete a group using the AWS Management Console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. In the navigation pane, choose **Groups**.
3. Select the group that you want to delete.
4. Choose **Actions**, and then choose **Delete group**.
5. Confirm that you want to delete the group.
6. To delete the group, choose the group in the IAM console, and then choose **Delete group**.
7. Confirm that you want to delete the group.
