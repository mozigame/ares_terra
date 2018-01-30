class Config():
    host = 'http://localhost:8095'
    # host = 'http://192.168.1.109:8083'
    test_host = 'http://192.168.0.223:8095'
    prod_host = 'http://10.1.10.82:8083'
    env = 'local'


class PathConfig():
    def __init__(self, path_name='', path=None):
        if Config.env == 'test':
            self.host = Config.test_host
        elif Config.env == 'prod':
            self.host = Config.prod_host
        else:
            print('--> 默认为local环境')
            self.host = Config.host
        self.path_name = path_name
        self.path = path

    def get_path(self):
        return self.host + self.path[self.path_name][0]

    def get_param(self):
        return self.path[self.path_name][1]

    def get_method(self):
        return self.path[self.path_name][2]
