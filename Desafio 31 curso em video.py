#Desenvolva um programa que pergunte a distancia de uma viagem em km,
#calcule o preço da passagem em km sendo R$ 0.50 ate 200 km e R$ 0.45 para viagens acima 200 km.

try:
    distancia = float(input('Quantos km deseja viajar:'))
    if distancia <= 0:
        print('Entrada invalida!')
    elif distancia >= 1 and  distancia <=200:
      print (f'O valor da viagem sera de R$ {distancia * .50:.2f}')
    elif distancia > 200:
      print (f'O valor da viagem é de R$ {distancia * .45:.2f}')
except ValueError:
      print ('Entrada invalida!')
