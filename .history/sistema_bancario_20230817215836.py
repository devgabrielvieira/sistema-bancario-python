menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

===> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


def depositar():
    global saldo, extrato
    valor_deposito = float(input("Digite o valor a ser depositado: "))

    if valor_deposito >= 0:
        saldo += valor_deposito
        extrato.append(f"Depósito de R${valor_deposito:.2f}\n")
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito não pode ser negativo.")


def sacar():
    global saldo, extrato, numero_saques
    if numero_saques < LIMITE_SAQUES:
        valor_saque = float(input("Digite o valor a ser sacado: "))

        if valor_saque <= saldo and valor_saque <= limite and valor_saque >= 0:
            saldo -= valor_saque
            extrato.append(f"Saque de R${valor_saque:.2f}\n")
            numero_saques += 1
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso. ")
        else:
            print(
                "Saldo insuficiente, valor negativo ou valor de saque acima do limite."
            )
    else:
        print("Limite de saques atingido.")


def exibir_extrato():
    print("\n===================== Extrato: =====================")
    for transacao in extrato:
        print(transacao)
    print(f"\nSaldo atual: R${saldo:.2f}")
    print(f"Limite de saques restantes: {LIMITE_SAQUES - numero_saques}")
    print("\n===================================================")


while True:
    try:
        opcao = int(input(menu))
    except ValueError:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
        continue

    if opcao == 1:
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        exibir_extrato()
    elif opcao == 0:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
