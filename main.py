from input_program import leitura

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
    estados, alfabeto, transicoes, estado_inicial, estados_finais = leitura()

    nfa = AFN(estados, alfabeto, transicoes, estado_inicial, estados_finais)

    # Teste
    print(nfa.aceita("S:c"))  # True
    print(nfa.aceita("S://u@h:pc?q#f"))  # True
    print(nfa.aceita("S://u@h:p"))  # False

if __name__ == "__main__":
    main()