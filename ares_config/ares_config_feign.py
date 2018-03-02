from ares_config.config import *
from utils.request_util import *

path = {
    'odds': ['/apis/odds', ('oddsId', 'lotteryId', 'payoffGroupId'), 'get', '获取赔率信息', 'AresConfigFeignController'],
}


# 获取赔率信息
def odds(oddsId=None, lotteryId=None, payoffGroupId=None):
    pc = PathConfig(path_name='odds', path=path, Config=Config)
    data = {'lotteryId': lotteryId, 'payoffGroupId': payoffGroupId}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    configureRead.runType = 'prod'  # dev/prod
    Config.env = 'prod'
    get_token('plat')

    for k, v in {"8": "1866", "102": "1800", "10": "1970"}.items():
        result = odds(lotteryId=int(k), payoffGroupId=int(v))
        print(k + " " + v + " ")
        print()
        data = result.json()['data']['itemPO']
        list = []
        list.__len__()
        print(type(data))
        print(data.__len__(), data)
        payoffs = []
        for item in data:
            payoffs.append({'playId': item['playId'], 'payoff': item['payoff']})
        print(payoffs.__len__(), payoffs)
