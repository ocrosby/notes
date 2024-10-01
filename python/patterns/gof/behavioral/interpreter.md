# Interpreter

The Interpreter pattern is a design pattern that specifies how to evaluate sentences in a language. The basic idea is to have a class for each symbol (terminal or nonterminal) in a specialized computer language. The syntax tree of a sentence in the language is an instance of the composite pattern and is used to evaluate (interpret) the sentence for a client.

```python
class Context:
    def __init__(self):
        self.input = ""
        self.output = ""

class AbstractExpression:
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        context.output = context.output + "Terminal"

class Nonterminal
```

## Problem

Imagine you have a language that needs to be interpreted. The problem is how to evaluate sentences in the language.

## Solution

The Interpreter pattern suggests creating a class for each symbol in the language. The syntax tree of a sentence in the language is an instance of the composite pattern and is used to evaluate the sentence for a client.

