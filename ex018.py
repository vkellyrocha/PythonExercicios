from math import sin,cos,tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de{angulo} tem a TANGENTE de {tangente:.2f}')
