import pytest
from common.httprequest import HttpRquest
from common.logger import Log
from conf import config,read_path
from common.readyaml import read_yaml
from datetime import datetime
from py._xmlgen import html


#定义一个函数，并在这个函数当中，实现用例的准备工作和清理工作
#在函数面前加上@pytest.fixture
#fixture可以设置作用域，默认是function
@pytest.fixture
def login():
    data = read_yaml(read_path.test_homepage_data,"test_app_login.yaml",config.url)
    Log().info("执行用例: " + data[0]['api_name'] + "-->" + data[0]['discriptions'])
    response = HttpRquest().http_request(data[0]['method'], data[0]['url'],
                                      data[0]['param'],
                                      data[0]['header'], cookies=None)
    result =  response.json()

    yield result['result']['access_token']

@pytest.fixture(scope="class")
def class_use():
    print("我是class级别的ficture")
    yield
    print("结束工作")

@pytest.fixture(scope="class")
def class_use():
    print("我是class级别的ficture")
    yield
    print("结束工作")

@pytest.fixture(scope="module")
def module_use():
    print("我是模块级别的ficture")
    yield
    print("结束工作")

@pytest.fixture(scope="class")
def uilogin():
    print("登录操作")

# pytest.mark.usefixtures("uilogin")


#通过conftest来实现报告的描述
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    # cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    # cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(1, html.td(report.description))
    except:
        pass
    # cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    # cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('Description'))
#     cells.insert(1, html.th('Time', class_='sortable time', col='time'))
#     cells.pop()
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
#     cells.pop()
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)

