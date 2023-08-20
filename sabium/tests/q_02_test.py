from q_02 import month_intTostr
import unittest



class TestMonth(unittest.TestCase):
    '''
    testCase para o método month_intTostr
    '''
    def testJaneiro(self):
        self.mes_ = month_intTostr(1)
        self.assertEqual(self.mes_, 'Janeiro')



