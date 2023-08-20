from q_03 import is_numero_primo
import unittest

class TestNumeroPrimo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def testIsNumeroPrimo(self):
        primos = [7, 2, 13, 17, 199]
        for numero in primos:
            self.assertTrue(is_numero_primo(numero))

        naoprimos = [10, 20, 200]    
        for numero in naoprimos:
            self.assertFalse(is_numero_primo(numero))

        