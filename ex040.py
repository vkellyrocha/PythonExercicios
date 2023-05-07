'''Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km
e R$ 0,45 para viagens mais longas.'''
d = float(input('Digite qual a distância que você deseja percorrer em km? '))
if d <=200:
    preco = d * 0.5
else:
    preco = d * 0.45
print(f'Sua viagem custará R${preco:.2f}')
