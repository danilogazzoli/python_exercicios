import sys
import os
directory = os.path.dirname(os.path.abspath('__file__'))
sys.path.append(os.path.dirname(directory))
import q_01 
import unittest

class TestObesidade(unittest.TestCase):
  
    @classmethod
    def setUpClass(cls): ### run once before all test cases ###
        pass
  
    @classmethod
    def tearDownClass(cls): ### run once after all test cases ###
        pass
  
    def setUp(self): ### run before each test case ###
        pass
  
    def tearDown(self): ### run after each test case ###
        pass
  
    ### make sure to add => test_ <= as prefix to all test cases otherwise they won't work ###
    def test_resultado_normal(self):
        '''Função de teste para verificar o resultado do imc'''
        self.obesidade = q_01.Obesidade(90, 1.9)
        expected = ['Normal', 25]
        self.assertEqual(self.obesidade.resultado[0], expected[0])
        self.assertLessEqual(self.obesidade.resultado[1], expected[1])

    #@unittest.skip('Some reason')
    def test_resultado_obeso(self):
        '''Função de teste para verificar o resultado do imc'''
        self.obesidade = q_01.Obesidade(100, 1.9)
        expected = ['Obeso', 26, 30]
        self.assertEqual(self.obesidade.resultado[0], expected[0])
        self.assertGreater(self.obesidade.resultado[1], expected[1])
        self.assertLess(self.obesidade.resultado[1], expected[2], 'teste de mensagem')

    def test_resultado_morbido(self):
        '''Função de teste para verificar o resultado do imc'''
        self.obesidade = q_01.Obesidade(120, 1.9)
        expected = ['Obeso mórbido', 30]
        self.assertEqual(self.obesidade.resultado[0], expected[0])
        self.assertGreater(self.obesidade.resultado[1], expected[1])

if __name__ == '__main__':
    unittest.main()