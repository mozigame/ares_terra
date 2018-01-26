from account.config import *
from utils.request_util import *

path = {
    'get_agent_info_by_id': ['/apis/plat/agent/getAgentInfoById', ('agentId',), 'get', '获取代理的所有配置信息',
                             'AgentResource'],
}


# 获取代理的所有配置信息
def get_agent_info_by_id(agent_id):
    pc = PathConfig(path_name='get_agent_info_by_id', path=path)
    params = pc.get_param()
    data = {params[0]: agent_id}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # Config.env = 'local'
    result = get_agent_info_by_id(2397)
    print(result.text)
