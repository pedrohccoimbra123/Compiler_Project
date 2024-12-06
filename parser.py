import ply.yacc as yacc
from lexer import tokens  # Importa os tokens definidos no lexer.py

# Regra inicial
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

# Lista de declarações ou comandos
def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# Declaração de variáveis
def p_statement_declaration(p):
    '''statement : INT ID SEMICOLON
                 | FLOAT ID SEMICOLON'''
    p[0] = ('declaration', p[1], p[2])

# Atribuições
def p_statement_assignment(p):
    '''statement : ID ASSIGN expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

# Estruturas de controle: if e while
def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE
                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6], None)
    else:
        p[0] = ('if', p[3], p[6], p[10])

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('while', p[3], p[6])

# Entrada e saída: print e read
def p_statement_print(p):
    '''statement : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('print', p[3])

def p_statement_read(p):
    '''statement : READ LPAREN ID RPAREN SEMICOLON'''
    p[0] = ('read', p[3])

# Expressões
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression GT term
                  | expression LT term
                  | term'''
    if len(p) == 4:
        p[0] = ('binary_op', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term MULT factor
            | term DIV factor
            | factor'''
    if len(p) == 4:
        p[0] = ('binary_op', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = ('value', p[1])
    else:
        p[0] = p[2]

# Manipulação de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro sintático: Token inesperado '{p.value}' na linha {p.lineno}")
    else:
        print("Erro sintático: Fim inesperado do arquivo")

# Construção do analisador sintático
parser = yacc.yacc()
