from random import choice
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('aluno 3: ')
aluno4 = input('Aluno 4: ')

'''Para criar uma lista, coloque: lista = [n1, n2, n3, n4]'''

escolhido = choice([aluno1, aluno2, aluno3, aluno4])
print(f'Aluno escolhido: {escolhido}')