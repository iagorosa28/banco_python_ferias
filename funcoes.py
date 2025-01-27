from datetime import datetime

def menu():
    print("1. Cadastrar cliente")
    print("2. Excluir cliente")
    print("3. Listar clientes")
    print("4. Debitar")
    print("5. Depostiar")
    print("6. Transferir")
    print("7. Débito automático")
    print("8. Extrato")
    print("9. Sair")

def cadastrar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    if cpf in clientes:
        print("Cliente já existente!")
    else:
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        conta = input("Digite o tipo de conta do cliente (normal ou plus): ")
        while conta != "normal" and conta != "plus":
            conta = input("Tipo de conta não existente! Tente ""normal"" ou ""plus"": ")
        saldo = float(input("Digite o saldo inicial do cliente: "))
        data = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        texto_extrato = f"{data} {hora} | +{saldo:.2f} | taxa: N/A | depósito inicial"
        extrato = [texto_extrato]
        automatico = {}
        cliente = {
            "cpf": cpf,
            "nome": nome,
            "idade": idade,
            "conta": conta,
            "saldo": saldo,
            "extrato": extrato,
            "automatico": automatico
        }
        clientes[cpf] = cliente
        print("Cliente cadastrado com sucesso!")
    print()

def excluir(clientes):
    cpf = input("Digite o CPF do cliente que deseja excluir: ")
    if cpf in clientes:
        del clientes[cpf]
        print("Cliente excluído com sucesso!")
    else:
        print("Cliente não existente!")
    print()

def listar(clientes):
    print("---------------")
    for cpf, dados in clientes.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']}")
        print(f"Conta: {dados['conta']}")
        print(f"Saldo: R$ {dados['saldo']:.2f}")
        print("---------------")
    print()

def debitando(acao, cliente, valor, recebidor):
    data = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    if cliente["conta"] == "normal" and cliente["saldo"] - (valor + (valor * 0.05)) >= -1000:
        cliente["saldo"] = cliente["saldo"] - (valor + (valor * 0.05))
        if acao == "debito":
            texto_extrato = f"{data} {hora} | -{(valor + (valor * 0.05)):.2f} | taxa: 5% | débito"
            cliente["extrato"].append(texto_extrato)
            print(f"Débito realizado com sucesso! Uma taxa de 5% foi aplicada.")
        else:
            texto_extrato = f"{data} {hora} | -{(valor + (valor * 0.05)):.2f} | taxa: 5% | transferência para {recebidor}"
            cliente["extrato"].append(texto_extrato)
    elif cliente["conta"] == "plus" and cliente["saldo"] - (valor + (valor * 0.03)) >= -5000:
        cliente["saldo"] = cliente["saldo"] - (valor + (valor * 0.03))
        if acao == "debito":
            texto_extrato = f"{data} {hora} | -{(valor + (valor * 0.03)):.2f} | taxa: 3% | débito"
            cliente["extrato"].append(texto_extrato)
            print(f"Débito realizado com sucesso! Uma taxa de 3% foi aplicada.")
        else:
            texto_extrato = f"{data} {hora} | -{(valor + (valor * 0.03)):.2f} | taxa: 3% | transferência para {recebidor}"
            cliente["extrato"].append(texto_extrato)
    else:
        if acao == "debito":
            print("Saldo insuficiente!")
        else:
            print("Saldo de origem insuficiente para transferência!")
            return 1

def debitar(clientes):
    cpf = input("Digite o CPF do cliente que deseja debitar: ")
    if cpf in clientes:
        cliente = clientes[cpf]
        valor = float(input("Insira o valor a ser debitado: "))
        debitando("debito", cliente, valor, "N/A")
    else:
        print("Cliente não existente!")
    print()

def depositando(acao, cliente, valor, pagador):
    data = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    cliente["saldo"] = cliente["saldo"] + valor
    if acao == "deposito":
        texto_extrato = f"{data} {hora} | +{valor:.2f} | taxa: N/A | depósito"
        cliente["extrato"].append(texto_extrato)
        print("Depósito realizado com sucesso!")
    else:
        texto_extrato = f"{data} {hora} | +{valor:.2f} | taxa: N/A | transferência de {pagador}"
        cliente["extrato"].append(texto_extrato)

def depositar(clientes):
    cpf = input("Digite o CPF do cliente que deseja depositar: ")
    if cpf in clientes:
        cliente = clientes[cpf]
        valor = float(input("Insira o valor a ser depositado: "))
        depositando("deposito", cliente, valor, "N/A")
    else:
        print("Cliente não existente!")
    print()

def transferir(clientes):
    cpf_origem = input("Digite o CPF de origem: ")
    if cpf_origem in clientes:
        cpf_destino = input("Digite o CPF de destino: ")
        if cpf_destino in clientes:
            cliente_origem = clientes[cpf_origem]
            cliente_destino = clientes[cpf_destino]
            valor = float(input("Insira o valor a ser transferido: "))
            retorno = debitando("transferencia", cliente_origem, valor, cliente_destino["nome"])
            if retorno != 1:
                depositando("transferencia", cliente_destino, valor, cliente_origem["nome"])
                print("Transferência realizada com sucesso!")
        else:
            print("Cliente destino não existente!")
    else:
        print("Cliente origem não existente!")
    print()

def automatizar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    if cpf in clientes:
        cliente = clientes[cpf]
        automatico = cliente['automatico']
        print("1. Adicionar débito automático")
        print("2. Cancelar débito automático")
        print("3. Consultar débitos automáticos")
        opcao = int(input("Digite uma opção: "))
        print()
        if opcao == 1:
            destino = input("Digite o destino do débito automático: ")
            if destino in automatico:
                print("Débito automático já existente!")
            else:
                valor = float(input("Digite o valor a ser debitado mensalmente: "))
                dia = int(input("Digite o dia do débito: "))
                debito_automatico = [destino, valor, dia]
                automatico[destino] = debito_automatico
                print("Débito automático cadastrado com sucesso!")
        elif opcao == 2:
            destino = input("Digite o destino do débito automático que deseja cancelar: ")
            if destino in automatico:
                del automatico[destino]
                print("Débito automático cancelado com sucesso!")
            else:
                print("Destino não existente!")
        elif opcao == 3:
            print("---------------")
            for automatico, dados in automatico.items():
                print(f"Destino: {dados[0]}")
                print(f"Valor: R$ {dados[1]:.2f}")
                print(f"Dia: {dados[2]}")
                print("---------------")
        else:
            print("Erro!")
    else:
        print("Cliente não existente!")
    print()

def extrato(clientes):
    cpf = input("Digite o CPF do cliente que deseja exibir o extrato: ")
    if cpf in clientes:
        extrato = clientes[cpf]['extrato']
        print("---------------")
        for dados in extrato:
            print(dados)
        print("---------------")
    else:
        print("Cliente não existente!")
    print()