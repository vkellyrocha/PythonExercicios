d = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km percorridos? '))
p = 60*d + 0.15*km
print(f'Total a pagar R${p:.2f}')
