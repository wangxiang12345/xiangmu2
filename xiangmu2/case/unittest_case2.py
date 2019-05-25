#coding=utf-8
import unittest
class FrigisterCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之前的后置')

    def setUp(self):
        print('这个是case的前置条件')

    def tearDown(self):
        print('这个是case的后置条件')

    @unittest.skip('不执行第一条')
    def testfrist04(self):
        print('这是第四条case')

    def testfrist05(self):
        print('这是第五条case')

    def testfrist06(self):
        print('这是第六条case')
# if __name__ == '__main__':
#     #unittest.main()
#     suite=unittest.TestSuite()
#     suite.addTest(FrigisterCase01('testfrist02'))
#     unittest.TextTestRunner.run(suite)
if __name__ == '__main__':
    #unittest.main()
    sutie=unittest.TestSuite()
    sutie.addTest(FrigisterCase01('testfrist04'))
    sutie.addTest(FrigisterCase01('testfrist05'))
    sutie.addTest(FrigisterCase01('testfrist06'))
    unittest.TextTestRunner().run(sutie)