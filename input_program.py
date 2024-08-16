import sys

def ler_set_de_string(string_set):
    # Remove as chaves e espaços desnecessários
    string_set = string_set.strip('{} ')
    # Divide a string pelos elementos separados por vírgula
    elementos = string_set.split(',')
    # Remove aspas e espaços em cada elemento
    set_final = {elem.strip().strip("'\"") for elem in elementos}
    return set_final

def ler_tupla_de_string(string):
    # Remove os parênteses externos
    string = string.strip("()")
    # Divide a string pelo separador de vírgula
    elementos = string.split(',')
    # Remove espaços e aspas em cada elemento
    tupla = tuple(elem.strip().strip("'\"") for elem in elementos)
    return tupla

def ler_lista_de_string(string):
    # Remove os colchetes externos
    string = string.strip("{}")
    # Divide a string pelo separador de vírgula
    elementos = string.split(',')
    # Remove espaços e aspas em cada elemento
    lista = [elem.strip().strip("'\"") for elem in elementos]
    return lista

def remover_espacos(string):
    return string.replace(" ", "")

def ler_ate_C(string, C):
    if C in string:
        antes, depois = string.split(C, 1)  # Divide na primeira ocorrência de C
    else:
        antes = string
        depois = ""  # Se não encontrar o caractere, a parte "depois" fica vazia
    return antes, depois

def leitura():
    nomeEntrada = input('Entre o nome do arquivo de entrada: ')

    with open(nomeEntrada,'r') as arquivo:
        entrada = remover_espacos(arquivo.readline().strip())
        nome,entrada = ler_ate_C(entrada,'=')

        alfabeto, entrada = ler_ate_C(entrada,'}')
        alfabeto += '}'
        lixo , alfabeto = ler_ate_C(alfabeto,'(')
        lixo, entrada = ler_ate_C(entrada,',') 
        alfabeto = ler_set_de_string(alfabeto)


        estados, entrada = ler_ate_C(entrada,'}')
        estados += '}'
        lixo, entrada = ler_ate_C(entrada,',')
        estados = ler_set_de_string(estados)


        estado_inicial, entrada = ler_ate_C(entrada,',')

        entrada=entrada[:-1]
        estados_finais = ler_set_de_string(entrada)

        if  (arquivo.readline().strip() != 'Prog'):
            sys.exit(1)
            
        transicoes = {}

        while(True):
            entrada = arquivo.readline().strip()
            if not entrada:
                break

            chave, atingidos = ler_ate_C(entrada,'=')
            
            chave = ler_tupla_de_string(chave)

            atingidos = ler_lista_de_string(atingidos)

            transicoes[chave] = atingidos

        print(transicoes)

        return estados, alfabeto, transicoes, estado_inicial, estados_finais