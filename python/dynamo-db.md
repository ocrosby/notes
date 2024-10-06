# DynamoDB

DynamoDB is a fully managed NoSQL database service provided by AWS. It is a key-value and document database that delivers single-digit millisecond performance at any scale. It is a fully managed, multi-region, multi-active, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications.

For the purposes of this demo

create a table named demo-dynamo-python in the AWS console

- **table_name**: demo-dynamo-python
- **partition_key**: customer_id (String)
- **sort_key**: order_id (String)


The following code snippet creates a table named `demo-dynamo-python` with a partition key `customer_id` and a sort key `order_id`.

```python
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='demo-dynamo-python',
    KeySchema=[
        {
            'AttributeName': 'customer_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'order_id',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'customer_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'order_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='demo-dynamo-python')

print(table.item_count)
```


Create a virtual environment and install the boto3 package

```bash
python3 -m venv .venv
source venv/bin/activate
pip install boto3
```

The following code requires you to configure your AWS credentials using the `aws configure` command 
or by setting the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

```python
import boto3
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime

class DynamoDBTable:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def create_item(self, customer_id, order_id, **attributes):
        item = {
            'customer_id': customer_id,
            'order_id': order_id,
            'status': 'pending',
            'created_at': datetime.now().isoformat(),
            **attributes
        }
        response = self.table.put_item(Item=item)
        print(f'Insert response: {response}')
        
    def get_item(self, customer_id, order_id):
        response = self.table.get_item(
            Key={
                'customer_id': customer_id,
                'order_id': order_id
            }
        )
        print(f'Get response: {response}')
        return response.get('Item')

    def update_item(self, customer_id, order_id, **attributes):
        update_expression = "SET " + ", ".join(f"{k} = :{k}" for k in attributes.keys())
        expression_attribute_values = {f":{k}": v for k, v in attributes.items()}
        
        self.table.update_item(
            Key={
                'customer_id': customer_id,
                'order_id': order_id
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

    def delete_item(self, customer_id, order_id):
        self.table.delete_item(
            Key={
                'customer_id': customer_id,
                'order_id': order_id
            }
        )

    def query_items(self, customer_id):
        response = self.table.query(
            KeyConditionExpression=Key('customer_id').eq(customer_id)
        )
        return response.get('Items')

# Example usage:
# table = DynamoDBTable('demo-dynamo-python')
# table.create_item('cust123', 'order456', attribute1='value1', attribute2='value2')
# item = table.get_item('cust123', 'order456')
# table.update_item('cust123', 'order456', attribute1='new_value')
# table.delete_item('cust123', 'order456')
# items = table.query_items('cust123')
```