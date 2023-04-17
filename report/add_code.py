lst = (
    (".gitignore", ""),
    ("LICENSE", ""),
    ("pyproject.toml", "toml"),
    ("README.md", "markdown"),
    ("AQAInterpreter/__init__.py", "python"),
    ("AQAInterpreter/main.py", "python"),
    ("AQAInterpreter/errors.py", "python"),
    ("AQAInterpreter/tokens.py", "python"),
    ("AQAInterpreter/scanner.py", "python"),
    ("AQAInterpreter/environment.py", "python"),
    ("AQAInterpreter/parser.py", "python"),
    ("AQAInterpreter/interpreter.py", "python"),
    ("AQAInterpreter/test_.py", "python"),
)

out = ""
template = """
## {}
```{}
{}
```
"""

for file, file_ext in lst:
    out += template.format(file, open(file, encoding="utf-8").read())

print(out)
