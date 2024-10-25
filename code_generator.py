class CodeGenerator:
    def generate(self, ast):
        if ast['type'] == 'binary':
            left = self.generate(ast['left'])
            right = self.generate(ast['right'])
            return f"({left} {ast['operator']} {right})"
        elif ast['type'] == 'literal':
            return str(ast['value'])
        return ""
