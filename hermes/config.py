import requests

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY5MzMzMjMsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiIwMmM2N2EzMi05NWVlLTRhNTctYTgxNi1lMGUyMjYyMzMyM2IiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.FzhsWg_KKc9IuIPXRVRQUQ7bR10CnLI9ljYRe-mh0jOzxiDeGGFTqzEojqPqXkFQ8D9B0W-nLtgyFxSwnMl5mDzekmXuUaqG2ADJEhN08UYXnYmA7Xm3GbuBsFjE8tLrTRDjsrTVahc35fnaRRlwm1eoUWuV45o6yOe_byXnqWnjL4yY2AwEdpvO9QGBiwGKjZCPoUHZb0lbxY3vzLGy0Obn0qd2D5FRQOXBLpvyrkq2habnHxiBBt03DlH6ot0pQ6PQF2V-j21Ff_4L8fnVa_6xcxYOVGhs49FYmD_pkdO3dovH_4wU7Qj-1oPGLPyuBA6nOUnmrJHVqN988jO4WA'


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

    def get_token(self):
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
