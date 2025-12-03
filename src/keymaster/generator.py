import string
import random
import secrets

# 2. Função Principal de Geração: (usando secrets)


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

# 1 caractere de cada pool requerida
    senha_chars = [secrets.choice(pool) for pool in pools_requeridas]

    # restante com escolhas seguras
    num_restante = tamanho - len(senha_chars)
    for _ in range(num_restante):
        senha_chars.append(secrets.choice(pool_total))

    # shuffle seguro
    rng = random.SystemRandom()
    rng.shuffle(senha_chars)

    senha = "".join(senha_chars)
    return senha