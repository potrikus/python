opçao = ''
while opçao != '1' and opçao != '2':
    print ('SEJA BEM VINDO PIZZARIA JOVAX!')
    opçao = input('Digite 1 para ir para o cardapio:').strip()
    if opçao == '1':
        
                        # Aqui começa janela de cardapio:
        finalizar = ''# '1'para pedido.
        cardapio = ['camarao','quatro queijos','peperone','frango']
        pedido = ['']
        while finalizar != '1':
            print ('         CARDAPIO DO DIA!')
            print ('')
            print ('Faça seu pedido e digite 1 para finalizar:')
            print ('')
            print ('Pizza de camarao: R$ 70.00')
            print ('Pizza de quatro queijos R$ 50.00')
            print ('Pizza de peperone R$ 50.00')
            print ('Pizza de frango R$ 50.00')
            pedido = input('Pizza de:').strip().lower()
            if pedido in cardapio:
                print ('                     ',pedido)
        
        
        
        
        
        
        
        
    elif opçao == '2':
        print ('FINALIZANDO SISTEMA!')
    else:
        print ('ENTRADA INVALIDA!')
