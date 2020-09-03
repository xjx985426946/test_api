from common.logger import Log
import json
def auth(func):
    """
    :param func:
    :return:
    """
    def inner(cls,*args,**kwargs):
        try:
            func(cls)
            Log().info("测试通过")
        except AssertionError as e:  # 抛出断言错误异常
            Log().error("断言结果为False~{0}".format(e))
            raise e
        finally:
            print("返回结果：".center(66, "-") + "\n", json.dumps(cls.result, ensure_ascii=False, indent=2))
    return inner



dbdata = None
def dbcheck(func):
    """
    :param func:
    :return:
    """
    def inner(cls,*args,**kwargs):
        global dbdata
        try:
            dbdata = func(cls)
            Log().info("测试通过")
        except AssertionError as e:  # 抛出断言错误异常
            Log().error("断言结果为False~{0}".format(e))
            raise e
        finally:
            pass
    return inner




