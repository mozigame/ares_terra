from forseti.config import *
from utils.request_util import *

path = {
    'agent_r_com_day_stat': ['/apis/internal/test/agent_r_com_day_stat', ('startTime', 'endTime'), 'post',
                             '每日退佣统计,手动执行，将代理的每日的退佣入库',
                             'InternalCommandResource.agentRComDayStat'],
    'month_bill_list': ['/apis/plat/agent/r_com/month_bill_list', ('year', 'rows', 'page'), 'get', '代理月结账单，代理显示',
                        'AgentRComResource.queryAgentMonthBillList'],
    'month_bill_detail': ['/apis/plat/agent/r_com/month_bill_detail', ('rComPcodeId',), 'get', '代理月结账单，退佣详情',
                          'AgentRComResource.queryAgentMonthBillDetail'],
    'stat_list': ['/apis/plat/agent/r_com/stat_list', ('pcode', 'agentName', 'rComJudge', 'rComStatus', 'rows', 'page'),
                  'get', '代理退佣统计', 'AgentRComResource'],
    'current_pcode_summary': ['/apis/plat/agent/r_com/current_pcode_summary',
                              ('agentName', 'rComJudge', 'rComStatus', 'rows', 'page'),
                              'get', '资金管理，退佣当期报表', 'AgentRComResource'],
    'update_status': ['/apis/plat/agent/r_com/update', ('rComPcodeId', 'rComStatus'),
                      'post', '退佣状态修改', 'AgentRComResource'],
}


# 每日退佣统计，手动执行
def agent_r_com_day_stat(startTime, endTime):
    pc = PathConfig(path_name='agent_r_com_day_stat', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: startTime, params[1]: endTime}
    return RequestServer(pc, data).request()


# 代理月结账单，代理显示
def month_bill_list():
    pc = PathConfig(path_name='month_bill_list', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: 2018}
    headers = {"Origin": "http://121.58.234.210:19091"}
    return RequestServer(pc, data).request(headers)


# 代理月结账单，退佣详情
def month_bill_detail():
    pc = PathConfig(path_name='month_bill_detail', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: 2018013175}
    return RequestServer(pc, data).request()


# 代理退佣统计
def stat_list():
    pc = PathConfig(path_name='stat_list', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: 49}
    return RequestServer(pc, data).request()


# 退佣当期报表
def current_pcode_summary():
    pc = PathConfig(path_name='current_pcode_summary', path=path, Config=Config)
    params = pc.get_param()
    data = {}
    return RequestServer(pc, data).request()


# 退佣状态修改
def update_status():
    pc = PathConfig(path_name='update_status', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: 20180125334, params[1]: 3}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # Config.env = 'local'
    token = get_token('plat')
    # print('Bearer', token)
    # 代理每日退佣统计，手动执行
    #
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-19 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-19 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-20 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-20 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-21 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-21 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-22 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-22 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-23 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-23 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-24 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-24 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-25 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-25 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-26 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-26 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-27 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-27 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-28 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-28 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-29 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-29 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-30 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-30 23:59:59') * 1000)

    #
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-23 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-23 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-01-24 00:00:00') * 1000,
    #                               datetime_timestamp('2018-01-24 23:59:59') * 1000)

    # 代理月结账单列表，代理显示
    # result = month_bill_list()
    # 代理月结账单详情，代理显示
    # result = month_bill_detail()
    # 代理退佣统计

    # result = stat_list()
    # 资金管理，退佣当期报表
    result = current_pcode_summary()
    # 退佣状态修改
    # result = update_status()
    # print(result.json())
    print(result.text)
