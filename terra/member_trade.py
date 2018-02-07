import requests
from utils.request_util import *
from time import sleep
from terra.config import *

url = ''

path = {
    'get_by_id': ['/api/hb/member_trade/get', ('id',), 'get', '根据id获取金流信息', 'MemberTradeResource'],
    'batch_get': ['/api/hb/member_trade/batch_get', ('ids',), 'get', '批量获取HBase中的金流', 'MemberTradeResource'],

}


# 根据id获取用户信息
def get_by_id(id):
    pc = PathConfig(path_name='get_by_id', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: id}
    return RequestServer(pc, data).request()


# 根据id获取用户信息
def batch_get(ids):
    pc = PathConfig(path_name='batch_get', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: ids}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # result = get_by_id('20180203150536317')
    result = batch_get(['20180203150536317', '20180203160026966', '20180203160830021', '20180203160933447'])
    print(result.text)
