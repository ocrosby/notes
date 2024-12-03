# Messaging

## Overvirew

Microservice messaging can be accomplished using a messaging system.

Examples of Messaging Systems

- Apache Kafka
- Rabbit MQ

## Apache Kafka

- Type: Distributed streaming platform
- Use Case: High-throughput, real-time data streaming, and event sourcing
- Architecture: Distributed, partitioned, and replicated log service
- Message Ordering: Guarantees ordering within a partition
- Persistence: Messages are persisted on disk and replicated
- Scalability: Highly scalable, designed for horizontal scaling
- Protocol: Custom binary protocol over TCP
- Features: High throughput, fault tolerance, stream processing with Kafka Streams

### Kafka Components

- Producer: Publishes messages to topics
- Consumer: Subscribes to topics and processes messages
- Broker: Kafka server that stores messages
- Zookeeper: Manages brokers and maintains metadata
- Topic: Category to which messages are published
- Partition: Logical division of a topic
- Offset: Unique identifier for a message within a partition
- Consumer Group: Group of consumers that share messages
- Replication: Copies of partitions for fault tolerance
- Leader: Broker responsible for handling read/write requests
- Follower: Broker that replicates data from the leader
- Controller: Broker responsible for managing partitions and replicas
- Log: Sequence of messages stored on disk
- Log Segment: File containing messages up to a certain size
- Log Compaction: Retains the latest message for each key
- Retention Policy: Time or size limit for storing messages
- Stream Processing: Real-time processing of data streams
- Kafka Streams: Library for building stream processing applications
- Connect API: Framework for connecting Kafka to external systems
- Connector: Plugin for importing/exporting data to/from Kafka
- MirrorMaker: Tool for replicating data between Kafka clusters
- Schema Registry: Service for storing Avro schemas

## Rabbit MQ

- Type: Message broker
- Use Case: Messaging, routing, and queuing
- Architecture: Centralized message queue with exchanges and queues
- Message Ordering: Supports message ordering within a queue
- Persistence: Messages are persisted on disk
- Scalability: Limited scalability, designed for vertical scaling
- Protocol: AMQP (Advanced Message Queuing Protocol)
- Features: Message routing, delivery acknowledgments, and clustering

## AWS SQS

- Type: Message queue service
- Use Case: Decoupling applications and microservices
- Architecture: Centralized message queue with FIFO and standard queues
- Message Ordering: Supports message ordering within a FIFO queue
- Persistence: Messages are persisted on disk
- Scalability: Highly scalable, designed for horizontal scaling
- Protocol: HTTP/HTTPS
- Features: Message deduplication, delay queues, and dead-letter queues

## AWS SNS

- Type: Message notification service
- Use Case: Pub/sub messaging for push notifications
- Architecture: Centralized message topic with subscribers
- Message Ordering: Does not guarantee message ordering
- Persistence: Messages are not persisted
- Scalability: Highly scalable, designed for horizontal scaling
- Protocol: HTTP/HTTPS, email, SMS, and more
- Features: Message filtering, message attributes, and message delivery status

## Summary

- Apache Kafka is best for high-throughput, real-time data streaming and event sourcing.
- RabbitMQ is suitable for traditional message queuing with complex routing and pub/sub patterns.
- AWS SQS is ideal for decoupling microservices and serverless applications with minimal operational overhead.
- AWS SNS is perfect for broadcasting messages to multiple subscribers and sending notifications.

## References

- [Apache Kafka](https://kafka.apache.org/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [AWS SQS](https://aws.amazon.com/sqs/)

