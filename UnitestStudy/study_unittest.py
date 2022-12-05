import unittest


class StudyUnittest(unittest.TestCase):
    def test_01_method(self):
        print('这是01方法')

    def test_02_method(self):
        print('这是02方法')

    def test_03_method(self):
        print('这是03方法')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(StudyUnittest("test_02_method"))
    suite.addTest(StudyUnittest("test_01_method"))
    unittest.TextTestRunner().run(suite)
    # 要想只执行添加到suite里的测试用例，需要注意右上角的执行环境，unittest***表示执行所有用例，需自己创建一个执行环境
    # https://zhuanlan.zhihu.com/p/97131025
