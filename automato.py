
class AF:
    def __init__(self, alfabeto: set, estados: set, transicoes: dict, estado_inicial: str, estados_aceita: set):
        """
        Cria um autômato finito.

        Parâmetros:
        - alfabeto: lista de símbolos do alfabeto do autômato.
        - estados: lista de estados do autômato.
        - transicoes: dicionário contendo as transições do autômato.
        - estado_inicial: estado inicial do autômato.
        - estados_aceita: lista de estados de aceitação do autômato.
        """
        self.alfabeto = alfabeto
        self.estados = estados
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceita = estados_aceita

    def aceita(self, palavra_entrada: str) -> bool:
        """
        Verifica se o autômato finito reconhece a palavra de entrada.

        Parâmetros:
        - palavra_entrada (bool): palavra a ser verificada.

        Retorna:
        - True se a palavra de entrada está no conjunto ACEITA do autômato, False caso contrário.
        """
        self.estados = frozenset(self.estados)
        estado_inicial = frozenset([self.estado_inicial])
        
        # Inicializa os estados atuais com o estado inicial
        estados_atuais = {estado_inicial}
        
        for simbolo in palavra_entrada:
            prox_estados = set()
            for estado in estados_atuais:
                # Busca os próximos estados se houver
                if (frozenset(estado), simbolo) in self.transicoes:
                    prox_estados |= frozenset(self.transicoes[(estado, simbolo)]) # União dos conjuntos
                    prox_estados = frozenset(prox_estados)
            estados_atuais = {prox_estados}
        
        # Verifica se algum dos estados atuais é um estado de aceitação
        return prox_estados in self.estados_aceita