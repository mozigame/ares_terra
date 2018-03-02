from venus.config import *
from utils.request_util import *

path = {
    'repair_no_draw_orders': ['/apis/lottery/repair_no_draw_orders',
                              ('pcode', 'code', 'pdate', 'lotteryId', 'page', 'size'), 'post',
                              '修复未执行开奖流程的订单', 'LotteryResource'],
}


# 修复未执行开奖流程的订单
def repair_no_draw_orders(pcode, code, pdate, lottery_id, page, size):
    pc = PathConfig(path_name='repair_no_draw_orders', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: pcode, params[1]: code, params[2]: pdate, params[3]: lottery_id, params[4]: page,
            params[5]: size}
    return RequestServer(pc, data).request()

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
    Config.env = 'prod'
    get_token('plat')
    result = repair_no_draw_orders(201802070906, 'bc_k3', 20180207, 106, 1, 200)
    print(result.text)
