import unittest
from main import AFN, leitura

class TesteAFN(unittest.TestCase):
    def setUp(self):
        estados, alfabeto, transicoes, estado_inicial, estados_finais = leitura()
        self.nfa = AFN(estados, alfabeto, transicoes, estado_inicial, estados_finais)

    def teste_aceita(self):
        self.assertTrue(self.nfa.aceita("S:c"))
        self.assertTrue(self.nfa.aceita("S://u@h:pc?q#f"))

    def teste_rejeita(self):
        self.assertFalse(self.nfa.aceita("S://u@h:p"))

if __name__ == '__main__':
    unittest.main()