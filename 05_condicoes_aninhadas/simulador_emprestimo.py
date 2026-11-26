valorCasa = float(input('Qual é o valor da casa? \nR$ '))
salario = float(input('Qual é o seu salário? \nR$ '))
anos = int(input('Quantos anos pretende pagar a casa?\n'))

meses = anos * 12

prestacao = valorCasa / meses

porExceder = salario * 0.30

diferenca = prestacao - porExceder


if prestacao > porExceder:
    print('Negado!!\n prestação excedeu 30% do seu salario por R$:{:.2f},\n a prestação era de {:.2f}, \n e os 30% do seu salario é de {}'.format(diferenca, prestacao, porExceder))
else:
    print('Aprovado!!!\n a prestação vai ser de R$:{:.2f},\n durante {} anos'.format(prestacao, anos))