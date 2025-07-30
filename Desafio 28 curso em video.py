#Faça um programa que faça o computador pensar
#em um numero entre o e 5 o usuario devera tentar adivinhar
#o numero e escrever na tela se o usuario ganhou ou perdeu.
# se o usuario ganhar escreva 'Parabens voce venceu!'.
#se o usuario perder 'O computador venceu!'
import random

pontos = int()
pontoscpu = int()
while True:
 numero = [1, 2, 3, 4, 5]
 numero = random.choice(numero)

 try:
     entrada = int(input('Entre 1 e 5, que numero estou pensando?:'))
 except ValueError:
     print ('Somente numeros!')
     continue
 if  entrada < 1 or entrada > 5:
    print ('Somente numeros de 1 a 5!')

 elif entrada == numero:
    pontos = pontos + 1
    print ('Voce acertou!           CPU pontos: (',pontoscpu,') Seus pontos: (',pontos,')')
 else:
    pontoscpu = pontoscpu +1
    print('Tente novamente!         CPU pontos: (',pontoscpu,') seus pontos: (',pontos,')')
