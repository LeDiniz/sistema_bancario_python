menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"DEPÓSITO - R${deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido, tente novamente.")

    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))
        saldo_insuficiente = saque > saldo
        limite_insufiente = saque > limite
        if saldo_insuficiente:
            print("Não será possível sacar o dinheiro por falta de saldo.")
        elif limite_insufiente:
            print("Limite indisponível para saque.")
        elif saque <= limite and saque <= saldo:
            numero_saques += 1
            if numero_saques <= LIMITE_SAQUES:
                saldo -= saque
                extrato += f"SAQUE - R${saque:.2f}\n"
                print("Saque realizado com sucesso!")
            else:
                 print("Não será possível sacar, limite diário atingido.")

    elif opcao == "e":
        print("------------EXTRATO------------")
        print("Nenhuma movimentação bancária foi realizada." if not extrato else extrato)
        print(f"SALDO - R${saldo:.2f}")
        print("-------------------------------")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")