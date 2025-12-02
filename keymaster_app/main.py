# Módulo principal para o projeto KeyMaster.
# Aqui será implementada a lógica de geração de senhas seguras.
import string  # Traz o módulo que nos dá conjuntos prontos de caracteres (letras, números, símbolos comuns).
import random  # Gerador de números aleatórios.
import secrets  # Gerador de números aleatórios seguros.
import sys # Usado para fechar o programa de forma controlada se o usuário cometer um erro grave.

def obter_opcao_sim_nao(pergunta): #Função auxiliar para garantir que o usuário responda com 's' (sim) ou 'n' (não).
    while True:
        # Pede a entrada, converte para minúsculas e remove espaços em branco (strip)
        resposta = input (f"{pergunta} (s/n: ").lower().strip()
        if resposta in ['s', 'n']:
            #retorna True se a resposta é valida
            return resposta == 's'
        # Se for inválido, exibe a mensagem e o loop repete
        print("Resposta inválida. Por favor, digite 's para sim ou 'n para não.")

def obter_tamanho_senha(): # Função para obter o tamanho desejado da senha, garantindo que seja um número válido (mínimo 8).
    while True:
        try:
            tamanho = int(input("Qual o comprimento da senha desejada (mínimo 8)? "))
