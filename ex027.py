nome = str(input('Digite seu nome completo: ')).strip()
nome_cortado = nome.split()
primeiro_nome = nome_cortado[0]
ultimo_nome = nome_cortado[nome.count(' ')]
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')
