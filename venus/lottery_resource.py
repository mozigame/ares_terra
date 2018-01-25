from venus.config import *
from utils.request_util import *

path = {
    'repair_no_draw_orders': ['/apis/lottery/repair_no_draw_orders',
                              ('pcode', 'code', 'pdate', 'lotteryId', 'page', 'size'), 'post',
                              '修复未执行开奖流程的订单', 'LotteryResource'],
}


# 修复未执行开奖流程的订单
def repair_no_draw_orders(pcode, code, pdate, lottery_id, page, size):
    pc = PathConfig(path_name='repair_no_draw_orders', path=path)
    params = pc.get_param()
    data = {params[0]: pcode, params[1]: code, params[2]: pdate, params[3]: lottery_id, params[4]: page,
            params[5]: size}
    return RequestServer(pc, data).request()


# 108 ： bc_pk10
# 106 : bc_k3
# 102 ： bc_ssc
# 8 ： bj_pk10
# 16： gd_11x5
# 2 : cq_ssc
# 24 : luckship
if __name__ == '__main__':
    # token = PathConfig().get_token(requests)
    # print('Bearer', token)

    result = repair_no_draw_orders(20180125001, 'luckship', 20180125, 24, 1, 200)
    # result = repair_no_draw_orders(20180124075, 'luckship', 20180124, 24, 1, 200)
    # result = repair_no_draw_orders(20180124076, 'luckship', 20180124, 24, 1, 200)
    # result = repair_no_draw_orders(20180124052, 'luckship', 20180124, 24, 1, 200)
    # result = repair_no_draw_orders(20180124052, 'luckship', 20180124, 24, 1, 200)
    print(result.text)
