import re

class Lexer:
    def __init__(self):
        self.tokens = []
        self.current_token = None

    def tokenize(self, source_code):
        # Simple regex patterns for tokenization
        patterns = {
            'NUMBER': r'\d+',
            'PLUS': r'\+',
            'MINUS': r'-',
            'MULTIPLY': r'\*',
            'DIVIDE': r'/',
            'LPAREN': r'\(',
            'RPAREN': r'\)',
            'IDENTIFIER': r'[a-zA-Z_]\w*',
            'WHITESPACE': r'\s+'
        }
        
        # Compile the patterns
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns.items())
        token_pattern = re.compile(token_regex)

        for match in token_pattern.finditer(source_code):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE':
                self.tokens.append((kind, value))
        return self.tokens
