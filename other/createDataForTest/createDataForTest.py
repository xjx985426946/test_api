from other import tools
from apiObject.setupApi import SetupApi
import yaml
yaml_data = open('data.yaml', encoding="utf-8")
test_data = yaml.load(yaml_data)
def createProduct(mobile_f,product_price,product_award):
    """
    :param mobile_f:
    :return:
    """
    token = SetupApi().login_f(mobile_f)

    pass

def createcard(mobile_f,product_price,product_award):
    """
    :param mobile_f:
    :return:
    """
    pass

def acceptCard(mobile_f,mobile_v,product_price,product_award):
    """

    :param mobile_f:
    :param mobile_v:
    :return:
    """
    pass

def createConfirm(mobile_f,mobile_v,mobile_c,product_price,product_award,product_mum):
    """

    :param mobile_f:
    :param mobile_v:
    :param mobile_c:
    :param product_price:
    :param product_award:
    :param product_mum:
    :return:
    """
    pass

def payfor(mobile_f,mobile_v,mobile_c,product_price,product_award,product_mum,pay_type):
    """

    :param mobile_f:
    :param mobile_v:
    :param mobile_c:
    :param product_price:
    :param product_award:
    :param product_mum:
    :param pay_type:
    :return:
    """
    pass
def derivery(mobile_f,mobile_v,mobile_c,product_price,product_award,product_mum,pay_type):
    """

    :param mobile_f:
    :param mobile_v:
    :param mobile_c:
    :param product_price:
    :param product_award:
    :param product_mum:
    :param pay_type:
    :return:
    """
    pass

def surederivery(mobile_f,mobile_v,mobile_c,product_price,product_award,product_mum,pay_type):
    """

    :param mobile_f:
    :param mobile_v:
    :param mobile_c:
    :param product_price:
    :param product_award:
    :param product_mum:
    :param pay_type:
    :return:
    """
    pass
def 结算(mobile_f,mobile_v,mobile_c,product_price,product_award,product_mum,pay_type):
    """

    :param mobile_f:
    :param mobile_v:
    :param mobile_c:
    :param product_price:
    :param product_award:
    :param product_mum:
    :param pay_type:
    :return:
    """
    pass

def 审核(mobile_f,mobile_v,mobile_c,product_price,product_award,product_mum,pay_type):
    """

    :param mobile_f:
    :param mobile_v:
    :param mobile_c:
    :param product_price:
    :param product_award:
    :param product_mum:
    :param pay_type:
    :return:
    """
    pass