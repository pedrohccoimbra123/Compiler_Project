class SymbolTable:
    def __init__(self):
        self.symbols = {}  # Armazena variáveis declaradas no formato {nome: {tipo, valor}}

    def declare(self, name, var_type):
        if name in self.symbols:
            raise Exception(f"Erro semântico: Variável '{name}' já declarada.")
        self.symbols[name] = {'type': var_type, 'value': None}

    def assign(self, name, value):
        if name not in self.symbols:
            raise Exception(f"Erro semântico: Variável '{name}' não declarada.")
        self.symbols[name]['value'] = value

    def get(self, name):
        if name not in self.symbols:
            raise Exception(f"Erro semântico: Variável '{name}' não declarada.")
        return self.symbols[name]

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, node):
        if node[0] == 'program':
            for stmt in node[1]:
                self.analyze(stmt)
        elif node[0] == 'declaration':
            var_type = node[1]  # Tipo da variável
            var_name = node[2]  # Nome da variável
            self.symbol_table.declare(var_name, var_type)
        elif node[0] == 'assignment':
            var_name = node[1]
            expr_value = self.evaluate_expression(node[2])
            var_info = self.symbol_table.get(var_name)
            # Verificar compatibilidade de tipos
            if var_info['type'] == 'int' and not isinstance(expr_value, int):
                raise Exception(f"Erro semântico: Esperado inteiro para '{var_name}', mas recebeu {type(expr_value).__name__}.")
            elif var_info['type'] == 'float' and not isinstance(expr_value, (int, float)):
                raise Exception(f"Erro semântico: Esperado ponto flutuante para '{var_name}', mas recebeu {type(expr_value).__name__}.")
            self.symbol_table.assign(var_name, expr_value)
        elif node[0] == 'if':
            condition = self.evaluate_expression(node[1])
            if not isinstance(condition, bool):
                raise Exception("Erro semântico: Condição do 'if' deve ser booleana.")
            for stmt in node[2]:
                self.analyze(stmt)
            if node[3]:  # Bloco else
                for stmt in node[3]:
                    self.analyze(stmt)

    def evaluate_expression(self, node):
        if node[0] == 'binary_op':
            left = self.evaluate_expression(node[2])
            right = self.evaluate_expression(node[3])
            op = node[1]
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    raise Exception("Erro semântico: Divisão por zero.")
                return left / right
        elif node[0] == 'value':
            value = node[1]
            if isinstance(value, str):  # Variável
                return self.symbol_table.get(value)['value']
            return value
