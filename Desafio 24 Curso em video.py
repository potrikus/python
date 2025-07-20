# programa que leia o nome de uma cidade e mostre se começa ou nao com a palavra SANTO.

cidade = input('Digite o nome de cidade:')
cidade = cidade.lower()# Converte as letras para minusculas.
cidade = cidade.capitalize()#Converte as primeiras letras das palavras para maiuscula.
cidades = cidade
cidade = cidade.split()# Separa as palavras em lista.
santo = 'Santo'


if santo == cidade[0]:
    print(cidades,'começa com:',santo)
else:
 print ('Nao começa com:',santo)


