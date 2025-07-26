#JANELA INICIAL DE MENU:

print ('Seja bem vindo a pizzaria Jovax!')
print ('MENU:')
print ('1: Cardapio.')
print ('2: Sair.')
cardapio = input()

#JANELA DE CARDAPIO:
if cardapio =='1':
    print('Cardapio:')
    print ('Pizza quatro queijos:R$ 50,00')
    print ('Pizza peperone:R$ 50,00')
    print ('Pizza camarao:R$ 70,00')
    print ('Pizza portugueza:R$ 50,00')
    
    sabores = ['quatro queijos','peperone','camarao','portuguesa']
    pedido = input('Digite seu pedido:')
    pedido = pedido.lower()
    sabores_escolhidos = []
    valor = []
    if pedido == sabores[2]:
         valor = ('70.00')
    else:
         valor = ('50.00')
    if pedido in sabores:
         sabores_escolhidos = pedido
         print ('Pedido:'sabores_escolhidos)
         
    else:
        print ('entrada invalida!')
