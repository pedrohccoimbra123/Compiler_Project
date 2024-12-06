from lexer import lexer
from parser import parser
from interpreter import interpret, SymbolTable  # Supondo que você tenha o interpretador no arquivo interpreter.py

if __name__ == "__main__":
    # Código de exemplo na linguagem
    code = """
    int x;
    float y;
    x = 10 + 5;
    y = x / 2.0;
    if (x > 10) {
        print(x);
    } else {
        print(y);
    }
    while (x > 0) {
        x = x - 1;
        print(x);
    }
    """

    # Alimentar o lexer com o código
    lexer.input(code)

    # Exibir tokens
    print("Tokens:")
    token = lexer.token()
    while token:
        print(token)
        token = lexer.token()

    # Análise Sintática
    print("\nAST Gerada:")
    ast = parser.parse(code)
    print(ast)

    # Criar a tabela de símbolos
    symbol_table = SymbolTable()

    # Interpretação da AST
    print("\nResultado da Interpretação:")
    interpret(ast, symbol_table)
