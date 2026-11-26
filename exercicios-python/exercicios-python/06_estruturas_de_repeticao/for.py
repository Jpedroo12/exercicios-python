texto = input("Digite um texto: ")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
            print(letra, end=' ')
else:
    print() #Adiciona uma quebra de linha no final da execução do for

for numero in  range(0, 91, 9):
     print(numero, end=' ')