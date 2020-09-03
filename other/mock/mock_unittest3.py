from unittest import mock
import unittest
from temple3 import Zhifu,Statues

class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''

    @mock.patch("temple3.Zhifu")
    def test_01(self, mock_Zhifu):
        '''测试支付成功场景'''
        a = mock_Zhifu.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        a.zhifu.return_value = {"result": "success", "reason":"null"}
        # 根据支付结果测试页面跳转
        statues = Statues().zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    @mock.patch("temple3.Zhifu")
    def test_02(self, mock_Zhifu):
        '''测试支付失败场景'''
        b = mock_Zhifu.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        b.zhifu.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = Statues().zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付失败")

if __name__ == "__main__":
    unittest.main()