#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
try:
 numero = int(input('Digite um numero:'))
 numero2 = int(input('Digite outro numero:'))
 numero3 = int(input('Digite ainda um terceiro numero:'))
 maior = int()
 menor = int()

 if numero > numero2 > numero3:
    print(f'O numero menor é: {numero3} e o numero maior é: {numero}')
 elif numero2 > numero3 > numero:
    print(f'O numero menor é: {numero} e o numero maior é: {numero2}')
 elif numero3 > numero > numero2:
    print(f'O numero menor é: {numero2} e o numero maior é: {numero3}')
 elif numero == numero2 == numero:
    print('Os numeros sao iguais.')
 elif numero < 0 and numero2 < 0 and numero3 <0:
     print('Numeros negativos nao sao validos.')
except ValueError:
    print ('Entrada inválida.')
