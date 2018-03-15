import multiprocessing

from hermes.config import *
from utils.request_util import *
from constains import AresTerraCons,ENV

path = {
    'charge_order': ['/apis/balance/charge/order', ('memberId', "platInfoId", "orderId", "acType", "amount"),
                     'post', '下单扣款', 'MemberBalanceResource'],
    'balance_update': ['/apis/balance/update', ('amount', "memberId", "acType",),
                       'post', '修改会员余额', 'MemberBalanceResource'],
    'balance_get': ['/apis/balance/internal/get', ('memberId', "memberName", "platInfoId",),
                    'get', '查询会员余额', 'MemberBalanceResource'],
    'balance_increment': ['/apis/balance/increment', ('amount', "memberId", "acType",),
                          'post', '同步增减余额', 'MemberBalanceResource'],
}


# 下单扣款
def charge_order(member_id=None, plat_info_id=None, order_id=None, ac_type=1, amount=None):
    pc = PathConfig(path_name='charge_order', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: member_id, params[1]: plat_info_id, params[2]: order_id, params[3]: ac_type, params[4]: amount}
    return RequestServer(pc, data).request()


# 修改会员余额
def balance_update(amount=None, memberId=None, acType="1"):
    pc = PathConfig(path_name='balance_update', path=path, Config=Config)
    data = {'amount': amount, 'memberId': memberId, 'acType': acType}
    return RequestServer(pc, data).request()


# 同步增减余额
def balance_increment(amount=None, memberId=None, acType="1", c_upd=None):
    pc = PathConfig(path_name='balance_increment', path=path, Config=Config)
    data = {'amount': amount, 'memberId': memberId, 'acType': acType, 'count': c_upd}
    return RequestServer(pc, data).request()


# 获取会员余额
def balance_get(memberId, memberName=None, platInfoId=None):
    pc = PathConfig(path_name='balance_get', path=path, Config=Config)
    data = {'memberId': memberId}
    return RequestServer(pc, data).request()


def pressure_get_balance():
    for i in range(0, 10):
        try:
            result = balance_get(192)
            print("--> get balance : " + result.text)
        except Exception as err:
            print(str(err))


def pressure_incr_balance():
    for i in range(0, 10):
        try:
            result = balance_increment(10, memberId=192, acType="1")
            print("--> update balance" + result.text)
        except Exception as err:
            print(str(err))


def pressure_charge_order():
    for i in range(0, 10):
        try:
            result = charge_order(member_id=178497, plat_info_id=38, order_id="{}{}".format(get_time_stamp(), i), amount=20)
            print("--> charge_order : "+result.text)
        except Exception as err:
            print(str(err))

def pressure_hermes_balance():
    for i in range(5):
        i += 1
        # 多进程代码开了16个进程
        pool = multiprocessing.Pool(processes=16)
        results = []
        for i in range(0, 10000):
            results.append(pool.apply_async(pressure_get_balance(), ))
            results.append(pool.apply_async(pressure_incr_balance(), ))
            results.append(pool.apply_async(pressure_charge_order(), ))
        # for i in range(len(proxies)):
        # results[i].get()
        pool.close()
        pool.join()


if __name__ == '__main__':
    get_token('plat')
    AresTerraCons.ENV=ENV.TEST
    # defStartTime = time.time() * 1000
    # for i in range(0, 1000):
    #     startTime = time.time() * 1000
    #     result = charge_order(member_id=178497, plat_info_id=38, order_id='210ap20181015v2%snqe' % i, amount=20)
    #     print(i, '\n', result.text)
    #     print("expend time : %f" % (time.time() * 1000 - startTime))
    #     print("all expend time : %f" % (time.time() * 1000 - defStartTime))
    # result = balance_increment(amount=1000000, memberId=355559)
    # print(result.text)
    # result = balance_get(192)
    # print(result.text)
    pressure_hermes_balance()
