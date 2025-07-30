#Escreva um programa que leia a velocidade de um carro.
#Se o carro ultrapassar 80 km por hora:
#Escreva que ele foi multado.
#Escreva o valor da multa que é R$ 7.00 para cada km exedido.

try:
   velocidade = int(input('''Voce passou por uma fiscaliçao eletronica!
   Qual velocidade do carro?:''').strip())
   if velocidade < 0:
       print('Valor invalido!')
   elif velocidade >80:
       multa = float(7.00)
       valor = (velocidade - 80) * multa
       print ('Voce foi multado! em: R$: {:.2f} '.format(valor))
   else:
       print('Voce nao foi multado!')

except ValueError:
    print ('Somente numeros!')


