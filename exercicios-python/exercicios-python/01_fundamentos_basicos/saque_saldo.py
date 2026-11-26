Saldo = float(input("Digite o saldo: "))
Saque = float(input("Digite o valor do saque: "))
Limite = float(input("Digite o limite: "))
Conta_Especial: bool = input("Conta especial? (s/n): ").strip().lower() == "s"
cliente = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis']

# AND = para ser True as duas condições precisam ser True

# OR = para ser True apenas uma das condições precisa ser True

'''expressao = Saldo >= Saque and Saque <= Limite or Conta_Especial and Saldo >= Saque
print('Expressão 1: {}'.format(expressao))

expressao2 = (Saldo >= Saque and Saque <= Limite) or (Conta_Especial and Saldo >= Saque)
print('Expressão 2: {}'.format(expressao2))
print('_'*30)
'''


conta_normal_com_saldo_suficiente = Saldo >= Saque
print('saldo suficiente: {}'.format(conta_normal_com_saldo_suficiente))
print('_'*40)
conta_especial_com_saldo_suficiente = Conta_Especial and Saldo >= Saque
print('Conta especial com saldo suficiente: {}'.format(conta_especial_com_saldo_suficiente))
print('_'*40)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print('Expressão 3: {}'.format(exp_3))

# IS NOT = para verificar se os objetos são diferentes
print('Os objetos são diferentes? {}'.format(conta_normal_com_saldo_suficiente is not conta_especial_com_saldo_suficiente))

# IN = para verificar se o objeto está na lista
ex_4 = 'João Doe' in cliente
print('João Doe está na lista de clientes? {}'.format(ex_4))

# NOT IN = para verificar se o objeto não está na lista
ex_5 = 'João Doe' not in cliente
print('João Doe não está na lista de clientes? {}'.format(ex_5))

