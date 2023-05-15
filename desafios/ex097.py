def area(largura, comprimento):
    tamanho = largura * comprimento
    print(f'A área de um terreno {largura:.2f}x{comprimento:.2f} é de {tamanho:.2f}m².')


# area(float(input('Largura (m): ')), comprimento=float(input('Comprimento (m): ')))
print('Controle de Terrenos')
print('-'*30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
