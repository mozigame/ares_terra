from hermes.config import *
from utils.request_util import *

path = {
    'master_statics_plat_list': ['/apis/master/report/statics/plat/list',
                                 ('platAccount', 'lotteryIds', 'playIds', 'source', 'startTime', 'endTime'), 'get',
                                 '主控平台商统计报表', 'MasterReportStatisticsResource'],
    'master_statics_member_list': ['/apis/master/report/statics/member/list',
                                   ('memberAccount', 'agentAccount', 'platAccount', 'lotteryId', 'playIds', 'source',
                                    'startTime', 'endTime'), 'get',
                                   '主控会员统计报表', 'MasterReportStatisticsResource'],
}

''' 
source 
1 PC PC
2 H5 H5
3 IOS IOS
4 Android ANDROID
'''


# 主控平台商统计报表
def master_statics_plat_list(platAccount=None, lotteryIds=None, playIds=None, source=None, startTime=None,
                             endTime=None):
    pc = PathConfig(path_name='master_statics_plat_list', path=path, Config=Config)
    data = {'platAccount': platAccount, 'lotteryIds': lotteryIds, 'playIds': playIds, 'source': source,
            'startTime': startTime, 'endTime': endTime}
    return RequestServer(pc, data).request()


# 主控会员统计报表
def master_statics_member_list(memberAccount=None, agentAccount=None, platAccount=None, lotteryId=None, playIds=None,
                               source=None, startTime=None,
                               endTime=None):
    pc = PathConfig(path_name='master_statics_member_list', path=path, Config=Config)
    data = {'memberAccount': memberAccount, 'agentAccount': agentAccount, 'platAccount': platAccount,
            'lotteryId': lotteryId, 'playIds': playIds, 'source': source,
            'startTime': startTime, 'endTime': endTime}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    AresTerraCons.ENV = ENV.PROD
    get_token('plat')
    result = master_statics_plat_list(#platAccount='test', playIds=[62102],
                                      # lotteryIds=[2,4],
                                      startTime=datetime_timestamp_ms('2018-02-01 00:00:00'),
                                      endTime=datetime_timestamp_ms('2018-03-22 00:00:00')
    )
    # result = master_statics_member_list(platAccount='xq_double',playIds=[62102], startTime=datetime_timestamp_ms('2018-01-01 00:00:00'),
    #                               endTime=datetime_timestamp_ms('2018-02-22 00:00:00'))
    print(result.text)
