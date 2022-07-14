def leiaint(a):
    """Leitor de um número inteiro com tratamento de erros"""
    try:
        n = int(input(a))
    except (ValueError, TypeError):
        print('\033[0;31mErro! Digite um número válido.\033[m')
    except(KeyboardInterrupt):
        print('\033[0;31mErro! Usuário não digitou um valor.\033[m') 
        return 0
    else:
        return n

def arquivoexiste(nome):
    """Verificador da existência do arquivo citado no programa principal"""
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    """Caso não exista o arquivo, esse programa cria o mesmo"""
    try:
        a= open(nome, 'wt+')
        a.close
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    """Programa que lê o arquivo no programa principal"""
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        print('-'*27)
        print('PESSOAS CADASTRADAS'.center(27))
        print('-'*27)
        print(a.read())
    finally:
        a.close()

def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    """Programa que escreve os dados tirados do programa principal no arquivo"""
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro com o arquivo')
    else:
        try:
            a.write(f'{nome:<10}  {idade:>10} anos\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} concluído')
            a.close()

