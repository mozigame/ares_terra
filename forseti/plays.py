from forseti.config import *
from utils.request_util import *
from constains import AresTerraCons,ENV

path = {
    'plays_tree': ['/api/playsTree', ("lotteryId", 'maxUpdateTime',), 'get', '获取玩法列表'],

}


class PlayService():
    """玩法"""

    def getPlaysTree(self, lotteryId=None, maxUpdateTime=''):
        """获取玩法列表"""
        pc = PathConfig(path_name='plays_tree', path=path, Config=Config)
        data = {"lotteryId": lotteryId}
        if maxUpdateTime:
            data = dict(data, **{'maxUpdateTime': maxUpdateTime})
        return RequestServer(pc, data).request()


if __name__ == '__main__':
    AresTerraCons.ENV=ENV.TEST
    get_token('member')
    Config.env = 'test'
    playService = PlayService()
    result = playService.getPlaysTree(lotteryId="4")
    print(result.text)
