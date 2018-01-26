from uaa.config import *
from utils.request_util import *

path = {
    'current_user': ['/api/currentUser', (), 'get',
                     '获取当前token的用户信息',
                     'CurrentUserResource'],
}


# 退佣状态修改
def current_user():
    pc = PathConfig(path_name='current_user', path=path)
    return RequestServer(pc, None).request()


if __name__ == '__main__':
    result = current_user()
    print(result.text)
