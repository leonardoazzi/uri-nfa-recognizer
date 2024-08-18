# UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL
# INSTITUTO DE INFORMÁTICA
# INF05005 - Linguagens Formais e Autômatos - Prof. Lucio Mauro Duarte

# Trabalho teórico-prático, 2024/1

# Dennis Pereira Krigger
# Leonardo Azzi Martins

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

    options = "p:c:rl"

    long_options = ["programa=", "csv_palavras=", "rejeita", "lista"]

    prog_path = ""
    csv_path = ""
    arg_rejeita = False
    arg_lista = False

    ## Parsing dos argumentos e valores atribuídos
    try:
        arguments, values = getopt.getopt(argument_list, options, long_options)

    except getopt.error as err:
        print(str(err))
        raise Exception("Desculpe, nenhum número abaixo de zero")  

    # Verifica os argumentos
    for current_argument, current_value in arguments:

        if current_argument in ("-p", "--programa"):
            prog_path = current_value
            print("\nArquivo de programa:", prog_path)

        elif current_argument in ("-c", "--csv_palavras"):
            if (re.search(r'\.csv$', current_value)):
                print("Arquivo .csv de Palavras:", current_value)
            else:
                raise Exception("O arquivo de palavras deve ser um arquivo .csv")
            csv_path = current_value

        elif current_argument in ("-r", "--rejeita"):
            arg_rejeita = True

        elif current_argument in ("-l", "--lista"):
            arg_lista = True

    return prog_path, csv_path, arg_rejeita, arg_lista

def ler_set_de_string(string_set: str) -> set:
    """
    Converte uma string contendo um conjunto de elementos separados por vírgula em um set.

    Args:
        string_set (str): A string contendo o conjunto de elementos separados por vírgula.

    Retorna:
        set: O conjunto contendo os elementos da string.

    Exemplo:
        >>> ler_set_de_string('{1, 2, 3}')
        {1, 2, 3}
    """
    # Remove as chaves e espaços desnecessários
    string_set = string_set.strip('{} ')
    # Divide a string pelos elementos separados por vírgula
    elementos = string_set.split(',')
    # Remove aspas e espaços em cada elemento
    set_final = {elem.strip().strip("'\"") for elem in elementos}
    return set_final

def ler_tupla_de_string(string: str) -> tuple:
    """
    Converte uma string representando uma tupla em uma tupla de elementos.

    Args:
        string (str): A string representando a tupla.

    Retorna:
        tuple: Uma tupla de elementos.

    Exemplo:
        >>> ler_tupla_de_string("(1, 2, 3)")
        (1, 2, 3)
    """
    # Remove os parênteses externos
    string = string.strip("()")
    # Divide a string pelo separador de vírgula
    elementos = string.split(',')
    # Remove espaços e aspas em cada elemento
    tupla = tuple(elem.strip().strip("'\"") for elem in elementos)
    return tupla

def ler_lista_de_string(string: str) -> list:
    """
    Função que recebe uma string contendo uma lista de strings e retorna uma lista de strings.

    Parâmetros:
    string (str): A string contendo a lista de strings.

    Retorna:
    list: Uma lista de strings.

    Exemplo:
    >>> ler_lista_de_string("['string1', 'string2', 'string3']")
    ['string1', 'string2', 'string3']
    """
    # Remove os colchetes externos
    string = string.strip("{}")
    # Divide a string pelo separador de vírgula
    elementos = string.split(',')
    # Remove espaços e aspas em cada elemento
    lista = [elem.strip().strip("'\"") for elem in elementos]
    return lista

def remover_espacos(string:str) -> str:
    """
    Remove os espaços em branco de uma string.

    Args:
        string (str): A string da qual os espaços em branco serão removidos.

    Returns:
        str: A string resultante após a remoção dos espaços em branco.
    """
    return string.replace(" ", "")

def ler_ate_C(string: str, C: str) -> tuple:
    """
    Retorna uma tupla contendo duas strings: a parte da string original antes da primeira ocorrência do caractere C
    e a parte da string original depois da primeira ocorrência do caractere C. Se o caractere C não for encontrado,
    a parte "depois" será uma string vazia.

    Parâmetros:
    - string: A string original a ser dividida.
    - C: O caractere a ser procurado na string.

    Retorno:
    - Uma tupla contendo duas strings: a parte da string original antes da primeira ocorrência do caractere C
    e a parte da string original depois da primeira ocorrência do caractere C.
    """
    if C in string:
        antes, depois = string.split(C, 1)  # Divide na primeira ocorrência de C
    else:
        antes = string
        depois = ""  # Se não encontrar o caractere, a parte "depois" fica vazia
    return antes, depois

def leitura(prog_path: str) -> tuple:
    """
    Lê um arquivo de programa e retorna as informações necessárias.

    Args:
        prog_path (str): O caminho do arquivo de programa.

    Retorna:
        tuple: Uma tupla contendo as seguintes informações:
            - alfabeto (str): O alfabeto do autômato.
            - estados (set): O conjunto de estados do autômato.
            - transicoes (dict): O dicionário de transições do autômato.
            - estado_inicial (str): O estado inicial do autômato.
            - estados_finais (set): O conjunto de estados finais do autômato.
    """
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

        return alfabeto, estados, transicoes, estado_inicial, estados_finais

def leituraCSV(csv_path: str) -> tuple:
    """
    Lê um arquivo CSV e retorna seu conteúdo como uma tupla.

    Parâmetros:
    csv_path (str): O caminho do arquivo CSV a ser lido.

    Retorna:
    tuple: Uma tupla contendo as strings do arquivo CSV, divididas por vírgula.

    Exemplo:
    >>> leituraCSV('/caminho/do/arquivo.csv')
    ('valor1', 'valor2', 'valor3')
    """
    with open(csv_path, 'r') as arquivo:
        conteudo = arquivo.read().strip()  # Lê o arquivo inteiro e remove espaços em branco extras
        return tuple(conteudo.split(','))  # Divide as strings por vírgula e transforma em tupla
