# Módulo principal para o projeto KeyMaster.
# Aqui será implementada a lógica de geração de senhas seguras.
import string  # Traz o módulo que nos dá conjuntos prontos de caracteres (letras, números, símbolos comuns).
import random  # Gerador de números aleatórios.
import secrets  # Gerador de números aleatórios seguros.
import sys # Usado para fechar o programa de forma controlada se o usuário cometer um erro grave.

# 1. FUNÇÕES DE VALIDAÇÃO DE INPUT:

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
        try: # tenta converter a entrada do usuário para um número inteiro
            tamanho = int(input("Qual o comprimento da senha desejada (mínimo 8)? "))
            if tamanho >=8: #verifica se o tamanho mínimo é 8
                return tamanho # Retorna o valor se for válido
            print(" O comprimento mínimo recomendado para uma senha segura é 8. Tente novamente.")

        except ValueError: # verifica se o usuário digitar algo que não é um número
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

# 2. Função Principal de Geração:

def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos): #Gera a senha segura usando parâmetros.
    pool_total = list(string.ascii_lowercase) # Base obrigatória: começa sempre com letras minúsculas.
    pools_requeridas = [string.ascii_lowercase] # Lista dos conjuntos que precisamos para garantir pelo menos um caractere

    if usar_maiusculas: # adiciona escolha p/ usuário, se True
        pool_total.extend(string.ascii_uppercase)
        pools_requeridas.append(string.ascii_uppercase)

    if usar_numeros:
        pool_total.extend(string.digits)
        pools_requeridas.append(string.digits)

    if usar_simbolos:
        pool_total.extend(string.punctuation)
        pools_requeridas.append(string.punctuation)

    senha = [] # Gera e gerante a composição
    for pool in pools_requeridas: # Garante a composição mínima (Pega 1 char de cada pool requerida)
        senha.append(random.choice(pool))

    num_restante = tamanho - len(senha) # Calcula quantos caracteres Faltam.

    for _ in range(num_restante): # Adiciona caracteres aleatórios.
        senha.append(random.choice(pool_total))

    random.shuffle(senha) # Embaralha a senha

    return "".join(senha)

