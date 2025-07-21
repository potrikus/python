# Crie um programa que leia o nome completo de uma pessoa e escreva se tem ou nao SILVA no nome

nome = input("Nome completo:")
nomes = nome
nome = nome.lower()
silva = 'silva'
if silva in nome:
    print ('O nome:',nome,'tem: Silva!')
else:
    print ('O nome: ',nome,'não tem: Silva!')

