from hermes.config import *
from utils.request_util import *

path = {
    'agent_r_com_day_stat': ['/apis/internal/test/mem_cash_back/detail_to_cash_day', ('pdate',), 'post',
                             '每日执行一次，将每个用户每个彩种的返水统计入库',
                             'InternalCommandResource'],
    'grant_balance': ['/apis/internal/test/mem_cash_back/grant_balance', ('date',), 'post',
                      '手动执行返水，给用户金额',
                      'InternalCommandResource'],
    'master_get_cash_back_config': ['/apis/master/cash_back_config/get', ('platInfoId',), 'get',
                                    '主控获取平台商返水配置', ''],
    'master_get_before_cash_back_config': ['/apis/master/cash_back_config/before_get', ('platInfoId',), 'get',
                                           '查询上一次平台商自动返水的配置', ''],
    'master_cash_back_config_set': ['/apis/master/cash_back_config/set', ('platInfoId', 'status',), 'post',
                                    '设置平台商自动返水配置', ''],
    'master_cash_back_config_flush': ['/apis/internal/cash_back_config/flush', (), 'post',
                                      '设置平台商自动返水配置刷新', ''],
}


# 每日执行一次，将每个用户每个彩种的返水统计入库
def agent_r_com_day_stat(pdate):
    pc = PathConfig(path_name='agent_r_com_day_stat', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: pdate}
    return RequestServer(pc, data).request()


# 手动执行返水，给用户金额
def grant_balance(date):
    pc = PathConfig(path_name='grant_balance', path=path, Config=Config)
    params = pc.get_param()
    # 时间为年月日时分秒
    data = {params[0]: date}
    return RequestServer(pc, data).request()


# 主控获取平台商返水配置
def master_get_cash_back_config(platInfoId):
    pc = PathConfig(path_name='master_get_cash_back_config', path=path, Config=Config)
    params = pc.get_param()
    # 时间为年月日时分秒
    data = {params[0]: platInfoId}
    return RequestServer(pc, data).request()


# 主控获取平台商返水配置
def master_get_before_cash_back_config(platInfoId):
    pc = PathConfig(path_name='master_get_before_cash_back_config', path=path, Config=Config)
    data = {"platInfoId": platInfoId}
    return RequestServer(pc, data).request()


# 设置平台商自动返水配置
def master_cash_back_config_set(platInfoId=None, status=None):
    pc = PathConfig(path_name='master_cash_back_config_set', path=path, Config=Config)
    data = {"platInfoId": platInfoId, "status": status}
    return RequestServer(pc, data).request()


# 设置平台商自动返水配置刷新
def master_cash_back_config_flush():
    pc = PathConfig(path_name='master_cash_back_config_flush', path=path, Config=Config)
    return RequestServer(pc, None).request()


if __name__ == '__main__':
    # token = PathConfig().get_token()
    # print('Bearer', token)
    # 每日执行一次，将每个用户每个彩种的返水统计入库
    # for i in range(1, 10):
    get_token("plat")

    # result = agent_r_com_day_stat(20180312)
    # print(result.text)

    # 手动执行返水，给用户金额
    # for i in range(1, 14):
    # result = grant_balance(int('%s010101' % (20180124)))
    # print(result.text)

    result = master_get_cash_back_config(39)
    print(result.text)
    # result = master_get_before_cash_back_config(platInfoId=38)
    # print(result.text)
    result = master_cash_back_config_set(platInfoId=39, status=2)
    print(result.text)
    # result = master_cash_back_config_flush()
    # print(result.text)
