MAIOR_IDADE = 18
IDADE_MINIMA = [16, 17]
idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade,pode tirar a cnh.")

elif idade == IDADE_MINIMA[0] or idade == IDADE_MINIMA[1]:
    print("Você é menor de idade, mas pode fazer as aulas teóricas.")

else:
    print("Você não tem idade, não pode tirar a cnh.")


