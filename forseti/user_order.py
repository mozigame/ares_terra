import json

from requests import request

from forseti.config import *
from forseti.plays import PlayService
from utils.request_util import *
from forseti.po.user_order import UserOrderPO, UserOrderReq

path = {
    'order_list': ['/api/orders/orderList',
                   ("searchType", 'statusType', 'lotteryId', 'sideType', 'pdate', 'page', 'pageSize'), 'post',
                   '每日退佣统计,手动执行，将代理的每日的退佣入库', 'UserOrderResource'],
    'bet_order': ['/api/orders/betOrder',
                  ("searchType", 'statusType', 'lotteryId', 'sideType', 'pdate', 'page', 'pageSize'), 'post',
                  '下注', 'UserOrderResource'],
    'reload_order': ['/apis/order/reload',
                     ("lotteryId", 'memberId', 'pdate', 'orderIds'), 'post',
                     '刷新缓存中的订单信息', 'UserOrderResource'],
    'order_detail': ['/api/orders/detail',
                     ("lotteryId", 'pdate', 'orderId'), 'get',
                     '获取注单详情', 'UserOrderResource'],
}


class UserOrderService():
    """订单"""
    userOrderPo = UserOrderPO(betAmount=100, betContent='09', betCount=1, betMode=0, chaseCount=1, ifChase=0,
                              moneyMode="y", multiple=3, payoff=0, playId=1011109, remark='wu')

    def bet_order(self, lotteryId, maxUpdateTime=None):
        """投注"""
        # 获取玩法列表
        playService = PlayService()
        plays = playService.getPlaysTree(lotteryId=lotteryId, maxUpdateTime=maxUpdateTime)

        pc = PathConfig(path_name='bet_order', path=path, Config=Config)
        data = '{"list":' \
               '[{"betAmount":300,"betContent":"09","betCount":1,"betMode":0,"chaseCount":1,"ifChase":0,"moneyMode":"y","multiple":3,"payoff":0,"playId":1011109,"remark":"teccc"},' \
               '{"betAmount":300,"betContent":"45","betCount":1,"betMode":0,"chaseCount":1,"ifChase":0,"moneyMode":"y","multiple":3,"payoff":0,"playId":1011145,"remark":"teccc"}],' \
               '"amount":600,"lotteryId":10,"operType":0,"pcode":"2018076","pdate":201809,"remark":"无","source":"h5","sourceType":"2"}'
        self_header = {"Content-Type": "application/json;charset=UTF-8",
                       "Origin": "http://cp2.bccp.co"}
        return RequestServer(pc, str(data).encode(encoding='utf-8')).request(self_headers=self_header)


# 订单列表
# pdate ： 0.本周，1.上周
def order_list(searchType, statusType, lotteryId, sideType, pdate, page, pageSize):
    pc = PathConfig(path_name='order_list', path=path, Config=Config)
    data = {"searchType": searchType, 'statusType': statusType, 'lotteryId': lotteryId, 'sideType': sideType,
            'pdate': pdate, 'page': page, 'pageSize': pageSize}
    self_header = {"Content-Type": "application/json;charset=UTF-8"}
    return RequestServer(pc, str(data).replace("'", '"')).request(self_headers=self_header)


# 下注
# pdate ： 0.本周，1.上周
def bet_order():
    pc = PathConfig(path_name='bet_order', path=path, Config=Config)
    data = '{"list":' \
           '[{"betAmount":300,"betContent":"09","betCount":1,"betMode":0,"chaseCount":1,"ifChase":0,"moneyMode":"y","multiple":3,"payoff":0,"playId":1011109,"remark":"teccc"},' \
           '{"betAmount":300,"betContent":"45","betCount":1,"betMode":0,"chaseCount":1,"ifChase":0,"moneyMode":"y","multiple":3,"payoff":0,"playId":1011145,"remark":"teccc"}],' \
           '"amount":600,"lotteryId":10,"operType":0,"pcode":"2018076","pdate":201809,"remark":"无","source":"h5","sourceType":"2"}'
    self_header = {"Content-Type": "application/json;charset=UTF-8",
                   "Origin": "http://cp2.bccp.co"}
    return RequestServer(pc, str(data).encode(encoding='utf-8')).request(self_headers=self_header)


def reload_order(lotteryId, memberId, pdate, orderIds):
    pc = PathConfig(path_name='reload_order', path=path, Config=Config)
    data = {'lotteryId': lotteryId, 'memberId': memberId, 'pdate': pdate, 'orderIds': orderIds}
    return RequestServer(pc, data).request()


# 获取订单详情
def order_detail(lotteryId, pdate, orderId):
    pc = PathConfig(path_name='order_detail', path=path, Config=Config)
    data = {'lotteryId': lotteryId, 'pdate': pdate, 'orderId': orderId}
    return RequestServer(pc, data).request()


# '{"betAmount":100,"betContent":"21","betCount":1,"betMode":0,"chaseCount":1,"ifChase":0,"moneyMode":"y","multiple":1,"payoff":0,"playId":1011121,"remark":"teccc"},' \
# '{"betAmount":100,"betContent":"33","betCount":1,"betMode":0,"chaseCount":1,"ifChase":0,"moneyMode":"y","multiple":1,"payoff":0,"playId":1011133,"remark":"teccc"},' \


if __name__ == '__main__':
    get_token('plat')
    # result = order_list(searchType=1, statusType=1, lotteryId=10, sideType=2, pdate=0, page=1, pageSize=10)
    # result = bet_order()
    # print(result.text)

    file = open('b.txt', mode='r', encoding='utf-8')
    lists = file.readlines()
    for l in lists:
        if l != '':
            o = json.loads(l)
            lotteryId = o['lotteryId']
            memberId = o['memberId']
            pdate = o['pdate']
            orderIds = o['orderIds']
            result = reload_order(lotteryId=lotteryId, memberId=memberId, pdate=pdate, orderIds=orderIds)
            print(result.text)

            # result = order_detail(lotteryId=lotteryId, pdate=pdate, orderId=orderIds)
            # print(result.text)




