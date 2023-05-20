from modulos.interface import *
from modulos.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arq_existe(arq):
    criar_arq(arq)
while True:
    cabecalho('MENU PRINCIPAL')
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas','Sair do Sitema'])
    if resposta == 1:
        ler_arq(arq)
        sleep(0.5)
    elif resposta == 2:
        cabecalho('NOV0 CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(0.5)
    elif resposta == 3:
        cabecalho('SAINDO DO SISTEMA...ATÉ LOGO!')
        sleep(1)
        break
    else:
        print('\033[31mERRO: Digite um opção válida! \033[m')
        sleep(1)
