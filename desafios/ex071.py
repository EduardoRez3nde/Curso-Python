print('='*30)
print('       LOJAS DO BARATINHO')
print('='*30)
total = mais = cont = item = menor = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if preco >= 1000:
        mais += 1
    if cont == 1:
        item = produto
        menor = preco
    else:
        if preco < menor:
            item = produto
            menor = preco
    if resp == 'N':
        break
print('======== FIM DO PROGRAMA ========')
print(f'Total da Compra: R${total:.2f}')
print(f'Temos {mais} produtos custando mais de R$1000')
print(f'O produto mais barato foi {item} que custa R${menor:.2f}')
