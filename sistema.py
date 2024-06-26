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
    opcao = input(menu).lower()

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: R$'))
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
        print(f"Saldo: R${saldo:.2f}\n")
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: R$'))
        if valor > saldo:
            print('Saldo insuficiente!')
        elif valor > limite:
            print('Limite de saque excedido!')
        elif numero_saques >= LIMITE_SAQUES:
            print('Número de saques excedido!')
        else:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numero_saques += 1
    elif opcao == 'e':
        print('Extrato:\n', extrato)
        print(f"Saldo: R${saldo:.2f}")
    elif opcao == 'q':
        break
    else:
        print('Opção inválida!')
    

    

