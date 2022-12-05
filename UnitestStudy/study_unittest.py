import os
import unittest


class StudyUnittest(unittest.TestCase):
    def test_01_method(self):
        print('这是01方法')

    def test_02_method(self):
        print('这是02方法')

    def test_03_method(self):
        print('这是03方法')


if __name__ == '__main__':
    # 要想只执行添加到suite里的测试用例，需要注意右上角的执行环境，unittest***表示执行所有用例，需自己创建一个执行环境
    # https://zhuanlan.zhihu.com/p/97131025

    suite = unittest.TestSuite()
    # 一个一个测试用例添加
    # suite.addTest(StudyUnittest("test_02_method"))
    # suite.addTest(StudyUnittest("test_01_method"))
    # unittest.TextTestRunner().run(suite)

    # 批量添加用例，可以指定路径
    testcases = unittest.TestLoader().discover(os.getcwd(),'study_unittest.py')
    suite.addTests(testcases)
    unittest.TextTestRunner().run(suite)

