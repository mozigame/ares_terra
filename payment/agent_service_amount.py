from payment.config import *
from utils.request_util import *

path = {
    'discount_stat': ['/apis/agent/discount/stat',
                      ('platInfoId', 'agentIdList', 'startTime', 'endTime'), 'get', '查询平台商下指定代理的优惠总计',
                      'MemCashBackDayResource'],
}


# 查询平台商下指定代理的优惠总计
def discount_stat(plat_info_id=None, agent_id_list=None, start_time=None, end_time=None):
    pc = PathConfig(path_name='discount_stat', path=path)
    params = pc.get_param()
    data = {params[0]: plat_info_id, params[1]: agent_id_list, params[2]: start_time, params[3]: end_time}
    headers = {"Accept": "application/json;charset=UTF-8"}
    return RequestServer(pc, data).request(self_headers=headers)


# 查询平台商下指定代理的优惠总计
def discount_stat(plat_info_id=None, agent_id_list=None, start_time=None, end_time=None):
    pc = PathConfig(path_name='discount_stat', path=path)
    params = pc.get_param()
    data = {params[0]: plat_info_id, params[1]: agent_id_list, params[2]: start_time, params[3]: end_time}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    token = PathConfig().get_token(requests)
    print('Bearer', token)

    # result = record(start_time=1516723200000, end_time=1516809600000, lottery_ids='2')
    # print(result.text)
    Config.env = 'test'
    result = discount_stat(plat_info_id=38, agent_id_list=[2192, 2305, 2306], start_time=1516723200000,
                           end_time=1516809599000)
    print(result.text)
