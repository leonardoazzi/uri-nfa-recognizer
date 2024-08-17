import sys, getopt, re

def arg_input() -> tuple:
    """
    Analisa os argumentos do terminal e retorna o caminho do programa e da lista de palavras CSV.

    Retorna:
        tuple: Uma tupla contendo o caminho do programa e o caminho do arquivo CSV.

    Lança:
        Exception: Se houver um erro ao analisar os argumentos da linha de comando.
    """
    # Entrada de parâmetros via terminal
    argument_list = sys.argv[1:]

    options = "p:c:"

    long_options = ["programa=", "csv_palavras="]

    prog_path = ""
    csv_path = ""

    ## Parsing dos argumentos e valores atribuídos
    try:
        arguments, values = getopt.getopt(argument_list, options, long_options)
        print(arguments, values)

    except getopt.error as err:
        print(str(err))
        raise Exception("Desculpe, nenhum número abaixo de zero")  

    # Verifica os argumentos
    for current_argument, current_value in arguments:

        if current_argument in ("-p", "--programa"):
            prog_path = current_value
            print("Arquivo de programa:", prog_path)

        elif current_argument in ("-c", "--csv_palavras"):
            if (re.search(r'\.csv$', current_value)):
                print("Arquivo .csv de Palavras:", current_value)
            else:
                raise Exception("O arquivo de palavras deve ser um arquivo .csv")
            
            csv_path = current_value

    return prog_path, csv_path

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

def leitura(prog_path):
    with open(prog_path,'r') as arquivo:
        entrada = remover_espacos(arquivo.readline().strip())
        _,entrada = ler_ate_C(entrada,'=')

        alfabeto, entrada = ler_ate_C(entrada,'}')
        alfabeto += '}'
        _ , alfabeto = ler_ate_C(alfabeto,'(')
        _, entrada = ler_ate_C(entrada,',') 
        alfabeto = ler_set_de_string(alfabeto)


        estados, entrada = ler_ate_C(entrada,'}')
        estados += '}'
        _, entrada = ler_ate_C(entrada,',')
        estados = ler_set_de_string(estados)

        estado_inicial, entrada = ler_ate_C(entrada,',')

        entrada=entrada[:-1]
        estados_finais = ler_set_de_string(entrada)

        if (arquivo.readline().strip() != 'Prog'):
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

        return estados, alfabeto, transicoes, estado_inicial, estados_finais

def leituraCSV(csv_path):
    with open(csv_path, 'r') as arquivo:
        conteudo = arquivo.read().strip()  # Lê o arquivo inteiro e remove espaços em branco extras
        return tuple(conteudo.split(','))  # Divide as strings por vírgula e transforma em tupla
