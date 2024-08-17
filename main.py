from input_program import leitura, leituraCSV, arg_input

class AFN:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceita):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceita = estados_aceita

    def aceita(self, palavra_entrada):
        """
        Verifica se o autômato finito reconhece a palavra de entrada.
        """
        # Inicializa os estados atuais com o estado inicial
        estados_atuais = {self.estado_inicial}
        
        for simbolo in palavra_entrada:
            prox_estados = set()
            for estado in estados_atuais:
                # Busca os próximos estados se houver
                if (estado, simbolo) in self.transicoes:
                    prox_estados |= set(self.transicoes[(estado, simbolo)]) # União dos conjuntos
            estados_atuais = prox_estados
        
        # Verifica se algum dos estados atuais é um estado de aceitação
        return any(estado in self.estados_aceita for estado in estados_atuais)

def main():
    programa_path, palavras_csv_path = arg_input()
    
    estados, alfabeto, transicoes, estado_inicial, estados_finais = leitura(programa_path)

    nfa = AFN(estados, alfabeto, transicoes, estado_inicial, estados_finais)

    print(programa_path, palavras_csv_path)

    palavras = leituraCSV(palavras_csv_path)

    for palavra in palavras:
        print(palavra, ' ', nfa.aceita(palavra))

if __name__ == "__main__":
    main()