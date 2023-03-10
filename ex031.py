distancia = float(input('Qual vai ser a distância de sua viagem ? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km.')
if distancia <= 200:
    valor = distancia * 0.5
    print(f'Sua viagem irá custar R${valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'Sua viagem irá custar R${valor:.2f}')
