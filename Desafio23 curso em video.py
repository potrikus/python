# faça um programa que leia um numero que vai de 0 a 9999.
# e mostre na tela cada um dos numeros separados em: unidade,dezena,centena e milhar.

         #ESTRUTURA DE REPETIÇAO, PARA ENTRADA INVALIDA:

while True:
    numero = input('Digite um numero de 0 a 9999:')
    try:
        numero = int(numero)
        if 0 <= numero <= 9999:

            break
        else:
         print('numero invalido')
    except ValueError:
         numero = str(numero)
         print('numero invalido')


         # MOSTRA OS NUMEROS INDENTIFICANDO SE SAO: UNIDADE,DEZENA,CENTENA OU MILHAR.

        
numero = str(numero)
indice = len(numero)
if indice == 1:
 print(numero[0],'é UNIDADE!')
if indice == 2:
 print (numero[0],'é DEZENA',numero[1],'é UNIDADE!')
if indice == 3:
 print(numero[0],'é CENTENA',numero[1],'é DEZENA',numero[2],'UNIDADE!')
if indice == 4:
 print(numero[0],'é MILHAR',numero[1],'é CENTENA',numero[2],'é DEZENA',numero[3],'é UNIDADE!')
