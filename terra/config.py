path = {
    'add': ['/api/user/add', ('id', 'name', 'age', 'address', 'create_time'), 'post', '添加数据', 'UserResource'],
    'get_by_id': ['/api/user/get', ('id',), 'get', '根据id获取', 'UserResource'],
    'update': ['/api/user/update', ('id', 'name', 'age', 'address'), 'post', '修改数据', 'UserResource'],
    'query_list': ['/api/user/query_list', ('id', 'name', 'age', 'address', 'page', 'rows'), 'get', '查询列表',
                   'UserResource'],
}


class Config():
    host = 'http://localhost:8081'
    # host = 'http://192.168.1.109:8083'
    test_host = 'http://192.168.0.223:8083'
    prod_host = 'http://10.1.10.82:8083'
    env = 'local'


class PathConfig():
    def __init__(self, path_name=''):
        if Config.env == 'test':
            self.host = Config.test_host
        elif Config.env == 'prod':
            self.host = Config.prod_host
        else:
            print('--> 默认为local环境')
            self.host = Config.host
        self.path_name = path_name

    def get_path(self):
        return self.host + path[self.path_name][0]

    def get_param(self):
        return path[self.path_name][1]

    def get_method(self):
        return path[self.path_name][2]
