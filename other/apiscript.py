from other.tools import Tool
from other.tt import Tool as Tool1
from apiObject.setupApi import SetupApi
from common.save_value import SaveValue

# F端用户登录
res_f = SetupApi().login_f("13729543834", 'e10adc3949ba59abbe56e057f20f883e')
SaveValue.TOKEN = res_f['access_token']
SaveValue.F_UUID = res_f['uuid']

# V端用户登录
res_v = SetupApi().login_v("13729547054", 'e10adc3949ba59abbe56e057f20f883e')
SaveValue.TOKEN_V = res_v['access_token']
SaveValue.V_UUID = res_v['uuid']

# C端用户登录
res_c = SetupApi().login_c("13729547059", 'e10adc3949ba59abbe56e057f20f883e')
SaveValue.TOKEN_C = res_c['access_token']
SaveValue.C_UUID = res_c['uuid']







if __name__ == '__main__':


    # #验收子任务

    #创建一个任务 显示名额2个，一个用户申请验收
    # print(Tool().task_check())

    #财务审核子任务
    # print(Tool().taskAudit())

    #申请截止的任务
    # print(Tool().taskSetSettleJodHandle())
    #
    # # 修改父任务状态6
    # print(Tool().putCanSettleOrderToAuditJodHandle())

    #结算
    print(Tool().taskSettleToDoneJodHandle())

    #终止任务
    # print(Tool().stopCard(178460))


    #验收子任务
    # print(Tool1().test_task(178458,'20-10185100-165'))



