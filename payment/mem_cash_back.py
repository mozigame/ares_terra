from payment.config import *
from utils.request_util import *

path = {
    'record': ['/apis/platinfo/mem_cash_back/record',
               ('account', 'type', 'levelIds', 'cashBackId', 'startTime', 'endTime', 'lotteryIds',
                'page', 'size'), 'get', '会员返水记录', 'MemCashBackDayResource'],
    'statistics_mem': ['/apis/platinfo/mem_cash_back/statistics_mem',
                       ('memberId', 'agentId', 'cashBackId', 'startTime', 'endTime', 'lotteryIds',
                        'page', 'size'), 'get', '会员返水统计会员部分', 'MemCashBackDayResource'],
}


# 会员返水记录
def record(account=None, type=None, level_ids=None, cash_back_id=None, start_time=None, end_time=None, lottery_ids=None,
           page=1, size=30):
    pc = PathConfig(path_name='record', path=path)
    params = pc.get_param()
    data = {params[0]: account, params[1]: type, params[2]: level_ids, params[3]: cash_back_id, params[4]: start_time,
            params[5]: end_time, params[6]: lottery_ids, params[7]: page, params[8]: size}
    return RequestServer(pc, data).request()


# 会员返水统计会员部分
def statistics_mem(account=None, type=None, level_ids=None, cash_back_id=None, start_time=None, end_time=None,
                   lottery_ids=None,
                   page=1, size=30):
    pc = PathConfig(path_name='record', path=path)
    params = pc.get_param()
    data = {params[0]: account, params[1]: type, params[2]: level_ids, params[3]: cash_back_id, params[4]: start_time,
            params[5]: end_time, params[6]: lottery_ids, params[7]: page, params[8]: size}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # token = PathConfig().get_token(requests)
    # print('Bearer', token)

    # result = record(start_time=1516723200000, end_time=1516809600000, lottery_ids='2')
    # print(result.text)

    result = statistics_mem(start_time=1516723200000, end_time=1516809600000, lottery_ids='2')
    print(result.text)
