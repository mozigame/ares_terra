from payment.config import *
from utils.request_util import *

path = {
    'record': ['/apis/platinfo/mem_cash_back/record',
               ('account', 'type', 'levelIds', 'cashBackId', 'startTime', 'endTime', 'lotteryIds',
                'page', 'size'), 'get', '会员返水记录', 'MemCashBackDayResource'],
    'statistics_mem': ['/apis/platinfo/mem_cash_back/statistics_mem',
                       ('memberId', 'agentId', 'cashBackId', 'startTime', 'endTime', 'lotteryIds',
                        'page', 'size'), 'get', '会员返水统计会员部分', 'MemCashBackDayResource'],
    'master_statistics_mem': ['/apis/master/mem_cash_back/statistics_mem',
                              ('memberId', 'agentId', 'cashBackId', 'startTime', 'endTime', 'lotteryIds',
                               'page', 'size', 'platInfoId'), 'get', '会员返水统计会员部分,主控', 'MemCashBackDayResource'],
    'details': ['/apis/platinfo/mem_cash_back/details',
                ('account', 'type', 'levelIds', 'page', 'rows',), 'get', '会员返水管理返水明细', 'MemCashBackDayResource'],
}


# 会员返水记录
def record(account=None, type=None, level_ids=None, cash_back_id=None, start_time=None, end_time=None, lottery_ids=None,
           page=1, size=30):
    pc = PathConfig(path_name='record', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: account, params[1]: type, params[2]: level_ids, params[3]: cash_back_id, params[4]: start_time,
            params[5]: end_time, params[6]: lottery_ids, params[7]: page, params[8]: size}
    return RequestServer(pc, data).request()


# 会员返水统计会员部分
def statistics_mem(memberId=None, agentId=None, cashBackId=None, startTime=None, endTime=None, lotteryIds=None,
                   page=None, size=None):
    pc = PathConfig(path_name='statistics_mem', path=path, Config=Config)
    data = {'memberId': memberId, 'agentId': agentId, 'cashBackId': cashBackId, 'startTime': startTime,
            'endTime': endTime, 'lotteryIds': lotteryIds, 'page': page, 'size': size}
    return RequestServer(pc, data).request()


# master_statistics_mem
def master_statistics_mem(platInfoId=None, memberId=None, agentId=None, cashBackId=None, startTime=None, endTime=None,
                          lotteryIds=None,
                          page=None, size=None):
    pc = PathConfig(path_name='master_statistics_mem', path=path, Config=Config)
    params = pc.get_param()
    data = {'platInfoId': platInfoId, 'memberId': memberId, 'agentId': agentId, 'cashBackId': cashBackId,
            'startTime': startTime,
            'endTime': endTime, 'lotteryIds': lotteryIds, 'page': page, 'size': size}
    return RequestServer(pc, data).request()


# 会员返水管理返水明细
def details(account=None, type=None, level_ids=None, page=1, size=30):
    pc = PathConfig(path_name='details', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: account, params[1]: type, params[2]: level_ids, params[3]: page, params[4]: size}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    Config.env = 'test'
    # 会员返水记录
    result = record(cash_back_id='20180126014001818',   start_time=1516809600000, end_time=1516895999000, type=1, account='Ctuiyong02',
                    )
    # print(result.text)
    # 会员返水管理返水明细
    # result = details(account=None, type=2)
    # print(result.text)

    # result = statistics_mem( startTime=datetime_timestamp_ms('2017-11-01 00:00:00'), endTime=1516809600000,
    #                         lotteryIds='2')
    # print(result.text)

    # result = master_statistics_mem(platInfoId=38, startTime=1516723200000, endTime=1516809600000, lotteryIds='2')
    print(result.text)
