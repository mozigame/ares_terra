from payment.config import *
from utils.request_util import *

'''主控出款扣款统计'''
path = {
    'plat_withhold_stats': ['/apis/master/plat/draw/withhold/stats',
                            ('platAccount', 'startTime', 'endTime', 'page', 'rows'), 'get', '平台商出款扣款统计',
                            'MemberBackWaterController'],
    'member_withhold_detail': ['/apis/master/member/draw/withhold/detail',
                               ('platInfoId', 'memberName', 'agentName', 'startTime', 'endTime', 'source', 'orderNo'),
                               'get', '会员出款扣款明细',
                               'MemberBackWaterController'],
}


# 平台商出款扣款统计
def plat_withhold_stats(platAccount=None, startTime=None, endTime=None, page=None, rows=None):
    pc = PathConfig(path_name='plat_withhold_stats', path=path, Config=Config)
    data = {'platAccount': platAccount, 'startTime': startTime, 'endTime': endTime, 'page': page,
            'rows': rows}
    return RequestServer(pc, data).request()


# 会员出款扣款明细
def member_withhold_detail(platInfoId=None, memberName=None, agentName=None, startTime=None, endTime=None, source=None,
                           orderNo=None):
    pc = PathConfig(path_name='member_withhold_detail', path=path, Config=Config)
    data = {'platInfoId': platInfoId, 'memberName': memberName, 'agentName': agentName, 'startTime': startTime,
            'endTime': endTime, 'source': source, 'orderNo': orderNo}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    Config.env='local'
    # result = plat_withhold_stats(platAccount='xq_double', startTime=datetime_timestamp_ms('2018-02-01 00:00:00'), endTime=datetime_timestamp_ms('2018-02-07 23:59:59'))
    result = member_withhold_detail(platInfoId=38)
    print(result.text)