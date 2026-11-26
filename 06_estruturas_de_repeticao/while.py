opcao = int(input('digite uma opção para qual sistema deseja acessar: \n [1] banco \n [2] Extrato \n [3] gerador de 100 números menos o escolhido \n [0] Sair \n:'))

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [3] gerador de 100 números menos o escolhido \n [0] Sair \n:"))

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Extrato gerado com sucesso!")
    elif opcao == 3:
        print("Gerando 100 números...")
    else:
        print("Opcao invalida, tente novamente!")

while opcao == 2:
    numero = int(input("Digite um numero: "))

    if numero == 0:
        break
    print('o numero é: {}'.format(numero))

while opcao == 3:
 for numero in range(100):
    if numero == 12:
        continue
    print(numero, end=' ')

while opcao == 0:
    print("Saindo do sistema...")