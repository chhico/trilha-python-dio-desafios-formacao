
def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Valor depositado: R$ {valor:.2f}\n"
        print(f"\n Depósito de R$ {valor:.2f} realizado com sucesso! ")
    else:
        print(f"\n O Valor {valor} informado para depósito é inválido")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if valor > saldo:
        print(f"\n Saque de R$ {valor:.2f} não realizado! Seu Saldo é de apenas R$ {saldo:.2f}")

    elif valor > limite:
        print(f"\n Saque de R$ {valor:.2f} não realizado! Seu limite de valor para saque é de apenas R$ {limite:.2f}")

    elif numero_saques >= limite_saques:
        print(f"\n Saque de R$ {valor:.2f} não realizado! Você so tem direito a realizar {numero_saques} saques")

    elif valor > 0:
        saldo -= valor
        extrato += f"Valor sacado: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n Depósito de R$ {valor:.2f} realizado com sucesso! Saldo atual R$ {saldo:.2f}")

    else:
        print(f"\n O Valor {valor} informado para saque é inválido")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n======== Extrato para simples conferência ========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("====================================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = pesquisar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF pertence a um usuário ja cadastrado!")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário (dd-mm-aaaa): ")
    endereco = input("Informe o endereço do usuário (endereço, num - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def pesquisar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = pesquisar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nNão foi possível criar a conta, pois o CPF informado não pertece a nenhum usuário")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            num Conta:\t\t{conta['numero_conta']}
            Nome Usuário:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    menu = """\n
    ================ MENU ================
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [c] - Nova conta
    [l] - Listar contas
    [u] - Novo usuário
    [q] - Sair
    => """
    
    QTD_LIMITE_SAQUES = 3
    VALOR_LIMITE_SAQUES = 500
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    qtd_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, qtd_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=VALOR_LIMITE_SAQUES,
                numero_saques=qtd_saques,
                limite_saques=QTD_LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
