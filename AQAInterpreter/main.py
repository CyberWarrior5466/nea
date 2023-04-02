from AQAInterpreter.tokens import *
from AQAInterpreter import scanner
from AQAInterpreter import parser
from pprint import pprint
import click
import sys

DEBUG = True


def run(had_error: bool, source: str):
    source += "\n"
    if DEBUG:
        print(source)
    tokens = scanner.scan_tokens(source)
    if DEBUG:
        pprint(tokens)
        print()
    statements = parser.parse(tokens)
    if statements is not None:
        if DEBUG:
            # pprint(statements)
            print(statements)
        for statement in statements:
            if statement is not None:
                statement.interpret()


@click.command()
@click.argument("filename", required=False)
@click.option("-c", "--cmd")
def main(filename, cmd):
    had_error = False
    if filename and cmd:
        raise click.UsageError("cannot specify both filename and cmd")
    
    if filename:
        with open(filename, encoding="utf-8") as infp:
            cmd = infp.read()
    else:
        while True:
            run(had_error, input("> "))

    run(had_error, cmd)
    if had_error:
        exit(65)


if __name__ == "__main__":
    main()