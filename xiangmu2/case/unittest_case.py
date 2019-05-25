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
    def testfrist01(self):
        print('这是第一条case')

    def testfrist02(self):
        print('这是第二条case')

    def testfrist03(self):
        print('这是第三条case')
# if __name__ == '__main__':
#     #unittest.main()
#     suite=unittest.TestSuite()
#     suite.addTest(FrigisterCase01('testfrist02'))
#     unittest.TextTestRunner.run(suite)
if __name__ == '__main__':
    #unittest.main()
    sutie=unittest.TestSuite()
    sutie.addTest(FrigisterCase01('testfrist01'))
    sutie.addTest(FrigisterCase01('testfrist03'))
    sutie.addTest(FrigisterCase01('testfrist02'))
    unittest.TextTestRunner().run(sutie)
