# Módulo principal para o projeto KeyMaster.
# Implementa geração de senhas com melhorias de usabilidade, logs e tratamento de erros.
import os
import string  # Traz o módulo que nos dá conjuntos prontos de caracteres (letras, números, símbolos comuns).
import random  # Gerador de números aleatórios.
import secrets  # Gerador de números aleatórios seguros.
import sys # Usado para fechar o programa de forma controlada se o usuário cometer um erro grave.
import logging

# Configuração do log
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "keymaster.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Utilitários de terminal (cores simples)
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def info(text):
    print(color(text, "34")) # azul

def success(text):
    print(color(text, "32")) # verde

def warning(text):
    print(color(text, "33")) # amarelo

def error(text):
    print(color(text, "31")) # vermelho



# 1. FUNÇÕES DE VALIDAÇÃO DE INPUT:


def obter_opcao_sim_nao(pergunta): #Função auxiliar para garantir que o usuário responda com 's' (sim) ou 'n' (não).
    while True:
        # Pede a entrada, converte para minúsculas e remove espaços em branco (strip)
        resposta = input(f"{pergunta} (s/n:) ").lower().strip()
        if resposta in ['s', 'n']:
            #retorna True se a resposta é valida
            return resposta == 's'
        # Se for inválido, exibe a mensagem e o loop repete
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

def obter_tamanho_senha(): # Pede o tamanho e garante que é inteiro >= 8.
    while True:
        entrada = input("Qual o comprimento da senha desejada (mínimo 8)? ").strip()
        if entrada == "":
            warning("Entrada vazia. Por favor, digite um número.")
            continue
        try:
            tamanho = int(entrada)
            if tamanho >= 8:
                return tamanho
            warning("O comprimento mínimo recomendado é 8. Tente novamente.")
        except ValueError:
            warning("Entrada inválida. Digite um número inteiro (ex: 12).")



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



# 3. Função de execução (MAIN) com tratamento e logs


def main(): #função principal que será executada
    print("\n" + "="*40)
    print("        KeyMaster - Gerador de Senhas")
    print("="*40)

    tamanho = obter_tamanho_senha() # Coleta do usuário o parâmetro

    info("\n--- Opções de Caracteres ---")
    usar_maiusculas = obter_opcao_sim_nao("Usar Letras Maiúsculas")
    usar_numeros = obter_opcao_sim_nao("Usar Números")
    usar_simbolos = obter_opcao_sim_nao("Usar Símbolos (ex: !@#$%^)")
    
    if not (usar_maiusculas or usar_numeros or usar_simbolos): # Verificação de segurança pelo menos uma opção deve ser True.
        error("\n[ERRO] É necessário selecionar pelo menos um tipo de caractere opcional para maior segurança.")
        logging.warning("Usuário não selecionou nenhuma opção de caractere.")
        sys.exit(1)

    senha_gerada = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos) #Geração da senha

    print("\n"+"="*40)
    success(f"Senha Gerada: {senha_gerada}")
    print("="*40)

    # Log de evento (não grava a senha em texto simples em produção; aqui é para registro do evento)
    logging.info(f"Senha gerada | comprimento={tamanho} | maiusculas={usar_maiusculas} | numeros={usar_numeros} | simbolos={usar_simbolos}")

    # Copiar para área de transferência (caso usuário queira)
    try:
            import pyperclip  # usuário pode instalar com pip install pyperclip
            pyperclip.copy(senha_gerada)
            success("Senha copiada para a área de transferência.")
    except Exception:
            info("Dica: instale 'pyperclip' para copiar automaticamente para o clipboard (opcional).")
            info("No windows: faça 'pip install pyperclip' no terminal")


# Executa programa

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        warning("\nExecução interrompida pelo usuário. Saindo...")
        logging.info("Execução interrompida pelo usuário (KeyboardInterrupt).")
        sys.exit(0)
    except Exception as e:
        error("\nOcorreu um erro inesperado. Veja o log para detalhes.")
        logging.exception("Erro inesperado no main()")
        sys.exit(1)