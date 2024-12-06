# Compiler_Project
ByteFlow é um compilador simples desenvolvido em Python para a linguagem básica MiniLang. Ele implementa análise léxica, sintática e semântica, suportando variáveis, operações aritméticas, controle de fluxo (if-else, while) e entrada/saída. Feito com PLY, ideal para aprender sobre compiladores.

---

## Funcionalidades

1. **Declaração de variáveis**:
   - Tipos suportados: `int` (inteiro) e `float` (ponto flutuante).
   - Exemplo: `int a; float b;`

2. **Operações aritméticas**:
   - Suporte para: adição (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`).
   - Exemplo: `a = 5 + 3;`

3. **Estruturas de controle de fluxo**:
   - Condicional `if-else`.
   - Laço de repetição `while`.
   - Exemplo:
     ```plaintext
     if (a > b) {
         print(a);
     } else {
         print(b);
     }
     ```

4. **Entrada e saída de dados**:
   - `read` para entrada.
   - `print` para saída.
   - Exemplo:
     ```plaintext
     int x;
     read(x);
     print(x);
     ```

5. **Detecção e tratamento de erros**:
   - Léxicos, sintáticos e semânticos.

---

## Estrutura do Projeto

- **`lexer.py`**:
  - Responsável pela análise léxica.
  - Identifica tokens como palavras-chave, operadores e identificadores.
  - Trata erros léxicos, como caracteres inválidos.

- **`parser.py`**:
  - Realiza a análise sintática.
  - Constrói uma Árvore Sintática Abstrata (AST).
  - Verifica a estrutura gramatical do código e relata erros sintáticos.

- **`semantic.py`**:
  - Executa a análise semântica.
  - Verifica tipos de variáveis, gerencia escopos e detecta usos incorretos.
  - Garante compatibilidade de tipos em atribuições e operações.

- **`interpreter.py`**:
  - Interpreta a AST gerada pelo parser e executa os comandos.
  - Imprime resultados das operações e simula a execução do código.

- **`main.py`**:
  - Integra todas as etapas do compilador.
  - Lê o código-fonte, passa pelas análises léxica, sintática, semântica e executa a interpretação.

---
