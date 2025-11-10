# Mini Compilador de Expressões Matemáticas
# Autor: Matheus Godoy
# Objetivo: Analisar e interpretar expressões matemáticas simples (+, -, *, /, parênteses)

import re

# ------------------------------
# 1. Analisador Léxico
# ------------------------------
def analisar_lexico(expressao):
    # Expressões regulares para tokens
    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expressao)
    print("\n=== ANÁLISE LÉXICA ===")
    for i, token in enumerate(tokens):
        tipo = "Número" if token.isdigit() else "Operador" if token in "+-*/" else "Parêntese"
        print(f"[{i}] '{token}' → Tipo: {tipo}")
    return tokens

# ------------------------------
# 2. Analisador Sintático e Interpretador
# ------------------------------
def avaliar_expressao(tokens):
    # Junta os tokens e avalia com segurança usando eval
    expressao_str = ''.join(tokens)
    try:
        resultado = eval(expressao_str)
        return resultado
    except Exception as e:
        print("Erro de sintaxe na expressão:", e)
        return None

# ------------------------------
# 3. Função principal
# ------------------------------
def main():
    print("=== MINI COMPILADOR DE EXPRESSÕES MATEMÁTICAS ===")
    expressao = input("Digite uma expressão (ex: 2 + 3 * (4 - 1)): ")

    # Etapa 1: Análise Léxica
    tokens = analisar_lexico(expressao)

    # Etapa 2: Avaliação
    print("\n=== INTERPRETAÇÃO ===")
    resultado = avaliar_expressao(tokens)
    if resultado is not None:
        print(f"Resultado da expressão: {resultado}")

if __name__ == "__main__":
    main()
