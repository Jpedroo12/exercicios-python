nomeCliente = str(input("Digite o nome do cliente: "))
idadeCliente = int(input("Digite a idade do cliente: "))
saldoInicial = float(input("Digite o saldo inicial do cliente: "))


print(f"\nBem-vindo, {nomeCliente.strip().title()}!")

while True:
    opcao = int(input("\nEscolha uma opção:\n1. Consultar saldo\n2. Realizar depósito\n3. Realizar saque\n4. Simulação de rendimento\n5. Sair\nOpção: "))
    if opcao == 1:
        print('Consultar saldo: R$ {:.2f}'.format(saldoInicial))

    elif opcao == 2:
        deposito = float(input("Digite o valor do depósito: "))
        saldoInicial += deposito
        print('Depósito realizado com sucesso! Novo saldo: R$ {:.2f}'.format(saldoInicial))
    elif opcao == 3:
        saque = float(input("Digite o valor do saque: "))
        if saque > saldoInicial:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saldoInicial -= saque
            print('Saque realizado com sucesso! Novo saldo: R$ {:.2f}'.format(saldoInicial))
    elif opcao == 4:
        print("Simulação de rendimento:")
        print("Considerando um rendimento de 0.5% ao mês:")
        meses = int(input("Digite o número de meses: "))
        saldoSimulado = saldoInicial
        for _ in range(meses):
            saldoSimulado *= 1.005
        print('Saldo simulado: R$ {:.2f}'.format(saldoSimulado))
    elif opcao == 5:
        print("Obrigado por utilizar nosso sistema! Até Logo")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")