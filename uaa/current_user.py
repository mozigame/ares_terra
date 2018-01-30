import os
import sys

from utils.request_util import *

from uaa.config import *

from uaa import configureRead

path = {
    'current_user': ['/uaa/api/currentUser', (), 'get',
                     '获取当前token的用户信息',
                     'CurrentUserResource'],
    'login': ['/uaa/apid/plat/login', ('grant_type', 'username', 'password', 'code'), 'post',
              '获取当前token的用户信息',
              'CurrentUserResource'],
}




# 退佣状态修改
def current_user():
    pc = PathConfig(path_name='current_user', path=path)
    return RequestServer(pc, None).request()


if __name__ == '__main__':
    configureRead.runType='dev';#dev/prod
    print('---runType='+configureRead.runType)
    # 获取当前token用户的信息

    result=RequestServer.getToken(loginModel='control')  #loginModel=member/agent/plat/control
    #print(result.text)
    result = current_user()
    print(result.text)
    # print(configureRead.getConfig('api', 'apiRoot'));

