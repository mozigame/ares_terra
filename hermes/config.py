import requests

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY3ODU1NzcsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiI2MzAyNTFkYS0zNGQ2LTRlMDAtOGE1MC1jOGZjMGM2ZTk3YzEiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.LyoNqb1s_KW8GxHfGY4PnpBwkWDWO_okWO4HPNMEoa3LuCbDcxYcUWIu-UwxS8Y_so_MmEUjL4w6EPqhz9n3CRfaaZWcnsX2Jt0KpaabSGGM4dcdCihA7u5--lEHZeW0SbBkOTryWZ22_gPQllQXHGlnXHtIwkEvY6YtFTcVmXFLFanZivq9NZ-cnHjfHNBTz_6_LkgKWLDi1QnSTeNLinIWTwJ8sX1DD3neUPohIhZ-0xb65njsOQaPeVhWSo1b6FWxWxvQl8Mm7k2EIFnu-jKDlLF-ePXJHitKhgOOeg-zLl7zkuBqOP2_2CCAK8PsgVbU-v81SL_8fYdCoowK2w'


class Config():
    host = 'http://localhost:8083'
    # host = 'http://192.168.1.109:8083'
    test_host = 'http://192.168.0.223:8083'
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

    def get_token(self, requests):
        login_path = 'http://121.58.234.210:19093/uaa/apid/plat/login'
        login_data = {'grant_type': 'password', 'username': 'test2', 'password': '123qwe', 'code': '000000'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        req = requests.post(url=login_path, data=login_data, headers=login_header)
        return req.json()['data']['access_token']


class RequestServer():
    def __init__(self, pc, data):
        self.pc = pc
        self.data = data

    def request(self):
        headers = {'Authorization': Authorization}
        if self.pc.get_method() == 'get':
            return requests.get(url=self.pc.get_path(), params=self.data, headers=headers)
        elif self.pc.get_method() == 'post':
            return requests.post(self.pc.get_path(), data=self.data, headers=headers)
        else:
            Exception('未指定请求方法')
