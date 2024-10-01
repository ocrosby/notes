# Chain of Responsibility

The Chain of Responsibility pattern is a behavioral design pattern that allows an object to pass a request along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it along the chain.

## Problem

Imagine you have a set of handlers that need to process requests. The handlers are organized in a chain, and the request is passed along the chain until a handler processes it. The problem is how to avoid coupling the sender of a request to its receiver.

## Solution

The Chain of Responsibility pattern suggests creating a chain of handler objects. Each handler has a successor, and the request is passed along the chain until a handler processes it. The sender of the request is decoupled from its receiver, and the handlers can be added or removed without affecting the sender.

## Structure

- `Handler`: defines an interface for handling requests.
- `ConcreteHandler`: handles requests it is responsible for; it can access its successor.
- `Client`: sends requests to the first handler in the chain.
- `Request`: represents a request to be processed.
- `Response`: represents a response to a request.
- `Middleware`: abstract class that implements the handler interface.
- `ConcreteMiddleware`: concrete class that extends the middleware class.
- `Server`: processes requests using a chain of middleware objects.
- `Application`: sends requests to the server to be processed.
- `Logger`: logs the request and response.
- `Authenticator`: authenticates the request.
- `Throttler`: limits the number of requests.
- `Router`: routes the request to the appropriate handler.
- `HandlerChain`: chains the handlers together.
