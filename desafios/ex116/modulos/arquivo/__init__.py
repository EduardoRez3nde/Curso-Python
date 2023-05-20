def linha(tam=40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do aquivo.')
    else:
        print(f'arquivo {nome} criado com sucesso.')


def ler_arq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for p in a:
            dados = p.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close()


# CADASTRAR PESSOAS

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro n abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo Registro de {nome} adicionado!')
            a.close()

