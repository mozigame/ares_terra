from terra.config import *
from utils.request_util import *

url = ''

path = {
    'get_es_by_id': ['/api/es/cash_flow/get', ('id',), 'get', '获取金流基础信息,es',
                     'UserResource'],
    'get_hbase_by_id': ['/api/hb/cash_flow/get', ('id',), 'get', '获取金流基础信息, hbase',
                        'UserResource'],
    'batch_get_hbase_by_id': ['/api/hb/cash_flow/batch_get', ('ids',), 'get', '批量获取金流基础信息, hbase',
                              'UserResource'],

}


# 在es中获取金流基础信息
def get_es_by_id(id):
    pc = PathConfig(path_name='get_es_by_id', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: id}
    return RequestServer(pc, data).request()


# 在hbase中获取金流基础信息
def get_hbase_by_id(id):
    pc = PathConfig(path_name='get_hbase_by_id', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: id}
    return RequestServer(pc, data).request()


# 在hbase中获取金流基础信息
def batch_get_hbase_by_id(ids):
    pc = PathConfig(path_name='batch_get_hbase_by_id', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: ids}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # 获取用户信息
    ids = ['20180201182519', '20180201182620']
    result = batch_get_hbase_by_id(ids)
    # print(result.json())
    # 添加用户信息
    # for i in range(3, 20):
    # result = add('id_%s' % 1)
    #     print(result.text)
    #     sleep(0.1)

    # result = get_by_id('1')
    print(result.text)
