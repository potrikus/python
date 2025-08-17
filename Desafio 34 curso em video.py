#Faça um programa que leia o salario de um funcionario e calcule seu almento.
#Para salario de R$ 1.250 o reajuste sera de 10%.
#Para inferiores o reajuste sera de 15%.
try:
 salario = float(input('Salario R$:').strip())

 if salario >= 1250:
    print (f'O reajuste do sarario de R$ {salario:.2f} é de R$ {salario/100*10+salario:.2f}')
 elif salario <= 0:
    print('Valor nao pode ser 0 ou negativo!')
 else:
    print (f'O reajuste do salario de R$ {salario:.2f} é de R$ {salario/100*15+salario:.2f}')

except ValueError:
    print('Entrada invalida.')
