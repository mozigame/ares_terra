from ares_config.config import *
from utils.request_util import *

path = {
    'get_agent_period': ['/apis/plat/getAgentPeriod', ('timeMillis', 'platId'), 'get', '获取代理期数配置',
                         'AgentPeriodFeginController'],
}


# 获取赔率信息
def get_agent_period(timeMillis=None, platId=None):
    pc = PathConfig(path_name='get_agent_period', path=path, Config=Config)
    data = {'timeMillis': timeMillis, 'platId': platId}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    Config.env = 'local'
    get_token('plat')
    timeMillis = datetime_timestamp_ms('2018-02-05 22:59:59')
    result = get_agent_period(timeMillis=1517846369000, platId=45)
    print(result.text)
