import tkinter as tk
from tkinter import messagebox
import requests

def consultar_cep(cep):
    # Remove caracteres não numéricos do CEP
    cep = cep.replace("-", "").strip()
    
    if len(cep) != 8 or not cep.isdigit():
        messagebox.showerror("Erro", "CEP inválido! Digite apenas 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    # Verifica se a requisição foi bem sucedida
    if resposta.status_code != 200:
        messagebox.showerror("Erro", "Não foi possível acessar a API.")
        return
    
    dados = resposta.json()

    #Verifica se o CEP é válido
    if "erro" in dados:
        messagebox.showwarning("Aviso", "CEP não encontrado!")
        return
    
    return dados  # Retorna os dados para serem exibidos na interface

def exibir_resultado(dados):
    resultado.set(
        f"Rua: {dados['logradouro']}\n"
        f"Bairro: {dados['bairro']}\n"
        f"Cidade: {dados['localidade']} - {dados['uf']}"
    )

def consultar_cep_interface():
    cep = entrada_cep.get()
    dados = consultar_cep(cep)
    if dados:
        exibir_resultado(dados)

if __name__ == "__main__":

    # Configuracao da janela
    janela = tk.Tk()
    janela.title("Consulta CEP")
    janela.geometry("300x250")

    # Label
    tk.Label(janela, text="Digite o CEP:", font=("Arial", 12)).pack(pady=5)

    # Entrada de texto
    entrada_cep = tk.Entry(janela, font=("Arial", 12), justify="center")
    entrada_cep.pack(pady=5)

    # Botão
    botao = tk.Button(janela, text="Consultar", font=("Arial", 12), command=consultar_cep_interface)
    botao.pack(pady=10)

    # Resultado
    resultado = tk.StringVar()
    tk.Label(janela, textvariable=resultado, font=("Arial", 11), justify="left").pack(pady=10)

    # Rodar janela
    janela.mainloop()
    # while True:
    #     cep = input("Digite o CEP (apenas números) ou 'sair' para encerrar: ")

    #     if cep.lower() == 'sair':
    #         print('Encerrando... ')
    #         break

    #     if len(cep) != 8 or not cep.isdigit():
    #         print("❌ CEP inválido! Digite apenas 8 números.")
    #     else:
    #         dados = consultar_cep(cep)
    #         if dados:
    #             print("\n📍 Endereço encontrado:")
    #             print(f"Rua: {dados['logradouro']}")
    #             print(f"Bairro: {dados['bairro']}")
    #             print(f"Cidade: {dados['localidade']} - {dados['uf']}")

