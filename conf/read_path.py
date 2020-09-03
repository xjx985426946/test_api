import os,sys
from common.readconfig import ReadConf

config_path=os.path.join(os.path.split(os.path.realpath(__file__))[0],'config.conf')

#顶级目录读取出来  项目的路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#测试版本文件路径
test_path = os.path.join(project_path,'test_zeno_1.1.0')


#测试数据的存储的路径
test_data_path = os.path.join(project_path,'test_zeno_1.1.0','data.xlsx')

#测试报告路径
test_data_report = os.path.join(project_path,'test_zeno_1.1.0','case_report')

# #测试日志的存储路径
# log_path=os.path.join(project_path,'test_result.yaml','test_log')
#
# #测试报告的存储路径
# report_path=os.path.join(project_path,'test_result.yaml','html_report')


path = str(sys.argv[0]).split('/')[-1]
# path = 'run_pytest.py'

if path == 'run_pytest.py':

    #test_case_F 测试环境
    f_testperson_data = project_path + '/test_case_F/test_person/test_data/'
    f_testshop_data = project_path + '/test_case_F/test_shop/test_data/'
    f_testintbeecard_data = project_path + '/test_case_F/test_intbeecard/test_data/'
    f_testintbeedata = project_path + '/test_case_F/test_intbeedata/test_data/'
    f_testorder_data = project_path + '/test_case_F/test_order/test_data/'
    f_testcoupons_data = project_path + '/test_case_F/test_coupons/test_data/'


    # test_case_V 测试环境
    test_homepage_data = project_path + '/test_case_V/test_homepage/test_data/'
    test_PersonalCenter_data = project_path + '/test_case_V/test_personalCenter/test_data/'
    test_find_data = project_path + '/test_case_V/test_find/test_data/'


    #test_case_C  测试环境
    c_test_personal_data = project_path + '/test_case_C/test_personal/test_data/'
    c_test_myorder_data = project_path + '/test_case_C/test_myorder/test_data/'
    c_test_wc = project_path + '/test_case_C/test_wc/test_data/'


    #test_intbeebusiness 测试环境
    test_intbeebusiness_data = project_path + '/test_intbeebusiness_case/test_data/'


    #user_center 测试环境
    test_uc_data = project_path + '/test_case_usercenter/test_data/'
    test_shop_data = project_path + '/test_shop_center/test_data/'

if path == 'run_production.py':

    # test_case_F 线上
    f_testperson_data = project_path + '/test_case_F/test_person/test_data_production/'
    f_testshop_data = project_path + '/test_case_F/test_shop/test_data_production/'
    f_testintbeecard_data = project_path + '/test_case_F/test_intbeecard/test_data_production/'
    f_testintbeedata = project_path + '/test_case_F/test_intbeedata/test_data_production/'
    f_testorder_data = project_path + '/test_case_F/test_order/test_data_production/'
    f_testcoupons_data = project_path + '/test_case_F/test_coupons/test_data_production/'


    # # test_case_V 线上环境
    test_homepage_data = project_path + '/test_case_V/test_homepage/test_data_production/'
    test_PersonalCenter_data = project_path + '/test_case_V/test_personalCenter/test_data_production/'
    test_find_data = project_path + '/test_case_V/test_find/test_data_production/'

    # test_case_c 线上环境
    c_test_personal_data = project_path + '/test_case_C/test_personal/test_data_production/'
    c_test_myorder_data = project_path + '/test_case_C/test_myorder/test_data_production/'
    c_test_wc = project_path + '/test_case_C/test_wc/test_data_production/'

    # test_intbeebusiness
    test_intbeebusiness_data = project_path + '/test_intbeebusiness_case/test_data/'

    # user_center
    test_uc_data = project_path + '/test_case_usercenter/test_data/'
    test_shop_data = project_path + '/test_shop_center/test_data/'
else:

    #test_case_F 测试环境
    f_testperson_data = project_path + '/test_case_F/test_person/test_data/'
    f_testshop_data = project_path + '/test_case_F/test_shop/test_data/'
    f_testintbeecard_data = project_path + '/test_case_F/test_intbeecard/test_data/'
    f_testintbeedata = project_path + '/test_case_F/test_intbeedata/test_data/'
    f_testorder_data = project_path + '/test_case_F/test_order/test_data/'
    f_testcoupons_data = project_path + '/test_case_F/test_coupons/test_data/'

    #new
    f_test_createcard = project_path + '/test_case_F2/test_intbeecard/test_data/'
    f_test_order = project_path + '/test_case_F2/test_order/test_data/'
    f_test_product = project_path + '/test_case_F2/test_product/test_data/'
    f_test_coupon = project_path + '/test_case_F2/test_coupon/test_data/'
    f_test_shop = project_path + '/test_case_F2/test_shop/test_data/'
    f_test_userauthentication =  project_path + '/test_case_F2/test_userauthentication/test_data/'
    wxappF_test_order = project_path + '/test_wxappF/test_order/test_data/'

    # test_case_V 测试环境
    test_homepage_data = project_path + '/test_case_V/test_homepage/test_data/'
    test_PersonalCenter_data = project_path + '/test_case_V/test_personalCenter/test_data/'
    test_find_data = project_path + '/test_case_V/test_find/test_data/'

    #new
    v_test_userauthentication =  project_path + '/test_case_V2/test_userauthentication/test_data/'
    v_test_userinfo = project_path + '/test_case_V2/test_userinfo/test_data/'
    v_test_poster = project_path + '/test_case_V2/test_poster/test_data/'
    v_test_task = project_path + '/test_case_V2/test_task/test_data/'
    v_test_inventory = project_path + '/test_case_V2/test_inventory/test_data/'
    v_test_card =  project_path + '/test_case_V2/test_card/test_data/'
    v_test_follows = project_path + '/test_case_V2/test_follows/test_data/'
    v_test_coupon = project_path + '/test_case_V2/test_coupon/test_data/'
    v_test_home = project_path + '/test_case_V2/test_home/test_data/'
    v_test_bank = project_path + '/test_case_V2/test_bank/test_data/'
    v_test_common = project_path + '/test_case_V2/test_common/test_data/'
    v_test_assets = project_path + '/test_case_V2/test_assets/test_data/'

    #test_case_C  测试环境
    c_test_personal_data = project_path + '/test_case_C/test_personal/test_data/'
    c_test_myorder_data = project_path + '/test_case_C/test_myorder/test_data/'
    c_test_wc = project_path + '/test_case_C/test_wc/test_data/'

    #new
    c_test_inventoty = project_path + '/test_case_C2/test_inventory/test_data/'
    c_test_address = project_path + '/test_case_C2/test_address/test_data/'
    c_test_order = project_path + '/test_case_C2/test_order/test_data/'
    c_test_userinfo = project_path + '/test_case_C2/test_userinfo/test_data/'
    c_test_coupon = project_path + '/test_case_C2/test_coupon/test_data/'
    c_test_pay = project_path + '/test_case_C2/test_pay/test_data/'
    #test_intbeebusiness 测试环境
    test_intbeebusiness_data = project_path + '/test_intbeebusiness_case/test_data/'

    #user_center 测试环境
    test_uc_data = project_path + '/test_case_usercenter/test_data/'
    test_shop_data = project_path + '/test_shop_center/test_data/'

#apiobject
procedure_data = project_path + '/apiObject/'

commondata =  project_path + '/common/'

tooldata = project_path + '/other/tooldata/'

test_common = project_path + '/apiObject/'



test_new_data = project_path + '/test_new/test_data/'

