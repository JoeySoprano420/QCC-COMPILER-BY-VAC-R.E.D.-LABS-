import sys
from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer
from code_generator import CodeGenerator
from error_handling import ErrorHandler

class QuantumCodeCompiler:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.semantic_analyzer = SemanticAnalyzer()
        self.code_generator = CodeGenerator()
        self.error_handler = ErrorHandler()

    def compile(self, source_code):
        tokens = self.lexer.tokenize(source_code)
        ast = self.parser.parse(tokens)

        if not self.error_handler.has_errors():
            self.semantic_analyzer.analyze(ast)
        
        if not self.error_handler.has_errors():
            machine_code = self.code_generator.generate(ast)
            return machine_code
        else:
            return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qcc.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    with open(source_file, 'r') as f:
        source_code = f.read()

    compiler = QuantumCodeCompiler()
    machine_code = compiler.compile(source_code)

    if machine_code:
        print("Compilation Successful!")
        print(machine_code)
    else:
        print("Compilation Failed. Check for errors.")
