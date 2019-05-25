#coding=utf-8
import unittest
import os
class Run_Case(unittest.TestCase):
    def test_case1(self):
        case_path=os.path.join(os.getcwd(),'../case')
        print(case_path)
        sutit=unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(sutit)
if __name__ == '__main__':
    unittest.main()