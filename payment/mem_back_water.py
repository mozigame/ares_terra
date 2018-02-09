from payment.config import *
from utils.request_util import *

'''主控平台商维度会员返水统计'''
path = {
    'plat_backwater_stats': ['/apis/master/plat/backwater/stats',
                             ('platAccount', 'startTime', 'endTime', 'page', 'rows'), 'get', '业主维度会员返水统计',
                             'MemberBackWaterController'],
    'agent_backwater_stats': ['/apis/master/agent/backwater/stats',
                              ('agentAccount', 'platInfoId', 'levelIds', 'startTime', 'endTime'), 'get', '代理维度会员返水统计',
                              'MemberBackWaterController'],
    'member_backwater_stats': ['/apis/master/member/backwater/stats',
                               ('memberAccount', 'lotteryIds', 'platInfoId', 'agentId', 'levelIds', 'startTime',
                                'endTime'), 'get', '会员维度会员返水统计',
                               'MemberBackWaterController'],
}


# 业主维度会员返水统计
def plat_backwater_stats(platAccount=None, startTime=None, endTime=None, page=None, rows=None):
    pc = PathConfig(path_name='plat_backwater_stats', path=path, Config=Config)
    data = {}
    if platAccount:
        data = dict(data, **{'platAccount': platAccount})
    if startTime:
        data = dict(data, **{'startTime': startTime})
    if endTime:
        data = dict(endTime, **{'endTime': endTime})
    if page:
        data = dict(data, **{'page': page})
    if rows:
        data = dict(data, **{'rows': rows})
    return RequestServer(pc, data).request()


# 代理维度会员返水统计
def agent_backwater_stats(agentAccount=None, platInfoId=None, levelIds=None, startTime=None, endTime=None):
    pc = PathConfig(path_name='agent_backwater_stats', path=path, Config=Config)
    data = {'agentAccount': agentAccount, 'platInfoId': platInfoId, 'levelIds': levelIds, 'startTime': startTime,
            'endTime': endTime}
    return RequestServer(pc, data).request()


# 会员维度会员返水统计
def member_backwater_stats(memberAccount=None, lotteryIds=None, platInfoId=None, agentId=None, levelIds=None,
                           startTime=None, endTime=None):
    pc = PathConfig(path_name='member_backwater_stats', path=path, Config=Config)
    data = {'memberAccount': memberAccount, 'lotteryIds': lotteryIds, 'platInfoId': platInfoId, 'agentId': agentId,
            'levelIds': levelIds, 'startTime': startTime, 'endTime': endTime}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    # Config.env = 'local'
    # result=plat_backwater_stats()
    # result=agent_backwater_stats(platInfoId=38)
    result = member_backwater_stats(platInfoId=38, agentId=2192)
    print(result.text)
