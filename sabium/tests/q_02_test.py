import os
import sys
current_dir = os.path.dirname(os.path.abspath('__file__'))
sys.path.append(os.path.dirname(current_dir))
import q_02
import unittest



class TestMonth(unittest.TestCase):
    '''
    testCase para o método month_intTostr
    '''
    def testJaneiro(self):
        self.mes_ = q_02. month_intTostr(1)
        self.assertEqual(self.mes_, 'Janeiro')


if __name__ == '__main__':
    unittest.main()


