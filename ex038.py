'''defina o preço de um produto conforme sua categoria'''

categoria = int(input('Digita qual a categoria do seu produto: '))
if categoria == 1:
    print('O preço do produto é R$10.00')
else:
    if categoria == 2:
        print('O preço do produto é R$18.00')
    else:
        if categoria == 3:
            print('O preço do produto é R$23.00')
        else:
            if categoria == 4:
                print('O preço do produto é R$26.00')
            else:
                if categoria == 5:
                    print('O preço do produto é R$31.00')
                else:
                    print('Categoria inválida, digite um número entre 1 e 5')