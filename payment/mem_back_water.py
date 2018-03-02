from payment.config import *
from utils.request_util import *

'''主控平台商维度会员返水统计'''
path = {
    'master_plat_backwater_stats': ['/apis/master/plat/backwater/stats',
                                    ('platAccount', 'startTime', 'endTime', 'page', 'rows'), 'get', '业主维度会员返水统计',
                                    'MemberBackWaterController'],
    'master_agent_backwater_stats': ['/apis/master/agent/backwater/stats',
                                     ('agentAccount', 'platInfoId', 'levelIds', 'startTime', 'endTime'), 'get',
                                     '代理维度会员返水统计',
                                     'MemberBackWaterController'],
    'master_member_backwater_stats': ['/apis/master/member/backwater/stats',
                                      ('memberAccount', 'lotteryIds', 'platInfoId', 'agentId', 'levelIds', 'startTime',
                                       'endTime'), 'get', '会员维度会员返水统计',
                                      'MemberBackWaterController'],
    'plat_member_backwater_stats': ['/apis/plat/member/backwater/stats',
                                    ('memberAccount', 'lotteryIds', 'agentId', 'levelIds', 'startTime',
                                     'endTime'), 'get', '会员维度会员返水统计',
                                    'MemberBackWaterController'],
}


# 业主维度会员返水统计
def master_plat_backwater_stats(platAccount=None, startTime=None, endTime=None, page=None, rows=None):
    pc = PathConfig(path_name='master_plat_backwater_stats', path=path, Config=Config)
    data = {}
    if platAccount:
        data = dict(data, **{'platAccount': platAccount})
    if startTime:
        data = dict(data, **{'startTime': startTime})
    if endTime:
        data = dict(data, **{'endTime': endTime})
    if page:
        data = dict(data, **{'page': page})
    if rows:
        data = dict(data, **{'rows': rows})
    return RequestServer(pc, data).request()


# 代理维度会员返水统计
def master_agent_backwater_stats(agentAccount=None, platInfoId=None, levelIds=None, startTime=None, endTime=None):
    pc = PathConfig(path_name='master_agent_backwater_stats', path=path, Config=Config)
    data = {'agentAccount': agentAccount, 'platInfoId': platInfoId, 'levelIds': levelIds, 'startTime': startTime,
            'endTime': endTime}
    return RequestServer(pc, data).request()


# 会员维度会员返水统计
def master_member_backwater_stats(memberAccount=None, lotteryIds=None, platInfoId=None, agentId=None, levelIds=None,
                                  startTime=None, endTime=None):
    pc = PathConfig(path_name='master_member_backwater_stats', path=path, Config=Config)
    data = {'memberAccount': memberAccount, 'lotteryIds': lotteryIds, 'platInfoId': platInfoId, 'agentId': agentId,
            'levelIds': levelIds, 'startTime': startTime, 'endTime': endTime}
    return RequestServer(pc, data).request()


# 平台商会员维度会员返水统计
def plat_member_backwater_stats(memberAccount=None, lotteryIds=None, agentId=None, levelIds=None,
                                startTime=None, endTime=None):
    pc = PathConfig(path_name='master_member_backwater_stats', path=path, Config=Config)
    data = {'memberAccount': memberAccount, 'lotteryIds': lotteryIds, 'agentId': agentId,
            'levelIds': levelIds, 'startTime': startTime, 'endTime': endTime}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    Config.env = 'test'
    # result = master_member_backwater_stats(platInfoId=38, agentId=2192)
    # result = plat_member_backwater_stats(agentId=2400, endTime=1518364799000, startTime=1517760000000)
    result = master_plat_backwater_stats(platAccount='xq_double', startTime='1518364800000', endTime='1518451199000',
                                         page=1, rows=15)
    # result = master_agent_backwater_stats()
    print(result.text)
