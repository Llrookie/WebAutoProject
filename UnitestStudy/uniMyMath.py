# 对类myMath1()的方法进行单元测试

'''
    unittest常用函数：
        TestCase：单个测试用例
        TestSuite：测试集合，有多个测试用例组成
        TestLoader:将测试用例加载到测试集合中
        TestRunner:运行器，常用TextTestRunner()
        TestResult:测试集合运行后的结果

    步骤：
        1、导包
        2、创建一个单元测试类,需继承 unittest.TestCase
        3、五个特殊的方法的使用，包括使用场景及执行顺序
            setUp()、test_xxx()、tearDown()不管怎么调整，执行顺序不变；有多条测试用例时，setUp()和tearDown()每次都会执行
            setUp():主要是进行测试用例的资源初始化，前提条件可以写在这里
            test_xxx():测试用例，要把测试用例的步骤写在这里
            tearDown():主要是测试用例资源的释放
            @classmethod注解的方法是类方法，不用创建对象也能使用，在对象创建之前就已经存在的方法，随着类加载一起进的内存
            setUpClass(cls):给当前单元测试类所有用例进行初始化，只执行一次
            tearDownClass():给当前单元测试类所有用例资源释放，只执行一次
        4、创建测试用例：test开头的方法
        5、测试用例执行:
            main():执行所有用例，执行顺序控制不了，按照用例的字母顺序执行，与书写顺序无关,unittest.main()
            解决这个问题，，使用测试集合，TestSuite
            TestSuite:
                1、创建对象
                2、追加测试用例,可使用addTest()、addTests()
                3、调用run()执行测试集合
            TestLoader:
                也可以用这个添加测试用例到测试集合中
                1、创建对象  loader = unittest.TestLoader()
                2、使用loader的loadTestsFromName()方法添加测试用例，并返回TestSuite对象
                    loadTestsFromName()参数比较灵活
                        1、可以是模块名    uniMyMath
                        2、可以是模块中的类名      uniMyMath.uniMyMath
                        3、可以是模块中某一类的某一测试用例名  uniMyMath.uniMyMath.testadd_2
            TestRunner:
                在前面测试用例、测试集合执行的时候都是用TestSuite.run()，suite.run(result),展示效果不好
                TextTestRunner():将结果以text文本形式展示的运行器
                HtmlTestRunner():第三方模块，将结果以html页面形式展示的运行器
                    1、下载该模块的python3版本
                    2、复制该文件到python的安装目录/lib
                    3、导包
                    下载地址：https://pypi.org/project/HTMLTestRunner/
        6、断言
            一个自动化测试用例，测试步骤、断言缺一不可
            unittest中提供的断言方式：
                assertEqual(a,b,msg=""):判断a,b是否相等，相等则断言成功，如果不相等，则报错，msg是报错文案
                assertNotEqual(a,b,msg=""):判断a,b是否不相等
                assertTrue(x):判断x是否为true这个布尔值
                assertFalse(x):判断x是否为false这个布尔值
                assertIs(a,b,msg=""):判断a和b的内存地址是否相等，如果相等则断言成功
                assertIsNot(a,b,msg=""):判断a和b的内存地址是否不相等，如果不相等则断言成功
                assertIsNone(a):判断a对象是不是一个空指针，是则断言成功
                assertIsNotNone(a):判断a对象是不是一个空指针，不是则断言成功
                assertIn(a,b):判断a是不是b的成员，如果是的话，则断言通过
                assertInNot(a,b)判断a是不是b的成员，如果不是的话，则断言通过
                assertIsInstance(a,b,msg=""):判断a是不是b的实例对象，是的话，则断言通过
                assertNotIsInstance(a,b,msg=""):判断a是不是b的实例对象，不是的话，则断言通过

'''
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from UnitestStudy.Mymath import Mymath


class uniMyMath(unittest.TestCase):

    # 注解，在python或java中使用这个方式给方法指定了特定的含义
    @classmethod
    def setUpClass(cls):
        print("我是setUpClass方法")

    @classmethod
    def tearDownClass(cls):
        print("我是tearDownClass方法")

    # 方法名不能改，self参数不能少
    def setUp(self):
        print("我是setup方法")
        # 每一个测试用例都需要创建myMath1对象，可提到这里进行初始化
        self.a = Mymath()

    # 定义一个test开头的方法，这就是一个测试用例
    # 在测试用例中添加文档字符串，这样生成的报告中就有用例说明了
    def test_add_1(self):
        # 验证加法运算
        print("我是测试用例1")
        sum = self.a.add(1, 2)
        exceptenum = 3
        self.assertEqual(sum, exceptenum, "预期结果和实际不相等")
        # a = "12"
        # b = "13"
        # self.assertIs(a,b,"身份不相同")
        # aa = [1,2]
        # bb = [1,2,3]
        # # self.assertIn(aa,bb,"a不在b中")
        # self.assertIsInstance(aa,myMath1,"a不是b的实例对象")

    def test_sub_2(self):
        print("我是测试用例2")
        sum2 = self.a.sub(4, 2)
        exceptnn = 2
        if sum2 == exceptnn:
            print('减法测试通过。。')

    # 方法名不能改，self参数不能少
    def tearDown(self):
        print("我是teardown方法")


if __name__ == '__main__':
    # 调用执行单元测试类，通过主方法main执行
    # 这个方法是可以执行我们单元测试用例的，是全部的测试类中的全部的测试用例
    # unittest.main()

    # 创建testsuite对象
    suite = unittest.TestSuite()

    # #追加单个测试用例到测试集合中
    # #格式：类名(方法名)
    suite.addTest(uniMyMath("test_sub_2"))

    # #追加多个测试用例到测试集合中
    # suite.addTests(map(uniMyMath,["test_add_1","test_sub_2"]))

    # 如果测试用例数量过大，可以使用TestLoader模块，提供了好多方法，将测试用例加到测试集合，返回TestSuite对象
    # 创建一个TestLoader对象
    # loader = unittest.TestLoader()

    # 添加测试用例到测试集合中
    # suite = loader.loadTestsFromName("uniMyMath.uniMyMath.test_sub_2")

    # 使用load的discover()加载用例
    # 第一个参数path是一个目录，表示当前目录下有单元测试用例文件(.py)
    # 第二个参数pattern是一个正则表达式，pattern='uni*.py 表示以uni开头，.py结尾的所有文件
    # suite = unittest.defaultTestLoader.discover(r'../unitestDemo/', pattern='uni*.py')

    # 测试集合中有run方法，直接执行,需要有值来接受返回值(执行结果)
    re = unittest.TestResult()
    suite.run(re)
    # #以字典形式打印出来
    # print(re.__dict__)

    # 使用TextTestRunner()运行器提供的run()方法运行测试集合
    # 需要创建一个文件传入，用来记录结果
    # TextTestRunner是TestRunner子类
    # with open(r'../unitestDemo/re.text','w',encoding='utf-8') as f:
    #     runner = unittest.TextTestRunner(f,descriptions='单元测试执行报告',verbosity=2)
    #     runner.run(suite)

    # 使用HtmlTestRunner()运行器提供的run()方法运行测试集合
    # 需要创建一个文件传入，用来记录结果
    # descriptions='第一次运行结果',verbosity=2,title="单元测试报告"  分别表示文件描述，等级，标题
    # wb,以字节形式写入
    # with open(r'../unitestDemo/re.html','wb') as f:
    #     runner = HTMLTestRunner(f,descriptions='第一次运行结果',verbosity=2,title="单元测试报告")
    #     runner.run(suite)

    # 以当前时间为文件名
    # filename = r'../unitestDemo/' + time.strftime('%Y-%m-%d-%H-%M-%S') + r'.html'
    # # 获取当前文件的目录
    # with open(filename, 'wb') as f:
    #     runner = HTMLTestRunner(f, title="单元测试报告")
    #     runner.run(suite)
