from AQAInterpreter import main
from AQAInterpreter.tokens import *
from AQAInterpreter import errors

@dataclass
class Scanner:
    source: str
    _start: int = 0
    _current: int = 0
    _line: int = 1
    _tokens: list[Token] = []

    def _at_end(self) -> bool:
        return self._current >= len(self.source)

    def _add(self, token_type: str, literal: str | None = None) -> None:
        self._tokens.append(Token(token_type, literal=literal, lexeme=self.source[self._start:self._current], line=self._line))

    def _match(self, char: str) -> bool:
        if self._at_end() or self.source[self._current] != char:
            return False
        self._current += 1
        return True

    def _peek(self) -> str:
        """looks ahead 1 character"""
        if self._at_end():
            return "\0"
        return self.source[self._current]

    def _peek_next(self) -> str:
        """looks ahead 2 character"""
        if self._current + 1 >= len(self.source):
            return "\0"
        return self.source[self._current + 1]

    def _advance(self) -> str:
        self._current += 1
        return self.source[self._current - 1]
    
    def _scan_token(self):
        match list(self.source):
            case ["(", *_]: print("(")
            case [")", *_]: print(")")
            case ["-", *_]: print("-")
            case ["+", *_]: print("+")
            case ["*", *_]: print("*")
            case ["×", *_]: print("×")
            case ["/", *_]: print("/")
            case ["÷", *_]: print("÷")
            case ["=", *_]: print("=")
            case ["≠", *_]: print("≠")
            case ["≤", *_]: print("≤")
            case ["≥", *_]: print("≥")
            case [":", *_]: print(":")

            case ["!", "=", *_]:
                print("!=")
            case ["<", "-", *_]:
                print("<-")
            case ["<", "=", *_]:
                print("<=")
            case ["<", *_]:
                print("<")
            case [">", "=", *_]:
                print(">=")
            case [">", *_]:
                print(">")
            case ["#", *_]:
                while self._peek() != "\n" and not self._at_end():
                    self._advance()

            case ['"', *_]:
                while self._peek() != '"' and not self._at_end():
                    if self._peek() == "\n":
                        errors.error(self._line, "unterminated string")
                    self._advance()

                    if self._at_end():
                        errors.error(self._line, "unterminated string")

                    # the closing `"`
                    self._advance()
                    self._add(STRING, self. source[self._start + 1 : self._current - 1])

            case ["'", *_]: pass

            case ["\n", *_]:
                print("\n")
                self._line += 1

            case [" ", *_] | ["\r", *_] | ["\t", *_]: return

            case _: pass

        if False: pass
        elif character == '"':
            while peek() != '"' and not at_end():
                if peek() == "\n":
                    errors.error(line, "unterminated string")
                advance()

            if at_end():
                errors.error(line, "unterminated string")

            # the closing `"`
            advance()
            add(STRING, source[start + 1 : current - 1])

        elif character == "'":
            while peek() != "'" and not at_end():
                if peek() == "\n":
                    errors.error(line, "unterminated string")
                advance()

            if at_end():
                errors.error(line, "unterminated string")

            # the closing `'`
            advance()
            add(STRING, source[start + 1 : current - 1])

        elif character in {" ", "\r", "\t"}:
            return current, line, tokens
        else:
            # variable
            if character.isdigit():
                while peek().isdigit(): advance()

                if peek() == "." and peek_next().isdigit():
                    # consume the '.'
                    advance()

                    while peek().isdigit(): advance()
                add(NUMBER, source[start:current])

            elif character.isalpha() or character == "_":
                while peek().isalpha() or peek() == "_": advance()

                if (text := source[start:current].lower()) == "true": add(TRUE)
                elif text == "false": add(FALSE)
                elif text == "not": add(NOT)
                elif text == "none": add(NONE)
                elif text == "and": add(AND)
                elif text == "or": add(OR)
                elif text == "if": add(IF)
                elif text == "then": add(THEN)
                elif text == "end": add(END)
                elif text == "endif": add(END)
                elif text == "else": add(ELSE)
                elif text == "while": add(WHILE)
                elif text == "endwhile": add(END)
                elif text == "for": add(FOR)
                elif text == "to": add(TO)
                elif text == "step": add(STEP)
                elif text == "endfor": add(END)
                elif text in {"print", "output"}: add(PRINT)
                else: add(IDENTIFIER)
            else:
                errors.error(line, "Unexpected character")

        return current, line, tokens
    
    def scan_tokens() -> list[Token]:
        while current < len(source):
            start = current
            current, line, tokens = scan_token(start, current, line, source, tokens)
        tokens.append(Token(EOF, line=line))
        return tokens

    

