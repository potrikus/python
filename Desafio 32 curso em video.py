#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

try:
    ano = int(input('Digite um ano para saber se ele é Bisexto:'))
    if ano <0:
        print ('Entrada invalida!')
    elif ano % 4 == 0 and ano % 100 > 0 :
       print (f'O ano: {ano}  é Bissexto.')
    elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 > 0:
       print (f'O ano: {ano} não é Bissexto.')
    elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        print(f'O ano: {ano} é bissexto.')
    elif ano % 4 > 0:
       print (f'O ano: {ano} nao Bissexto')
except ValueError:
     print('Entrada invalida!')
