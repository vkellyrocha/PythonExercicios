p = float(input('Qual é o preço do produto? R$'))
np = p - (p*5/100)
print(f'O produto que custava R${p:.2f}, na promoção com desconto de 5% vai custar R${np:.2f}')
