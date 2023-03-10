nome = input('Qual é seu nome completo? ').strip()
resp = 'SILVA' in nome.upper().split()
print(f'Tem SILVA no seu nome? {resp}')
