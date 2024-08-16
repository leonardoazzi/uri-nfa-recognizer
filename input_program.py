import sys

class AFN:
    def __init__(self,nome,alfabeto,estados,estado_inicial,estados_finais, transicoes):
        self.nome = nome
        self.alfabeto = alfabeto
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def processar_entrada(self, entrada):
        return self._processar_entrada_recursivo(self.estado_inicial, entrada)

    def _processar_entrada_recursivo(self, estado_atual, entrada):
        if not entrada:  # Se a entrada acabou
            return estado_atual in self.estados_finais
        
        simbolo = entrada[0]
        resto_entrada = entrada[1:]
        
        proximos_estados = self.transicoes.get((estado_atual, simbolo), [])
        
        for proximo_estado in proximos_estados:
            if self._processar_entrada_recursivo(proximo_estado, resto_entrada):
                return True  # Se qualquer um dos caminhos levar a um estado final, a entrada é aceita
        
        return False  # Se nenhum dos caminhos levar a um estado final, a entrada é rejeitada



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
# Exemplo de uso
    
entrada = remover_espacos(input())
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

# if  (input() != 'Prog'):
# 	sys.exit(1)
     
transicoes = {}

while(True):
    entrada = input()
    if entrada == "":
         break

    chave, atingidos = ler_ate_C(entrada,'=')
	
    chave = ler_tupla_de_string(chave)

    atingidos = ler_lista_de_string(atingidos)

    transicoes[chave] = atingidos

print(transicoes)
    

afn = AFN(estados, alfabeto, transicoes, estado_inicial, estados_finais,transicoes)

# Testando o autômato com uma entrada
palavra = "ab"
if afn.processar_entrada(palavra):
    print(f"A entrada '{palavra}' foi aceita pelo AFN.")
else:
    print(f"A entrada '{palavra}' foi rejeitada pelo AFN.")