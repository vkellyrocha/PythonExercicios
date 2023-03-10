from math import hypot
cateto_o = float(input('Digite o comprimento do cateto oposto: '))
cateto_a = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_o, cateto_a)
print(f'O comprimento da hipotenusa vale {hipotenusa:.2f}')