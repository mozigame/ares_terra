
class Config():
    host = 'http://localhost:8082'
    # host = 'http://192.168.1.109:8083'
    test_host = 'http://192.168.0.223:8082'
    prod_host = 'http://10.1.10.82:8083'
    env = 'test'


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

    def get_token(self, requests):
        login_path = 'http://121.58.234.210:19093/uaa/apid/plat/login'
        login_data = {'grant_type': 'password', 'username': 'test2', 'password': '123qwe', 'code': '000000'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        req = requests.post(url=login_path, data=login_data, headers=login_header)
        return req.json()['data']['access_token']
