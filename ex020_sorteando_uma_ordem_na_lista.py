from random import sample
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('aluno 4: ')
lista = [aluno1,aluno2,aluno3,aluno4]
ordem_de_apresentação = sample(lista, 4)
print('A ordem de apresentação será')
print(ordem_de_apresentação)