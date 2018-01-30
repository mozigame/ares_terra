from uaa.config import *
from utils.request_util import *

path = {
    'current_user': ['/api/currentUser', (), 'get',
                     '获取当前token的用户信息',
                     'CurrentUserResource'],
    'login': ['/apid/plat/login', ('grant_type', 'username', 'password', 'code'), 'post',
              '获取当前token的用户信息',
              'CurrentUserResource'],
}


# 退佣状态修改
def current_user():
    pc = PathConfig(path_name='current_user', path=path)
    return RequestServer(pc, None).request()


# 登录,获取平台商token
def get_plat_token(env=Config.TEST):
    pc = PathConfig(path_name='login', path=path)
    params = pc.get_param()
    # 生产环境
    if env is Config.PROD:
        data = {params[0]: 'password', params[1]: 'test2', params[2]: '123qwe', params[3]: '000000_test'}
        login_header = {'Origin': 'http://blcagent.88bccp.com', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    else:  # 测试环境
        data = {params[0]: 'password', params[1]: 'test2', params[2]: '123qwe', params[3]: '000000_test'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    return RequestServer(pc, data=data).request(self_headers=login_header)


# 登录,获取代理token
def get_agent_token(env=Config.TEST):
    pc = PathConfig(path_name='login', path=path)
    params = pc.get_param()
    # 生产环境
    if env is Config.PROD:
        data = {params[0]: 'password', params[1]: 'test2', params[2]: '123qwe', params[3]: '000000_test'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    else:  # 测试环境
        data = {params[0]: 'password', params[1]: 'test2', params[2]: '123qwe', params[3]: '000000_test'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    return RequestServer(pc, data=data).request(self_headers=login_header)


# 登录,获取主控token
def get_controller_token(env=Config.TEST):
    pc = PathConfig(path_name='login', path=path)
    params = pc.get_param()
    # 生产环境
    if env is Config.PROD:
        data = {params[0]: 'password', params[1]: 'test2', params[2]: '123qwe', params[3]: '000000_test'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    else:  # 测试环境
        data = {params[0]: 'password', params[1]: 'test2', params[2]: '123qwe', params[3]: '000000_test'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    return RequestServer(pc, data=data).request(self_headers=login_header)


if __name__ == '__main__':
    # 获取当前token用户的信息
    # result = current_user()
    result = get_agent_token()
    print(result.text)
