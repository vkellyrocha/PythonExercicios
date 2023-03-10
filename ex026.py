nome = str(input('Digite uma frase: ')).strip()
contagem = nome.lower().count('a')
primeiro_a = int(nome.lower().find('a')) + 1
ultimo_a = int(nome.lower().rfind('a')) + 1
print(f'No nome {nome} aparece {contagem} vezes a letra a')
print(f'A letra A aparece pela primeira vez na posição {primeiro_a}')
print(f'A letra A aparce pela última vez na posição {ultimo_a}')
