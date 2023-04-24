- add a section explaining grade A algorithms used
  - Expr and Stmt interface inherit .interpret() method which is defined for multiple classes (polymorphism)
  - file handling used in main.py
  - pattern matching used in scanner.py via * wildcard

- explain using @dataclass and python's match statement to remove redundant code

**using dataclass**
```python
from dataclasses import dataclass
from typing import any

class ExampleClass:
    def __init__(attribute: Any) -> None:
        self.attribute = attribute

    def method(self):
        ...

    def __str__():
        return f"ExampleClass({self.attribute_1}, {self.attribute_2})"


@dataclass
class ExampleDataClass:
    attribute: Any

    def method(self):
        ...
```

**using match**
```python
```


- maybe move unit tests to design section, include the word unit tests in report.md
- pyproject.toml is used to upload the project to pypi
- add in the code dump that the code is also available in a github repo 'The code for this project is avalable in this document as well as in a github repo on github @ https://github.com/CyberWarrior5466/nea and '



