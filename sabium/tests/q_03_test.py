import sys
import os
#cur_dir = os.path.dirname(os.path.abspath('__file__'))
#sys.path.append(os.path.dirname(cur_dir))
sys.path.append('..')
import q_03
import unittest

class TestNumeroPrimo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def testIsNumeroPrimo(self):
        primos = [7, 2, 13, 17, 199]
        for numero in primos:
            self.assertTrue(q_03.is_numero_primo(numero))

        naoprimos = [10, 20, 200]    
        for numero in naoprimos:
            self.assertFalse(q_03.is_numero_primo(numero))

if __name__ == '__main__':
    unittest.main()