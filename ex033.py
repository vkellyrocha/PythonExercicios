n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 :
    if n1 > n3:
       if n2 > n3 :
           print(f'O maior número é {n1}  e o menor é {n3}')
       else:
           print(f'O maior número é {n1} e o menor é {n2}')
    else:
        print(f'O maior número é {n3} e o menor é {n2}')
else:
    if n1 > n3 :
        print(f'O maior número é {n2} e o menor é {n3}')
    else:
        if n2 > n3:
            print(f'O maior número é {n2} e o menor é {n1}')
        else:
            print(f'O maior número é {n3} e o menor é {n1}')
