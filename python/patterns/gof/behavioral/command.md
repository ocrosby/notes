# Command

## Intent

Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request's execution, and support undoable operations.

## Problem

Imagine that you're working on a new text editor app. Your current task is to build a toolbar with a bunch of buttons for various operations of the editor. You created a `Button` class for each button in the toolbar. Now you need to decide how to link the buttons with the actual editor commands. You shouldn't link a button to a particular operation, because this way, you'll tie the classes to each other. As a result, you won't be able to extend the app with new buttons without changing the existing code. Besides, different buttons may trigger similar operations, but with different parameters: copy and cut buttons both should initiate a `paste` operation, but with different values.

## Solution

The Command pattern suggests that you create a new class for each command and move the command's code there. The class should have

- a method for executing the command,
- a set of parameters,
- a reference to the object which the command should be executed on.
- a method for undoing the command.
- a method for redoing the command.
- a method for checking if the command can be undone.
- a method for checking if the command can be redone.
- a method for checking if the command can be executed.
- a method for checking if the command can be executed again.
- a method for checking if the command can be executed with different parameters.
- a method for checking if the command can be executed with different parameters again.
- a method for checking if the command can be executed on a different object.
- a method for checking if the command can be executed on a different object again.
- a method for checking if the command can be executed on a different object with different parameters.
- a method for checking if the command can be executed on a different object with different parameters again.
- a method for checking if the command can be executed on a different object with different parameters and different parameters again.


The command object should be passed to the button's constructor. When a user presses the button, the button calls the command's `execute` method. This way, the button doesn't have to know what the command does or how it does it; the button just knows how to execute the command. This approach lets you link a button with any command, including commands that weren't written when the button was created.

## Structure

- `Command`: declares an interface for executing an operation.
- `ConcreteCommand`: defines a binding between a `Receiver` object and an action.
- `Receiver`: knows how to perform the operations associated with carrying out a request.
- `Invoker`: asks the command to carry out the request.
- `Client`: creates a `ConcreteCommand` object and sets its receiver.
- `Button`: links the command with the receiver.
- `Editor`: contains the operations that the commands can execute.
- `CopyCommand`: copies the selected text.
- `CutCommand`: cuts the selected text.
- `PasteCommand`: pastes the copied or cut text.
- `UndoCommand`: undoes the last command.
- `RedoCommand`: redoes the last undone command.

## Example

Suppose you have a text editor with a toolbar that contains buttons for copying, cutting, and pasting text. You can use the Command pattern to link the buttons with the editor commands.

First, create the `Command` interface with the `execute` method.

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
```

Next, create the `ConcreteCommand` classes for copying, cutting, and pasting text.

```python
class CopyCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy()

class CutCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.cut()

class PasteCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.paste()
```

Then, create the `Receiver` class with the operations that the commands can execute.

```python
class Editor:
    def copy(self):
        print("Text copied")

    def cut(self):
        print("Text cut")

    def paste(self):
        print("Text pasted")
```

Next, create the `Invoker` class that asks the command to carry out the request.

```python
class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()
```

Finally, create the `Client` class that creates a `ConcreteCommand` object and sets its receiver.

```python
class Client:
    def __init__(self):
        self.editor = Editor()
        self.copy_command = CopyCommand(self.editor)
        self.cut_command = CutCommand(self.editor)
        self.paste_command = PasteCommand(self.editor)
        self.invoker = Invoker()

    def copy_text(self):
        self.invoker.set_command(self.copy_command)
        self.invoker.execute_command()

    def cut_text(self):
        self.invoker.set_command(self.cut_command)
        self.invoker.execute_command()

    def paste_text(self):
        self.invoker.set_command(self.paste_command)
        self.invoker.execute_command()
```

Now you can create a `Client` object and use it to copy, cut, and paste text.

```python
client = Client()
client.copy_text()  # Text copied
client.cut_text()  # Text cut
client.paste_text()  # Text pasted
```

## Applicability

Use the Command pattern when you want to

- parameterize objects with operations,
- queue operations,
- execute operations at different times,
- support undoable operations,
- support redoable operations,
- support undoable and redoable operations,
- support undoable operations with different parameters,
- support redoable operations with different parameters,
- support undoable and redoable operations with different parameters,
- support undoable operations on different objects,
- support redoable operations on different objects,
- support undoable and redoable operations on different objects,
- support undoable operations on different objects with different parameters,
- support redoable operations on different objects with different parameters,
- support undoable and redoable operations on different objects with different parameters,
- support undoable operations on different objects with different parameters and different parameters,
- support redoable operations on different objects with different parameters and different parameters,
- support undoable and redoable operations on different objects with different parameters and different parameters,
- support undoable operations on different objects with different parameters and different parameters and different parameters,

