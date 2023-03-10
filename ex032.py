from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 :
    if ano <= 400:
       print(f'O ano {ano} é um ano bissexto')
    else:
        if ano % 100 == 0:
           if ano % 400 == 0:
                print(f'O ano {ano} é um ano bissexto')
           else:
                print(f'O ano {ano} não é bissexto')
        else:
            print(f'O ano {ano} é um ano bissexto')
else:
    print(f'O ano {ano} não é bissexto')
