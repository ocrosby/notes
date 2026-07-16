# Event-Driven Architecture

A definitional reference for event-driven architecture (EDA): what it is, what it is not, the vocabulary the field uses, and the trade-offs the paradigm accepts. This document is intentionally scoped to *definitions and concepts*. Implementation guides, broker comparisons, and pattern walkthroughs live in sibling documents (see [Related notes](#related-notes)).

---

## Table of contents

- [Definition](#definition)
- [What is an event?](#what-is-an-event)
- [Why event-driven?](#why-event-driven)
- [EDA vs. request-driven architecture](#eda-vs-request-driven-architecture)
- [Core principles](#core-principles)
- [Core components](#core-components)
- [The three EDA patterns](#the-three-eda-patterns)
- [Delivery guarantees](#delivery-guarantees)
- [Ordering and partitioning](#ordering-and-partitioning)
- [Idempotency and duplicate handling](#idempotency-and-duplicate-handling)
- [When to use EDA](#when-to-use-eda)
- [When not to use EDA](#when-not-to-use-eda)
- [Trade-offs](#trade-offs)
- [Glossary](#glossary)
- [Related notes](#related-notes)

---

## Definition

**Event-driven architecture (EDA)** is a software architecture paradigm in which the flow of control between components is driven by the production, detection, and consumption of *events* — discrete, immutable records that describe something that has already happened in the system.

In an event-driven system, components communicate by emitting facts about their own state changes rather than by invoking each other directly. Other components observe those facts and react. The producer of an event does not know — and does not need to know — which components will consume it, when they will consume it, or what they will do in response.

This produces a system whose components are **loosely coupled in time, space, and identity**:

- **Time decoupling** — producer and consumer do not need to be active simultaneously.
- **Space decoupling** — producer and consumer do not need to know each other's network location.
- **Identity decoupling** — producer and consumer do not need to know each other's identity or existence.

EDA is a *paradigm*, not a product. It can be implemented on top of many different transports (message queues, event streams, event stores, in-process pub/sub, webhooks), and a single system may use several of them at once.

## What is an event?

An **event** is an immutable record of a state change that has already occurred. Two properties are essential:

1. **Past tense.** An event describes something that *has happened*, not something that should happen. `OrderPlaced` is an event; `PlaceOrder` is a command. Confusing the two collapses the distinction between "reacting to reality" and "requesting an action," which is the distinction EDA exists to preserve.
2. **Immutable.** Once emitted, an event is a historical fact. It is never edited or deleted. If the fact was wrong, a *new* event corrects it (`OrderCancelled`, `PriceCorrected`); the original event remains.

Beyond these two properties, an event typically carries:

| Element | Purpose |
|---|---|
| **Type / name** | Identifies the kind of event (e.g. `PaymentReceived`, `UserRegistered`). Consumers dispatch on this. |
| **Identifier** | A unique ID for this specific event instance — required for idempotent processing. |
| **Timestamp** | When the state change occurred, not when it was published. |
| **Subject / aggregate ID** | The entity the event is about (e.g. `order_id`, `user_id`). |
| **Payload** | The data that describes the change. Size depends on the pattern (see [The three EDA patterns](#the-three-eda-patterns)). |
| **Metadata** | Correlation IDs, causation IDs, schema version, source service, trace context. |

An event is *not*:

- A command (imperative, expects action, may be rejected)
- A query (asks for information, expects a response)
- A message in general (message is the transport-layer term; event is a semantic subtype)

## Why event-driven?

Systems adopt EDA to solve a specific class of problem: **components need to react to state changes in other components, and the set of interested reactors changes over time.**

Direct request/response coupling forces the producer of a state change to know every consumer. Adding a new consumer requires modifying the producer. Removing one requires the same. This coupling scales badly across teams, services, and years.

Event-driven communication inverts this: the producer emits a fact and forgets it. New consumers can be added without touching the producer. Existing consumers can be removed, replaced, or reimplemented without notifying anyone upstream. The producer's contract is the *event schema*, not a list of downstream callers.

The trade the paradigm accepts, in exchange, is that the system's runtime behavior is no longer visible in any single call graph. See [Trade-offs](#trade-offs).

## EDA vs. request-driven architecture

| Dimension | Request-driven | Event-driven |
|---|---|---|
| **Direction of knowledge** | Caller knows callee | Producer does not know consumer |
| **Communication mode** | Synchronous request/response (usually) | Asynchronous publish/consume |
| **Coupling** | Tight — signature changes ripple | Loose — schema changes ripple |
| **Failure model** | Caller sees callee's failure | Consumer failures are invisible to producer |
| **Reasoning** | Trace a call stack | Trace a causal chain across time |
| **Adding a new participant** | Modify the caller | Subscribe to the topic |
| **Testing** | Mock the callee | Assert the event was emitted |
| **Latency profile** | Bounded by slowest hop | Bounded by broker + consumer lag |

Neither is universally better. Request-driven systems are easier to reason about at a single point in time; event-driven systems are easier to evolve across many points in time.

## Core principles

1. **Events are facts, not requests.** A consumer may choose to ignore an event; a producer may not demand a specific reaction.
2. **Producers do not depend on consumers.** The set of consumers can change freely without producer awareness.
3. **Communicate state changes, not internal state.** Publish the delta or the resulting fact, not a snapshot of a private data structure.
4. **Design for at-least-once delivery.** Assume every event may be delivered more than once. Consumers must be idempotent (see [Idempotency and duplicate handling](#idempotency-and-duplicate-handling)).
5. **Schema is the contract.** The event schema is the interface between producer and consumer. Treat it with the same versioning discipline as a public API.
6. **Order is a resource, not a given.** Global ordering across a distributed system is expensive; scope ordering to a partition key (see [Ordering and partitioning](#ordering-and-partitioning)).

## Core components

Every event-driven system, regardless of transport, is built from four roles. The same physical component can play more than one role.

### Event

The unit of communication. See [What is an event?](#what-is-an-event).

### Producer

The component that detects a state change and emits an event describing it. A producer:

- Publishes to a channel (topic, queue, stream) without knowing the consumers
- Owns the event schema for the events it produces
- Is responsible for exactly-once *production* (typically via transactional outbox or idempotent publish)

### Consumer

The component that subscribes to a channel and reacts to events. A consumer:

- May be one of many independent subscribers to the same channel
- May be part of a *consumer group* that shares the load of a channel among group members
- Must handle duplicate delivery, out-of-order delivery within its scope, and its own failures
- Owns its offset / cursor / acknowledgment state

### Channel

The transport that carries events from producers to consumers. Channels come in three broad shapes, distinguished by *retention* and *addressing*:

| Shape | Retention | Consumers see | Example |
|---|---|---|---|
| **Message queue** | Events discarded after acknowledgment | Each event once (per queue) | RabbitMQ, SQS, ActiveMQ |
| **Event stream** | Events retained for a configured window; replayable | Any event at any offset within the window | Kafka, Kinesis, Pulsar, Redpanda |
| **Event store** | Events retained forever, indexed by stream / aggregate | The full history of an aggregate | EventStoreDB, Marten, Axon Server |

The term "channel" is the abstract concept. In practice you will see *topic*, *queue*, *stream*, *subject*, *exchange*, *partition*, and *log* used with overlapping meanings depending on the vendor.

## The three EDA patterns

EDA is not a single technique. It is an umbrella over three distinct patterns that solve different problems. A single system commonly uses more than one. See [`patterns.md`](./patterns.md) for the deep dive; the summaries below are the shortest useful version.

### Event notification

The producer emits a minimal event announcing that *something happened*. The event carries only an identifier and enough metadata for interested consumers to fetch the details themselves (typically via a REST call back to the producer or a shared store).

- **Payload**: minimal — often just an ID and a timestamp
- **Coupling**: consumers still depend on the producer's read API to hydrate the event
- **Best for**: notifying that something occurred when most consumers do not need the full detail
- **Watch out for**: chatty callbacks, the producer becoming a lookup bottleneck, coupling reappearing at the query layer

### Event-carried state transfer (ECST)

The producer emits an event containing all the state a consumer needs to act. Consumers do not call back to the producer; they build local materialized views from the events they receive.

- **Payload**: complete — the event carries the relevant state
- **Coupling**: minimal at runtime — consumers can operate even if the producer is offline
- **Best for**: reducing runtime coupling, enabling consumers to serve their own reads, enabling different consumer technology choices
- **Watch out for**: larger payloads, duplicated data across services, eventual consistency between the producer's view and the consumer's view

### Event sourcing

The producer stores every state change as an event in an append-only *event store*. The current state of any entity is derived by replaying its event stream from the beginning (or from the latest snapshot). Events here are the *system of record*, not a communication mechanism.

- **Payload**: complete and history-preserving — the events *are* the data
- **Coupling**: internal to a single service — event sourcing is an internal persistence pattern, not primarily an integration pattern
- **Best for**: audit-critical domains, systems that need to answer "what did we know when," systems that benefit from temporal queries, CQRS read models
- **Watch out for**: schema evolution across historical events, snapshotting for performance, GDPR / right-to-be-forgotten conflicts, upfront complexity that rarely pays back on simple CRUD

These three are frequently confused because all three involve emitting events. The distinction is *what the events are for*: notification (announce), ECST (integrate), event sourcing (persist).

## Delivery guarantees

Every event transport makes one of three guarantees. There is no free lunch — each has a specific failure mode.

| Guarantee | Meaning | Failure mode |
|---|---|---|
| **At-most-once** | Every event is delivered zero or one times | Events can be lost |
| **At-least-once** | Every event is delivered one or more times | Events can be duplicated |
| **Exactly-once** | Every event is delivered exactly once — end to end | Only achievable with strong constraints (idempotent consumers, transactional writes, or single-partition scope); often "effectively exactly-once" in marketing terms |

Most production event systems provide *at-least-once* delivery and require the consumer to achieve *effectively exactly-once* processing through idempotency.

## Ordering and partitioning

Ordering across independent producers is not naturally defined. Even within one channel, most brokers guarantee order only within a *partition* — a sub-stream of the channel keyed by some attribute of the event.

A well-chosen **partition key** groups events that must be processed in order onto the same partition. Common choices: aggregate ID, user ID, tenant ID. Events with the same key go to the same partition; events with different keys may be processed in parallel and may arrive at consumers in any order.

Global ordering is possible (single partition, single consumer) but sacrifices throughput. Most systems accept per-key ordering as the correct trade.

## Idempotency and duplicate handling

Because most transports deliver at-least-once, consumers must produce the same result whether they process a given event once or ten times. This is *idempotency*.

Common techniques:

- **Idempotency key** — record the processed event's ID; skip if already seen
- **Conditional writes** — use the event's `version` or `timestamp` in a `WHERE` clause so a second attempt is a no-op
- **Natural idempotency** — express the effect as `SET x = value` rather than `x += 1`
- **Transactional outbox on the consumer side** — atomically write the side effect and the "processed" marker

An event-driven system whose consumers are not idempotent is not correct; it is only *usually* correct.

## When to use EDA

EDA earns its complexity in systems where:

- **Multiple independent consumers** need to react to the same state changes, and the set of consumers changes over time
- **Producers and consumers should evolve independently**, on different release cycles, owned by different teams
- **Workloads are naturally asynchronous** — the producer does not need a synchronous answer to continue
- **Load smoothing** matters — the broker absorbs bursts that would overwhelm synchronous callees
- **Auditability** or **temporal reasoning** is a first-class requirement (event sourcing specifically)
- **Cross-service reactions** must survive partial failures — the event outlives the producer's crash

## When not to use EDA

EDA is the wrong answer when:

- **The interaction is inherently synchronous** — the caller cannot proceed without a specific response (queries, transactions with immediate user feedback)
- **There is exactly one consumer, forever** — a direct call is simpler and more debuggable
- **The domain has no meaningful events** — CRUD over a single table with no reactors gains nothing from a broker
- **The team lacks the operational maturity** to run a broker, monitor consumer lag, handle poison messages, and evolve schemas — EDA moves complexity from code to infrastructure and process
- **Strong consistency is required across the resulting state** — EDA is fundamentally eventually consistent

## Trade-offs

What you gain:

- Loose coupling; independent evolution of services
- Natural load smoothing and back-pressure absorption
- New consumers can be added without touching producers
- Failure isolation — one consumer's outage does not stop others
- Auditability, especially with event sourcing
- Temporal replay: reconstruct past state, backfill new consumers

What you give up:

- Ease of end-to-end reasoning — no single stack trace shows the full effect of an action
- Strong consistency — the system is eventually consistent by construction
- Simplicity of debugging — root-cause investigations cross services, time, and broker state
- Trivial testing — integration tests must consider ordering, duplicates, and consumer lag
- Straightforward schema changes — the schema is a contract between producers and *every current and historical consumer*
- Low operational overhead — brokers, schema registries, dead-letter queues, and lag monitoring are non-negotiable

The paradigm is a lever, not a virtue. Apply it where the trade is worth it; keep request/response where it is not.

## Glossary

- **Aggregate** — a cluster of domain objects treated as a single unit for the purpose of data changes. Events are typically scoped to an aggregate.
- **At-least-once / at-most-once / exactly-once** — see [Delivery guarantees](#delivery-guarantees).
- **Broker** — the server or cluster that hosts channels and routes events (RabbitMQ, Kafka, NATS).
- **Choreography** — a coordination style in which services react to each other's events with no central coordinator. Contrast with *orchestration*.
- **Command** — a request for a state change to occur. Distinguished from an event, which is a record that a state change *has* occurred.
- **Consumer group** — a set of consumers that share the load of a channel; each event is delivered to exactly one member of the group.
- **Correlation ID** — a metadata value shared across all events causally related to the same originating request. Enables distributed tracing.
- **CQRS** — Command Query Responsibility Segregation. A pattern that separates the model used to write data from the model used to read it. Frequently paired with event sourcing.
- **Dead-letter queue (DLQ)** — a channel that receives events a consumer has repeatedly failed to process, so they do not block the main channel.
- **Event** — see [What is an event?](#what-is-an-event).
- **Event store** — see [Core components](#core-components).
- **Event stream** — see [Core components](#core-components).
- **Idempotency** — see [Idempotency and duplicate handling](#idempotency-and-duplicate-handling).
- **Message queue** — see [Core components](#core-components).
- **Offset / cursor** — the consumer's position within a stream; determines what it will read next.
- **Orchestration** — a coordination style in which a central component directs the flow across services. Contrast with *choreography*.
- **Partition** — a sub-stream of a channel; the unit within which most brokers guarantee ordering.
- **Poison message** — an event that repeatedly causes consumer failure; typically routed to a DLQ.
- **Projection** — a read model derived by processing events, kept up to date as new events arrive.
- **Pub/sub** — publish-subscribe; a messaging style where publishers emit to a channel and any subscriber to that channel receives a copy.
- **Replay** — re-processing events from a past offset, usually to rebuild a projection or seed a new consumer.
- **Saga** — a long-running, multi-step transaction implemented as a sequence of events and compensating actions.
- **Schema registry** — a service that stores and versions event schemas so producers and consumers can agree on structure.
- **Snapshot** — a materialized current state of an aggregate, stored to avoid replaying its entire event history on every read (an optimization for event sourcing).
- **Subject** — the entity an event is about; alternately, the NATS term for a topic-like address.
- **Topic** — a named channel; the primary addressing unit in Kafka, Pulsar, and similar systems.
- **Transactional outbox** — a pattern in which a producer writes the event and the state change to the same database transaction, and a separate process ships events from the outbox table to the broker. Prevents the "wrote to DB but crashed before publishing" failure.

## Related notes

- [`patterns.md`](./patterns.md) — deep dive on notification, event-carried state transfer, and event sourcing, with flow diagrams and failure modes
- [`_index.md`](./_index.md) — the Hugo landing page for this section, with worked examples in Go and mermaid diagrams
- [`kafka/`](./kafka/) — notes on Apache Kafka as an event streaming implementation
- [`../messaging/`](../messaging/) — sibling notes on messaging concepts more broadly
