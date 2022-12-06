import unittest

"""
    a. @unittest.skip()，加在方法上可跳过该测试用例
    b. @unittest.skipIf(条件，'理由')，满足条件后跳过该测试用例
    c. @unittest.skipUnless(条件，'理由')，结果为false跳过该测试用例
    d.他们三个也可以加在模块上，整个跳过不执行
"""


class UnittestSkipStudy(unittest.TestCase):
    age = 22

    @unittest.skip('就是忽略')
    def test_01_skip(self):
        print('这是第一个测试方法')

    @unittest.skipIf(age > 20, 'age大于20就忽略')
    def test_02_skip(self):
        print('这是第二个测试方法')

    @unittest.skipUnless(age < 18, '结果为false就忽略')
    def test_03_skip(self):
        print('这是第三个测试方法')


@unittest.skip('整个模块忽略')
class TestStudy(unittest.TestCase):
    def test_01_skip(self):
        print('这是第四个测试方法')

    def test_02_skip(self):
        print('这是第五个测试方法')


if __name__ == '__main__':
    unittest.main()
