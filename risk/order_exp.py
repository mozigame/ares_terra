from risk.config import *
from utils.request_util import *

path = {
    'save': ['/apis/risk/orderExp/save', (
        'lotteryId', 'lotteryName', 'betMaxWinPay', 'betNumAllPercent', 'continueWinCount', 'continueWinPeriod',
        'betMaxPrize', 'betMaxWinCountInOnePcode', 'sideType'), 'post',
             '保存订单风控配置', 'OrderExpResource'],
}


# 保存订单风控配置
def save(lottery_id, lottery_name):
    pc = PathConfig(path_name='save', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: lottery_id, params[1]: lottery_name}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # Config.env = 'test'
    token = get_token('plat')
    result = save(lottery_id=111, lottery_name='秒速时时彩双面彩')
    print(result.text)
