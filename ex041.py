'''Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular a soma (+), subtração (-), mul[plicação (*) e divisão (/).
Exiba o resultado da operação solicitada.'''
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
print('Digite: \n1 para soma (+)\n2 para subtração (-) \n3 para multiplicação (*)\nE 4 para divisão (/).')
op = float(input())
if op == 1:
    r = n1 + n2
    print(r)
elif op == 2:
    r = n1 - n2
    print(r)
elif op == 3:
    r = n1 * n2
    print(r)
elif op == 4:
    r = n1 / n2
    print(r)
else:
    print('Valor inválido!')
    print('Digite um valor entre 1 e 5.')