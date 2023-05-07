'''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.'''
valor = float(input('Qual o valor da casa a comprar: R$'))
salario = float(input('Qual o valor do seu salário: R$'))
quant = float(input('Quantidade de anos a pagar: '))
prestacao = valor/(quant * 12)
if prestacao <= (salario * 0.3):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
