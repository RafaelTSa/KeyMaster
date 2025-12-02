# Módulo principal para o projeto KeyMaster.
# Aqui será implementada a lógica de geração de senhas seguras.
import string  # Traz o módulo que nos dá conjuntos prontos de caracteres (letras, números, símbolos comuns).
import random  # Gerador de números aleatórios.
import secrets  # Gerador de números aleatórios seguros.
import sys # Usado para fechar o programa de forma controlada se o usuário cometer um erro grave.

def obter_opcao_sim_nao(pergunta): #Função auxiliar para garantir que o usuário responda com 's' (sim) ou 'n' (não).
    while True: # Pede a entrada, converte para minúsculas e remove espaços em branco (strip)
        reposta = input (f"{pergunta} (s/n: ").lower().strip()
if __name__ == "__main__":
    main()