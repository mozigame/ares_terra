import requests

from time import sleep
from terra.config import *

url = ''


class RequestServer():
    def __init__(self, pc, data):
        self.pc = pc
        self.data = data

    def request(self):
        if self.pc.get_method() == 'get':
            return requests.get(url=self.pc.get_path(), params=self.data)
        elif self.pc.get_method() == 'post':
            return requests.post(self.pc.get_path(), data=self.data)
        else:
            Exception('未指定请求方法')


# 添加用户信息
def add(id):
    pc = PathConfig(path_name='add')
    params = pc.get_param()
    data = {params[0]: id, params[1]: 'name_' + str(id), params[2]: id, params[3]: 'address'}
    return RequestServer(pc, data).request()


# 修改用户信息
def update(id, name, age, address):
    pc = PathConfig(path_name='update')
    params = pc.get_param()
    data = {params[0]: id, params[1]: name, params[2]: age, params[3]: address}
    return RequestServer(pc, data).request()


# 根据id获取用户信息
def get_by_id(id):
    pc = PathConfig(path_name='get_by_id')
    params = pc.get_param()
    data = {params[0]: id}
    return RequestServer(pc, data).request()


# 查询用户列表
def query_list(id='', name='', age='', address='', page=1, rows=15):
    pc = PathConfig(path_name='query_list')
    params = pc.get_param()
    data = {params[0]: id, params[1]: name, params[2]: age, params[3]: address, params[4]: page, params[5]: rows}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # 获取用户信息
    # result = get_by_id(1)
    # print(result.json())
    # 添加用户信息
    # for i in range(3, 20):
    #     result = add(i)
    #     print(result.text)
    #     sleep(0.1)

    result = query_list(address='address', page=1, rows=10)
    print(result.text)
