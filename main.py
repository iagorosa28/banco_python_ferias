from funcoes import *
import json
import os

clientes = {}

if os.path.exists("arquivo.json"):
    with open("arquivo.json", "r") as arquivo:
        clientes = json.load(arquivo)
else:
    with open("arquivo.json", "w") as arquivo:
        json.dump(clientes, arquivo)

while True:
    menu()
    opcao = int(input("Digite uma opção: "))
    print()
    if opcao == 1:
        cadastrar(clientes)
    elif opcao == 2:
        excluir(clientes)
    elif opcao == 3:
        listar(clientes)
    elif opcao == 4:
        debitar(clientes)
    elif opcao == 5:
        depositar(clientes)
    elif opcao == 6:
        transferir(clientes)
    elif opcao == 7:
        automatizar(clientes)
    elif opcao == 8:
        extrato(clientes)
    elif opcao == 9:
        print("Tchau!")
        break
    else:
        print("Erro!")

with open("arquivo.json", "w") as arquivo:
    json.dump(clientes, arquivo, indent=4)