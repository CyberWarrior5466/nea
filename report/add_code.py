"""adds tree and code for technical solution in `report.md` from disk"""

from pathlib import Path
import subprocess
import sys

files_list = (
    (".gitignore", "text"),
    ("LICENSE", "text"),
    ("pyproject.toml", "toml"),
    ("AQAInterpreter/__init__.py", "python"),
    ("AQAInterpreter/main.py", "python"),
    ("AQAInterpreter/errors.py", "python"),
    ("AQAInterpreter/tokens.py", "python"),
    ("AQAInterpreter/scanner.py", "python"),
    ("AQAInterpreter/environment.py", "python"),
    ("AQAInterpreter/parser.py", "python"),
    ("AQAInterpreter/interpreter.py", "python"),
)

tests_list = (("AQAInterpreter/test_.py", "python"),)


files_out = (
    "```\n"
    + subprocess.run(
        f"tree --prune -P '{'|'.join(Path(row[0]).name for row in files_list)}'",
        shell=True,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.rstrip()
    + "\n```"
)
tests_out = ""

TEMPLATE = """
## {}
``` {{.{} .numberLines}}
{}
```
"""


for file, file_ext in files_list:
    files_out += TEMPLATE.format(file, file_ext, Path(file).read_text(encoding="utf-8"))

for file, file_ext in tests_list:
    tests_out += TEMPLATE.format(file, file_ext, Path(file).read_text(encoding="utf-8"))

file_path = Path(sys.argv[1])

content = file_path.read_text(encoding="utf-8")
content = content.replace("\\TECHNICAL_SOLUTION", files_out)
content = content.replace("\\TESTS", tests_out)

if len(sys.argv) == 3:
    for char in ("│", "╭", "─", "├", "└", "∕", "≠", "≤", "≥"):
        content = content.replace(char, "")

file_path.write_text(content, encoding="utf-8")
