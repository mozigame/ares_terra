from terra.config import *
from utils.request_util import *

path = {
    'member_trade_list': ['/apis/member/trade/list', (
        'orderNo', 'platInfoId', 'memberId', 'memberName', 'agentId', 'agentName', 'tradeType', 'startTime', 'endTime',
        'page', 'row'), 'get', '会员金流查询',
                          'CashFlowBaseResource'],
}


# 在es中获取金流基础信息
def member_trade_list(orderNo=None, platInfoId=None, memberId=None, memberName=None, agentId=None, agentName=None,
                      tradeType=None, startTime=None, endTime=None,
                      page=1, row=15):
    pc = PathConfig(path_name='member_trade_list', path=path, Config=Config)
    params = pc.get_param()
    data = {"page": page, "row": row, 'startTime': startTime, 'endTime': endTime}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    result = member_trade_list(page=2, row=5, startTime=datetime_timestamp_ms('2018-02-01 18:00:00'),
                               endTime=datetime_timestamp_ms('2018-02-02 18:50:00'))
    print(result.text)
