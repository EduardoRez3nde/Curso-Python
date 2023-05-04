tipos = input('Digite algo: ')
print(f'o tipo primitivo de {tipos} e: {type(tipos)}')
print(f'So tem espacos? {tipos.isspace()}')
print('E alfanumerico? ',tipos.isalnum())
print('E somente letras?' ,tipos.isalpha())


