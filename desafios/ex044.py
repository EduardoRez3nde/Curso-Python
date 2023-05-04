produto = float(input('Preço Produto: R$'))
print('CONDIÇÃO DE PAGAMENTO')
condicao = int(input('1 A vista\n2 A vista cartão\n3 2x no cartão\n4 3x ou mais cartão'))
if condicao == 1:
    avista = produto * 10 / 100
    print('=-' * 20)
    print('A VISTA:')
    print(f'O valor com 10% de desconto. Total a Pagar: R${produto-avista}')
    print('=-' * 20)
elif condicao == 2:
    avista_cart = produto * 5 / 100
    print('=-'*20)
    print('A VISTA NO CARTÃO:')
    print(f'O valor com 5% de desconto.\nTotal a Pagar: R${produto-avista_cart} ')
    print('=-' * 20)
elif condicao == 3:
    print('=-' * 20)
    print('2X NO CARTÃO:')
    print(f'O valor não produto não tem desconto\ncom essa forma de pagamento Total a Pagar: R${produto}')
    print('=-' * 20)
elif condicao == 4:
    juros = produto * 20 / 100
    print('=-' * 20)
    print('3X OU MAIS NO CARTÃO:')
    print(f'Nessa forma de pagamento,\no produto tem um acrescimo de 20%. Total a Pagar: {produto+juros}')
    print('=-' * 20)
