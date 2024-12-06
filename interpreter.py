# interpreter.py

class SymbolTable:
    def __init__(self):
        self.symbols = {}  # Dicionário para armazenar variáveis e seus valores

    def declare(self, name, var_type):
        if name in self.symbols:
            raise Exception(f"Erro: A variável '{name}' já foi declarada.")
        self.symbols[name] = {'type': var_type, 'value': None}

    def assign(self, name, value):
        if name not in self.symbols:
            raise Exception(f"Erro: A variável '{name}' não foi declarada.")
        self.symbols[name]['value'] = value

    def get(self, name):
        if name not in self.symbols:
            raise Exception(f"Erro: A variável '{name}' não foi declarada.")
        return self.symbols[name]['value']


# Função para interpretar a AST
def interpret(ast, symbol_table):
    if ast[0] == 'program':
        for stmt in ast[1]:
            interpret(stmt, symbol_table)
    elif ast[0] == 'declaration':
        var_type = ast[1]
        var_name = ast[2]
        symbol_table.declare(var_name, var_type)
        print(f"Declarando variável {var_name} do tipo {var_type}")
    elif ast[0] == 'assignment':
        var_name = ast[1]
        value = interpret(ast[2], symbol_table)  # Avalia a expressão à direita
        symbol_table.assign(var_name, value)
        print(f"Atribuindo valor para variável {var_name}: {value}")
    elif ast[0] == 'print':
        value = interpret(ast[1], symbol_table)
        print(f"Imprimindo: {value}")
    elif ast[0] == 'binary_op':
        # Cálculo de operações aritméticas e relacionais
        if ast[1] == '+':
            return interpret(ast[2], symbol_table) + interpret(ast[3], symbol_table)
        elif ast[1] == '-':
            return interpret(ast[2], symbol_table) - interpret(ast[3], symbol_table)
        elif ast[1] == '*':
            return interpret(ast[2], symbol_table) * interpret(ast[3], symbol_table)
        elif ast[1] == '/':
            return interpret(ast[2], symbol_table) / interpret(ast[3], symbol_table)
        elif ast[1] == '>':
            return interpret(ast[2], symbol_table) > interpret(ast[3], symbol_table)
        elif ast[1] == '<':
            return interpret(ast[2], symbol_table) < interpret(ast[3], symbol_table)
    elif ast[0] == 'value':
        # Se for um valor direto, retorna o valor (pode ser número ou variável)
        if isinstance(ast[1], str):  # Se for uma variável
            return symbol_table.get(ast[1])
        return ast[1]  # Caso contrário, é um número literal
