
saldo = float(input("Digite o saldo: "))
saque = float(input("Digite o valor do saque: "))

# verifica se o saldo é igual ao saque
print('Saldo é igual ao saque:', saldo == saque)

 # verifica se o saldo é diferente do saque
print('Saldo é diferente do saque:', saldo != saque)

# verifica se o saldo é maior que o saque
print('Saldo é maior que saque:', saldo > saque)

# verifica se o saldo é menor que o saque
print('Saldo é menor que saque:', saldo < saque)
saldo -= saque
# verifica se o saldo é maior ou igual ao saque
print(saldo)
print('Saldo é maior ou igual ao saque:', saldo >= saque)

# verifica se o saldo é menor ou igual ao saque
print('Saldo é menor ou igual ao saque:', saldo <= saque)