# programa que leia uma frase e mostre:
# 1 quantas vezes aparece a letra: a
# 2 em que posiçao ela aparece na primeira vez
# 3 em que posiçao ela aparece na ultima vez

frase = input('Digite uma frase: ')
frase = frase.lower()# Frase fica em letras minusculas.
nletras = frase.count('a')# Conta numeros de vezes que 'a' aparece.
posiçao =frase.find('a')# Acha no inicio da frase.
posiçaof = frase.rfind('a')# Acha no fim da frase.


if nletras == 0:# mostra quantidade de A na frase, com condiçao caso nao exista.
    print ('Não existe letra A na frase!')
else:
    print ('1 A frase',frase,'contem:',nletras,' letra A.')
    print ('2 : Aparece na posiçao:',posiçao,'pela primeira vez.')
    print ('3 : Aparece na posiçao:',posiçaof,'pela ultima vez.')
