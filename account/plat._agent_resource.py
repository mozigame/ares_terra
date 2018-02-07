from account.config import *
from utils.request_util import *
from utils.obj_conver import *
from account.po.plat_agent import *

path = {
    'add_agent': ['/apis/plat/agent/save', ('',), 'post', '添加代理',
                  'PlatAgentResource'],
}


# 添加代理
def add_agent(data):
    pc = PathConfig(path_name='add_agent', path=path, Config=Config)
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    return RequestServer(pc, data).request(self_headers=headers)


if __name__ == '__main__':
    get_token('plat')
    agent_po = AgentVO(agentAccount='j_test', loginPwd='1234567', agentName='j_test')
    data = str(class_to_json(agent_po)).replace("'", '"')
    result = add_agent(data)
    print(result.text)
