import unittest
from main import AF, leitura
from conversao import afn_para_afd

class TesteAFD(unittest.TestCase):
    def setUp(self):
        alfabeto, estados, transicoes, estado_inicial, estados_finais = leitura(prog_path="entrada")

        self.afn = AF(alfabeto=alfabeto,
                    estados=estados, 
                    transicoes=transicoes, 
                    estado_inicial=estado_inicial, 
                    estados_aceita=estados_finais
                    )
        self.afd = afn_para_afd(self.afn)
        
    def teste_aceita(self):
        self.assertTrue(self.afd.aceita("S:c"))
        self.assertTrue(self.afd.aceita("S://u@h:pc?q#f"))

    def teste_rejeita(self):
        self.assertFalse(self.afd.aceita("S://u@h:p"))

if __name__ == '__main__':
    unittest.main()