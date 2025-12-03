import os
import sys
import logging
from keymaster.generator import gerar_senha


# =============================
# Configuração de Logs
# =============================

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "keymaster.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# =============================
# Utilitários de Terminal
# =============================

def color(text, code):
    return f"\033[{code}m{text}\033[0m"


def info(text):
    print(color(text, "34"))  # Azul


def success(text):
    print(color(text, "32"))  # Verde


def warning(text):
    print(color(text, "33"))  # Amarelo


def error(text):
    print(color(text, "31"))  # Vermelho


# =============================
# Funções de Entrada (Input)
# =============================

def obter_opcao_sim_nao(pergunta):
    """Garante resposta apenas 's' ou 'n'."""
    while True:
        resposta = input(f"{pergunta} (s/n): ").lower().strip()
        if resposta in ("s", "n"):
            return resposta == "s"
        warning("Resposta inválida. Digite 's' ou 'n'.")


def obter_tamanho_senha():
    """Garante que o tamanho seja um número >= 8."""
    while True:
        entrada = input("Comprimento da senha (mínimo 8): ").strip()
        try:
            tamanho = int(entrada)
            if tamanho >= 8:
                return tamanho
            warning("O tamanho mínimo recomendado é 8.")
        except ValueError:
            warning("Digite um número inteiro válido.")


# =============================
# Função Principal
# =============================

def main():
    print("\n" + "=" * 40)
    print("        KeyMaster - Gerador de Senhas")
    print("=" * 40)

    tamanho = obter_tamanho_senha()

    info("\nOpções de caracteres:")
    usar_maiusculas = obter_opcao_sim_nao("Usar letras maiúsculas")
    usar_numeros = obter_opcao_sim_nao("Usar números")
    usar_simbolos = obter_opcao_sim_nao("Usar símbolos")

    if not (usar_maiusculas or usar_numeros or usar_simbolos):
        error("Selecione pelo menos uma opção adicional.")
        logging.warning("Nenhuma opção de caracteres selecionada.")
        sys.exit(1)

    senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)

    print("\n" + "=" * 40)
    success(f"Senha gerada: {senha}")
    print("=" * 40)

    logging.info(
        f"Senha gerada | tamanho={tamanho} | "
        f"maiusculas={usar_maiusculas} | "
        f"numeros={usar_numeros} | "
        f"simbolos={usar_simbolos}"
    )

    # Copiar para área de transferência (opcional)
    try:
        import pyperclip
        pyperclip.copy(senha)
        success("Senha copiada para a área de transferência.")
    except Exception:
        info("Dica: instale 'pyperclip' para copiar automaticamente.")


# =============================
# Execução Segura
# =============================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        warning("\nExecução interrompida pelo usuário.")
        logging.info("Programa interrompido manualmente.")
        sys.exit(0)
    except Exception:
        error("Erro inesperado. Verifique o log.")
        logging.exception("Erro não tratado.")
        sys.exit(1)
