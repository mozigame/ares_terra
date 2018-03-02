import ares_config.config as config_config
import account.plat_info as plat_info
from utils.request_util import *

path = {
    'domain_agent_list': ['/apis/domain/listAgent', ('platInfoId',), 'get', '获取赔率信息', 'AresConfigFeignController'],
}


# 获取赔率信息
def domain_agent_list(platInfoId=None):
    pc = PathConfig(path_name='domain_agent_list', path=path, Config=config_config.Config)
    data = {'platInfoId': platInfoId}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    config_config.Config.env = 'test'


