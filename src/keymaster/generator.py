import string
import random
import secrets


def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    """Gera uma senha segura usando secrets."""

    pool_total = list(string.ascii_lowercase)
    pools_requeridas = [string.ascii_lowercase]

    if usar_maiusculas:
        pool_total.extend(string.ascii_uppercase)
        pools_requeridas.append(string.ascii_uppercase)

    if usar_numeros:
        pool_total.extend(string.digits)
        pools_requeridas.append(string.digits)

    if usar_simbolos:
        pool_total.extend(string.punctuation)
        pools_requeridas.append(string.punctuation)

    # Garante pelo menos 1 caractere de cada grupo escolhido
    senha_chars = [secrets.choice(pool) for pool in pools_requeridas]

    restante = tamanho - len(senha_chars)
    for _ in range(restante):
        senha_chars.append(secrets.choice(pool_total))

    random.SystemRandom().shuffle(senha_chars)

    senha = "".join(senha_chars)
    return senha
