'''Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o
tipo de instalação: R para residências, I para indústrias e C para
comércios. Calcule o preço a pagar de acordo com a tabela a seguir.'''
quant = float(input('Quantidade de kWh consumida: '))
print('Tipo de instalação: ')
print('R para residências, I para indústrias e C para comércios.')
tipo = input().lower()
preco = 0
if tipo == 'r':
    if quant <=500:
        preco = quant * 0.4
    else:
        preco = quant * 0.65
elif tipo == 'c':
    if quant <= 1000:
        preco = quant * 0.55
    else:
        preco = quant * 0.60
elif tipo == 'i':
    if quant <= 5000:
        preco = quant * 0.55
    else:
        preco = quant * 0.60
else:
    print('Tipo invalido')
print(f'Preço : R${preco:.2f}')