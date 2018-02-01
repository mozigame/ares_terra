from hermes.config import *
from utils.request_util import *

path = {
    'charge_order': ['/apis/balance/charge/order', ('memberId', "platInfoId", "orderId", "acType", "amount"),
                     'post', '下单扣款', 'MemberBalanceResource'],
}


# 下单扣款
def charge_order(member_id=None, plat_info_id=None, order_id=None, ac_type=1, amount=None):
    pc = PathConfig(path_name='charge_order', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: member_id, params[1]: plat_info_id, params[2]: order_id, params[3]: ac_type, params[4]: amount}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    Config.env = 'local'
    defStartTime = time.time() * 1000
    for i in range(0, 1000):
        startTime = time.time() * 1000
        result = charge_order(member_id=178497, plat_info_id=38, order_id='210ap20181015v5%snqe' % i, amount=20)
        print(i, '\n', result.text)
        print("expend time : %f" % (time.time() * 1000 - startTime))
    print("all expend time : %f" % (time.time() * 1000 - defStartTime))
