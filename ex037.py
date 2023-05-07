'''Escreva um programa que leia a quantidade
de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.'''
d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))
d_em_s = d * 24 * 60 * 60
h_em_s = h * 60 * 60
m_em_s = m * 60
total_s = d_em_s + h_em_s + m_em_s + s
print(f'O total de segundos é {total_s}')
