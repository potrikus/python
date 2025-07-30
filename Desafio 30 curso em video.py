#Crie um programa que leia um numero qualquer e mostre se ele é par ou impar.


try:
    numero = int(input('Escolha um numero: ').strip())
    resultado = numero % 2
    if resultado == 0:
        print(f'O numero:{numero} é par! ')
    else:
        print(f'O numero: {numero} é impar!')
except ValueError:
        print ('Entrada invalida!')
