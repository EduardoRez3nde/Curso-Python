def leiadinheiro(msg):
    validar = False
    while not validar:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! "{entrada}" é um preço invalido!\033[m')
        else:
            validar = True
            return float(entrada)
