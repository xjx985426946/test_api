import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow import threads

#引入改写的报告插件，可进行多线程执行用例，并展示跳过的测试用例，条件允许的话不建议使用多线程，用例设计不好的话怕用例之前互相影响，影响测试
# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "test_ YAML")
reportpath = os.path.join(curpath, "report")

def add_case(case_path=casepath, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

@threads(11)  #多线程执行测试用例，以test_*.py为单位
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试deafult报告', log_path='report')

if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    for i in cases:
         run(i)