cidade = str(input('Em que cidade você nasceu? ').strip())
teste = cidade.upper().split()
resultado = 'SANTO' in teste[0]
print(f'Começa com SANTO? ', resultado)