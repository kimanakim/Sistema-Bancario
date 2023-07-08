menu = """
    Seja bem-vindo ao nosso banco! Selecione a opcao desejada:
    [a] Deposito
    [b] Saque
    [c] Extrato
    [d] Sair
"""

saldo = 0
extrato = ""
limite_saque = 500
quantidade_saques = 0

while True:
    
    selecao = (input(menu)).lower()
    
    if selecao == "a":
        deposito = float(input("Digite o valor a depositar: "))
        if deposito < 0:
            print("Valor invalido")
        else:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            
    elif selecao == "b":
        saque = float(input("Digite o valor que deseja sacar: "))
        if saque < 0:
            print("Valor invalido")
        elif saque > 500 and saque < saldo:
            print("Limite por saque excedido")
        elif saque > saldo:
            print("Saldo insuficiente")
        elif quantidade_saques >= 3:
            print("Limite diario excedido")
        else:
            saldo -= saque
            quantidade_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print( f"Saque de R${saque} realizado com sucesso." )

    elif selecao == "c":
        if extrato == "":
            print("Nao existem movimentacoes nessa conta")
        else:
            print( f"**********Extrato********** \n {extrato}")
            print( f"\nSaldo: R${saldo:.2f}")
            
    elif selecao == "d":
        break
    
    else:
        print("Operacao invalida")