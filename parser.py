class Parser:
    def __init__(self):
        self.tokens = []
        self.current_index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.current_index = 0
        return self.expr()

    def expr(self):
        left = self.term()
        while self.match('PLUS', 'MINUS'):
            operator = self.previous()
            right = self.term()
            left = {'type': 'binary', 'operator': operator, 'left': left, 'right': right}
        return left

    def term(self):
        left = self.factor()
        while self.match('MULTIPLY', 'DIVIDE'):
            operator = self.previous()
            right = self.factor()
            left = {'type': 'binary', 'operator': operator, 'left': left, 'right': right}
        return left

    def factor(self):
        if self.match('NUMBER'):
            return {'type': 'literal', 'value': int(self.previous()[1])}
        elif self.match('LPAREN'):
            expr = self.expr()
            self.consume('RPAREN')
            return expr
        raise Exception("Invalid syntax")

    def match(self, *types):
        if self.check(*types):
            self.advance()
            return True
        return False

    def check(self, *types):
        if self.is_at_end():
            return False
        return self.tokens[self.current_index][0] in types

    def advance(self):
        self.current_index += 1
        return self.previous()

    def previous(self):
        return self.tokens[self.current_index - 1]

    def is_at_end(self):
        return self.current_index >= len(self.tokens)

    def consume(self, type):
        if self.check(type):
            return self.advance()
        raise Exception(f"Expected token type: {type}")
