from random import randint
from time import sleep
numero = randint(0,5)
print('-=-'*40)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*40)
n = int(input(('Em que número eu pensei? ')))
print('Processando...')
sleep(2)
if n == numero:
    print('Parabéns! você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {numero} e não no {n}!')
