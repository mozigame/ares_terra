import json

from venus.config import *
from utils.request_util import *

path = {
    'repair_no_draw_orders': ['/apis/lottery/repair_no_draw_orders',
                              ('pcode', 'code', 'pdate', 'lotteryId', 'page', 'size'), 'post',
                              '修复未执行开奖流程的订单', 'LotteryResource'],
    'repair_draw_num_wrong': ['/apis/lottery/repair_draw_num_wrong',
                              ('pcode', 'winNum', 'pdate', 'lotteryId'), 'post',
                              '修复中奖号码失败逻辑', 'LotteryResource'],
    'single_order_payoff': ['/apis/lottery/single/order/payoff',
                            ('lotteryId', 'playId', 'platInfoId', 'acType'), 'post',
                            '修复中奖号码失败逻辑', 'LotteryResource'],
}


# 修复未执行开奖流程的订单
def repair_no_draw_orders(pcode, code, pdate, lottery_id, page, size):
    pc = PathConfig(path_name='repair_no_draw_orders', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: pcode, params[1]: code, params[2]: pdate, params[3]: lottery_id, params[4]: page,
            params[5]: size}
    return RequestServer(pc, data).request()


# 修复未执行开奖流程的订单
def repair_draw_num_wrong(pcode, winNum, pdate, lottery_id):
    pc = PathConfig(path_name='repair_draw_num_wrong', path=path, Config=Config)
    data = {"pcode": pcode, "winNum": winNum, "pdate": pdate, "lotteryId": lottery_id}
    return RequestServer(pc, data).request()


def single_order_payoff(lotteryId, playId, platInfoId, acType, content=None):
    pc = PathConfig(path_name='single_order_payoff', path=path, Config=Config)
    headers = {"Content-Type": "application/json"}
    path['single_order_payoff'][0] = "/apis/lottery/single/order/payoff?lotteryId={}&playId={}&platInfoId={}&acType={}". \
        format(lotteryId, playId, platInfoId, acType)
    print(path['single_order_payoff'][0])
    # data = '[{"betContent":"6","betContentProc":[["6"]],"fifthPrizeNum":0,"firstPrizeNum":1,"forthPrizeNum":0,"isTied":0,"isZodiacYear":0,"lotteryId":10,"memberId":2096451,"moneyMode":"y","multiple":3000,"orderId":"210a201803375thn1fi1","orderStatus":1,"payoff":0,"playId":1101207,"secondPrizeNum":0,"thirdPrizeNum":0,"winNumber":"09,13,16,18,19,34,21"}]'
    data = content.encode('utf-8')
    return RequestServer(pc, data).request(self_headers=headers)


'''
1	cq_ssc
2	cq_ssc
3	jx_11x5
4	jx_11x5
5	js_k3
6	js_k3
7	bj_pk10
8	bj_pk10
9	lhc
10	xg_lhc
11	tj_ssc
12	tj_ssc
13	xj_ssc
14	xj_ssc
15	gd_11x5
16	gd_11x5
17	sd_11x5
18	sd_11x5
19	ah_k3
20	ah_k3
21	hub_k3
22	hub_k3
24	luckship
101	bc_ssc
102	bc_ssc
103	bc_11x5
104	bc_11x5
105	bc_k3
106	bc_k3
107	bc_pk10
108	bc_pk10
110	bc_lhc
'''
if __name__ == '__main__':
    # Config.env = 'prod'

    get_token('plat')
    result = repair_no_draw_orders(20180512104, 'cq_ssc', 20180512, 2, 1, 100)
    print(result.text)
    # result = repair_no_draw_orders(201803071143, 'bc_k3', 20180307, 106, 1, 200)
    # result = repair_no_draw_orders(201803071143, 'bc_ssc', 20180307, 102, 1, 200)
    # result = repair_no_draw_orders(20180307120, 'bj_pk10', 20180307, 8, 1, 200)
    # result = repair_no_draw_orders(20180307079, 'cq_ssc', 20180307, 2, 1, 200)
    # result = repair_no_draw_orders(201803070229, 'bc_lhc', 20180307, 110, 1, 200)
    # result = repair_no_draw_orders(201803261008, 'bc_pk10', 20180326, 108, 1, 100)
    # print(result.text)
    # result = repair_draw_num_wrong(pcode="1524738212872", winNum="1,1,1,1,1", pdate=20180426, lottery_id=116)
    # print(result.text)
    # file = open("user_order_20180422.txt", mode='r', encoding='utf-8')
    # lists = file.readlines()
    # file.close()

    # file = open('bb.txt', mode='w+', encoding='utf-8')
    # for i in lists:
    #     if i != '':
    #         print(i)
    #         obj = json.loads(i)
    #         lotteryId = obj[0]['lotteryId']
    #         playId = obj[0]['playId']
    #         platInfoId = obj[0]['platInfoId']
    #         acType = obj[0]['acType']
    #         print(obj[0]['betContent'])
    #         result = single_order_payoff(lotteryId=lotteryId, playId=playId, platInfoId=platInfoId, acType=acType,
    #                                      content=i)
    #         result_json = result.json()
    #         print("json:{}".format(result_json['data']))
    #         file.write("json:{}".format(result_json['data'])+"\n")
    # file.close()

    # file = open("bb.txt", mode='r', encoding='utf-8')
    # lists = file.readlines()
    # file.close()
    # for i in lists:
    #     b=i.replace("json", '\n')
    #     print(b)
    #     file = open("cc.txt", mode='w', encoding='utf-8')
    #     file.write(b)
    #     file.close()
