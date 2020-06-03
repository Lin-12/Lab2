from enum import Enum

class Regular(Enum):
    EOS = 0
    ANY = 1
    AT_BOL = 2
    AT_EOL = 3
    CCL_END = 4
    CCL_START = 5
    CLOSE_CURLY = 6
    CLOSE_PAREN = 7
    CLOSURE = 8
    DASH = 9
    END_OF_INPUT = 10
    L = 11
    OPEN_CURLY = 12
    OPEN_PAREN = 13
    OPTIONAL = 14
    OR = 15
    PLUS_CLOSE = 16

Regulars = {
    '.': Regular.ANY,
    '^': Regular.AT_BOL,
    '$': Regular.AT_EOL,
    ']': Regular.CCL_END,
    '[': Regular.CCL_START,
    '}': Regular.CLOSE_CURLY,
    '*': Regular.CLOSURE,
    '{': Regular.OPEN_CURLY,
    '|': Regular.OR,
    '+': Regular.PLUS_CLOSE,
}

class Lexer(object):                 # Lexical analysis of regular expressions
    def __init__(self, pattern):
        self.pattern = pattern
        self.lexeme = ''
        self.pos = 0
        self.isescape = False
        self.current_token = None

    def advance(self):
        pos = self.pos
        pattern = self.pattern
        if pos > len(pattern) - 1:
            self.current_token = Regular.EOS
            return Regular.EOS

        text = self.lexeme = pattern[pos]
        # Handle escape characters
        if text == '\\':
            self.isescape = not self.isescape
            self.pos = self.pos + 1
            self.current_token = self.handle_escape()
        else:
            self.current_token = self.handle_semantic(text)

        return self.current_token

    def handle_escape(self):
        expr = self.pattern.lower()
        pos = self.pos
        ev = {
            '\0': '\\',
            'b': '\b',
            'f': '\f',
            'n': '\n',
            's': ' ',
            't': '\t',
            'e': '\033',
        }
        rval = ev.get(expr[pos])
        if rval is None:
            if expr[pos] == '^':
                rval = self.handle_tip()
            elif expr[pos] == 'O':
                rval = self.handle_oct()
            elif expr[pos] == 'X':
                rval = expr[pos]
            else:
                rval = expr[pos]
        self.pos = self.pos + 1
        self.lexeme = rval
        return Regular.L

    def handle_semantic(self, text):
        self.pos = self.pos + 1
        return Regulars.get(text, Regular.L)

    def handle_tip(self):
        self.pos = self.pos + 1
        return self.pattern[self.pos] - '@'

    def handle_oct(self):
        return 1

    def handle_hex(self):
        return  1

    def match(self, token):
        return self.current_token == token



