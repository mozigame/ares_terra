from terra.config import *
from utils.request_util import *

url = ''

path = {
    'add': ['/api/kf/user/add', ('id', 'name', 'age', 'address', 'create_time'), 'post', '添加数据', 'UserResource'],

}


# 添加用户信息
def add(id):
    pc = PathConfig(path_name='add', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: id, params[1]: 'name_' + str(id), params[2]: id, params[3]: 'address'}
    return RequestServer(pc, data).request()


# 根据id获取用户信息
def get_by_id(id):
    pc = PathConfig(path_name='get_by_id', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: id}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # 获取用户信息
    result = add(4)
    # print(result.json())
    # 添加用户信息
    # for i in range(3, 20):
    # result = add('id_%s' % 1)
    #     print(result.text)
    #     sleep(0.1)

    # result = get_by_id('1')
    print(result.text)
