numInt = int(input('Digite um número inteiro: \n'))
resposta = int(input('Qual base vc quer? \n1 para binário, \n2 paraa octal e \n3 para hexadecimal\n'))

if resposta == 1:
    binario = bin(numInt)
    binario_limpo = bin(numInt)[2:]
    print('Seu numero é {}, em binario é: {}\n'.format(numInt, binario_limpo))

elif resposta == 2:
    octal = oct(numInt)
    octal_limpo = oct(numInt)[2:]
    print('Seu numero é {}, em octal é: {}\n'.format(numInt, octal_limpo))

elif resposta == 3:
    hexadecimal = hex(numInt)
    hexadecimal_limpo = hex(numInt)[2:]
    print('Seu numero é {}, em hexadecimal é: {}\n'.format(numInt, hexadecimal_limpo))