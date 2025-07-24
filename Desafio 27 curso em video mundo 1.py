# programa que leia nome completo de uma pessoa e mostre primeiro e ultimo nome.

nome = input('Nome:  ')
nomes = nome# Guarda entrada original.
nome = nome.split()# Transforma nome completo em lista


print ('O primeiro nome de:',nomes.title(),'é:',nome[0],'e o ultimo é:',nome[-1])
