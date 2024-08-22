# UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL
# INSTITUTO DE INFORMÁTICA
# INF05005 - Linguagens Formais e Autômatos - Prof. Lucio Mauro Duarte

# Trabalho teórico-prático, 2024/1

# Dennis Pereira Krigger
# Leonardo Azzi Martins

from automato import AF

def afn_para_afd(afn: AF) -> AF:
    """
    Converte um autômato finito não-determinístico (AFN) em um autômato finito determinístico (AFD)
    através do algoritmo de determinização.

    Parâmetros:
    - afn: O autômato finito não-determinístico (AFN) a ser convertido.

    Retorna:
    - O autômato finito determinístico (AFD) resultante da conversão.

    """

    # Inicializa um AFD com o estado inicial do AFN
    afd = AF(afn.alfabeto, set(), dict(), afn.estado_inicial, set())
    afd.estados.add(afn.estado_inicial)

    # O frozenset é um conjunto imutável, que pode ser usado como chave de dicionário
    estados_nao_processados = [frozenset([afd.estado_inicial])]
    estados_processados = set()

    # Busca estados ainda não processados, enquanto houver
    while estados_nao_processados:
        estado_atual = estados_nao_processados.pop()
        estados_processados.add(estado_atual)

        # Verifica se o estado atual contém um estado de aceitação do AFN,
        # mesmo estados agrupados pela determinização em um frozenset
        if any(estado in afn.estados_aceita for estado in estado_atual):
            afd.estados_aceita.add(estado_atual)

        for simbolo in afd.alfabeto:
            estados_atingidos = set()

            for estado in estado_atual:
                # Faz a união dos estados atingidos pela transição atual
                estados_atingidos.update(afn.transicoes.get((estado, simbolo), set()))

            # Cria um novo estado com a união dos estados atingidos
            novo_estado = frozenset(estados_atingidos)

            # Se o novo_estado não foi processado, adiciona à lista de estados não processados
            if novo_estado and novo_estado not in estados_processados:
                estados_nao_processados.append(novo_estado)

            if novo_estado:
                afd.estados.add(novo_estado) # Adiciona o novo estado ao AFD
                # Adiciona ao AFD a transição do estado atual para o novo estado
                afd.transicoes[(estado_atual, simbolo)] = novo_estado

    return afd