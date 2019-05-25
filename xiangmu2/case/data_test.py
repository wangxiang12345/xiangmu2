#coding=utf-8
import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self) -> None:
         print('zhe')
    def tearDown(self) -> None:
        print('5544')

    @ddt.data(
        [1,2],
        [2,3],
        [3,4]
    )
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)
if __name__ == '__main__':
    unittest.main()
