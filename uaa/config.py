import requests
from uaa import configureRead


class Config():
    host = 'http://localhost:9999'
    # host = 'http://192.168.1.109:8083'
    test_host = 'http://192.168.0.225:9999'
    # test_host = 'http://192.168.0.217:9999'
    prod_host = 'http://10.1.10.81:9999'
    LOCAL = 'local'
    TEST = 'test'
    PROD = 'proc'
    env = TEST


class PathConfig():
    def __init__(self, path_name='', path=None):
        self.host = configureRead.getConfig('api', 'apiRoot')
        self.path_name = path_name
        self.path = path

    def get_path(self):
        return self.host + self.path[self.path_name][0]

    def get_param(self):
        return self.path[self.path_name][1]

    def get_method(self):
        return self.path[self.path_name][2]

