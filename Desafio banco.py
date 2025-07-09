menu = '''
============= BEM VINDO AO BANCO ALUNO =============

Escolha entre as opções abaixo: 
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

==>
'''
saldo = 0 
limite = 500
extrato = []
numsaque = 3

while True:
    opção = (input(menu)) 

    if opção == '1':
        depósito = float(input('Digite o valor do depósito: '))
        if depósito < 0:
            while depósito < 0:
                depósito = float(input('Não é possível depositar valores negativos. Por favor digite um valor positivo: '))
                if depósito >= 0: 
                    print ('Depósito realizado com sucesso!')
                    saldo += depósito
                    print (f'O saldo atual é de: R${saldo}')
                    extrato.append (f'Depósito de R$ {depósito}')
        elif depósito >= 0: 
            print ('Depósito realizado com sucesso!')
            saldo += depósito
            print (f'O saldo atual é de: R${saldo}')
            extrato.append (f'Depósito de R$ {depósito}')

    elif opção == '2':
        if numsaque > 0:
            print (f'Você ainda tem direito a {numsaque} saque(s) hoje')
            saque = float(input('Digite aqui o valor do saque (Max de 500R$): '))
            if saque > 500:
                while saque > 500:
                    saque = float(input('Seu valor extrapolou o limite de 500 R$ p/ saque. Tente novamente: '))
                resultado = saldo - saque
                if resultado > 0:
                    saldo = saldo - saque
                    print ('Saque realizado com sucesso!')
                    print (f'O saldo atual é de R${saldo}')
                    extrato.append (f'Saque de R${saque}')
                    numsaque = numsaque - 1
                else: 
                    print ('Você não tem saldo o bastante para a realização deste saque.')
            else: 
                resultado = saldo - saque
                if resultado >= 0:
                    saldo = saldo - saque
                    print (f'Saque de R${saque} realizado com sucesso!')
                    print (f'O saldo atual é de R${saldo}')
                    extrato.append (f'Saque de R${saque}')
                    numsaque = numsaque - 1
                else: 
                    print ('Você não tem saldo o bastante para a realização deste saque.')
        else:
            print ('Você já atingiu o limite maximo de saques no dia de hoje.')

    elif opção == '3':
        for p in extrato:
            print (p)
        print (f'O saldo atual é de R${saldo}')
    elif opção == '4':
        break
    else:
        print ('Opção inválida, tentre novamente:')

print ('FIM DO PROGRAMA!!')
