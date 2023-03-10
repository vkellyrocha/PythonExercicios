salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250 :
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15
print(f'Quem ganhava R${salario} passa a ganhar R${novo_salario:.2f} agora.')
