from cadastro import *
from time import sleep

#Leitor de arquivo com dados do cadastro
arq = 'cursomemvideo.txt'
if arquivoexiste(arq):
    print('\nArquivo encontrado com sucesso!\n')
else:
    print('\nArquivo não encontrado.\n')
    criararquivo(arq)
#Leitor de arquivo com dados do cadastro
    
#Programa principal de execução
while True:
    print('-'*27)
    print('MENU PRINCIPAL'.center(27))
    print('-'*27)
    print('''
\033[0;33m1-\033[m \033[0;36mVer pessoas cadastradas;\033[m
\033[0;33m2-\033[m \033[0;36mCadastrar nova pessoa;\033[m
\033[0;33m3-\033[m \033[0;36mEncerrar operação.\033[m
---------------------------''')
    try:
        opc = int(input('\n\033[0;33mQual a sua opção? ->\033[m '))
        sleep(0.5)
        if opc == 1:
            sleep(0.3)
            lerarquivo(arq)
            sleep(2.0)
        elif opc == 2:
            sleep(0.3)
            print('-'*27)
            print('NOVO CADASTRO'.center(27))
            print('-'*27)
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            cadastrar(arq, nome, idade)
            sleep(0.3)
        elif opc == 3:
            print('-'*22)
            print('OPERAÇÃO FINALIZADA'.center(22))
            print('-'*22)
            break
        else:
            sleep(0.3)
            print('\033[0;31mErro! Digite uma opção válida.\033[m')
            sleep(0.3)
    except (ValueError, TypeError):
        sleep(0.3)
        print('\033[0;31mErro! Digite uma opção válida.\033[m')
        sleep(0.5)
        continue
    except(KeyboardInterrupt):
        sleep(0.3)
        print('\033[0;31mErro! Usuário não digitou um valor.\033[m') 
        sleep(0.5)  
    else:
        continue
#Programa principal de execução