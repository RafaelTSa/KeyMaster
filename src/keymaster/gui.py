import tkinter as tk
from tkinter import messagebox

from keymaster.generator import gerar_senha

def gerar():
    try:
        tamanho = int(entry_tamanho.get())

        if tamanho < 8:
            raise ValueError
        
        senha = gerar_senha(
            tamanho,
            var_maiusculas.get(),
            var_numeros.get(),
            var_simbolos.get()
        )

        # Mostrar a senha na interface
        resultado.config(text=senha)

        # ✅ COPIAR AUTOMATICAMENTE PARA A ÁREA DE TRANSFERÊNCIA
        root.clipboard_clear()
        root.clipboard_append(senha)

        messagebox.showinfo(
            "Sucesso",
            "Senha gerada e copiada para a área de transferência."
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um número válido (mínimo 8)."
        )


# Janela principal
root = tk.Tk()
root.title("KeyMaster - Gerador de Senhas")
root.geometry("400x300")
root.resizable(False, False)

# Tamanho da senha
tk.Label(root, text="Tamanho da senha (mín. 8):").pack(pady=5)
entry_tamanho = tk.Entry(root)
entry_tamanho.insert(0, "12")
entry_tamanho.pack()

# Opções
var_maiusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Letras maiúsculas", variable=var_maiusculas).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Números", variable=var_numeros).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Símbolos", variable=var_simbolos).pack(anchor="w", padx=20)

# Botão
tk.Button(root, text="Gerar Senha", command=gerar).pack(pady=10)

# Resultado
resultado = tk.Label(root, text="", font=("Courier", 12), fg="green")
resultado.pack(pady=10)

# Executar a interface
root.mainloop()