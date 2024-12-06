import ply.lex as lex

# Palavras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'read': 'READ',
}

# Definição dos tokens
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'MULT', 'DIV', 'ASSIGN',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
    'GT', 'LT',  # Operadores relacionais
] + list(reserved.values())  # Inclui palavras reservadas nos tokens

# Regras para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_GT = r'>'
t_LT = r'<'

# Regras para identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra reservada
    return t

# Regras para números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Regra para rastrear linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Manipulação de erros
def t_error(t):
    print(f"Erro léxico na linha {t.lexer.lineno}: Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o analisador léxico
lexer = lex.lex()
