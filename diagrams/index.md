# Diagrams

## Tools

- Mermaid
- PlantUML
- HackerDraw


What is important to me?

- Easy to use
- Easy to read
- Easy to maintain
- Must integrate easily with Markdown on GitHub
- Must be able to generate diagrams from code



Diagrams is a python package that allow you to create diagrams as code.

It was inspired by the original [diagrams](

Diagrams lets you draw the cloud system architecture in Python code.

It was born for prototyping a new system architecture without any design tools. You can also describe or visualize the existing system architecture as well.

Diagrams currently supports six major providers: AWS, Azure, GCP, Kubernetes, Alibaba Cloud and Oracle Cloud. It now also supports On-Premise nodes.

NOTE: It does not control any actual cloud resources nor does it generate cloud formation or terraform code. It is just for drawing the cloud system architecture diagrams.

## Installation

```bash
pip install diagrams
```

## Getting Started

Here is a simple example:

```python
from diagrams import Diagram

with Diagram("Simple Diagram"):
    pass
```

- [Simple Diagram](https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/simple-diagram.png)
