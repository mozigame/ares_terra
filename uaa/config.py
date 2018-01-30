import requests
from uaa import configureRead

# Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTcwMjE5MDksInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiI1MmZlNjk5Ni1iZWZhLTQzZTItOGNhZC1mNjE1NzljMTlhMTgiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.jLXSEes9HKncxzmjFwA9F6jeAS6SUWiNppLCDWjyR_0M3qVS_KDFUB2hS7nQVBdv4idybQu91DLV6FNrd5aT9NHhA3v92LtvQjp0P5UOwpfYNxhusAHm4iGmFerzZJFyo0ZXwY8IZuD7eafr0y1jaYpWOsda15iPfc5M5rjfJ3TOmVITZ9EM-uWkYM-wdZyb1vAl4IMFkNdxjCz1UdhqXm3CfM-zJCznsJtfXaiIMQMqG8po3SWZxrdIzXXnfv8M4wbuD2zFtioJ_wjP-4Gv4i4xSf3AM6OWfmq_g9C_WrPm_u9so4pUU-7fGGmAPc88GrScvVlMhk0IK9FL4rUH7w'
Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTcwNDQ2OTEsInVzZXJfbmFtZSI6IkFHRU5UX3hxX2RvdWJsZXx2aWN0b3JxIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BR0VOVCJdLCJqdGkiOiJmNDg5MzMxZS1hN2QzLTRkYzUtYjMzNS03YTFkMjA4MDYwMWYiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.PZss9CdPNDfTE5lDLCxZbedCYeGR6bLWHc0xZROZVJj217mtHyAyXb3FYmE4ki0AErxw3uZHql0FCZ218OqaBCTIULsfplmvgAmjZYGR8SxEXudVe9zE4-bVt-mlgBAc-pv1jGMuYyPdy4UQwspa2UjzN9VqackbEcTx8bVpAgFv3342DnU6oNzOcpcCjzinqDy89EGuwafWMvSxBXSv-HYG_fcL-qBBrIlDdmNeesfydkN4L37bKhEtQ8Y1KsGEoJxErJa7O9aQp9hmyUIeXsO5F2zUvydZkl701f1fOd9W5BacQGNWsDGmKnJkpGUSoRsoqRPOg78C0vOmJgZJHA'


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
        self.host = configureRead.getConfig('api', 'apiRoot');
        self.path_name = path_name
        self.path = path

    def get_path(self):
        return self.host + self.path[self.path_name][0]

    def get_param(self):
        return self.path[self.path_name][1]

    def get_method(self):
        return self.path[self.path_name][2]

    def get_token(self):
        login_path = Config().apiProd+'/uaa/apid/plat/login'
        login_data = {'grant_type': 'password', 'username': 'test2', 'password': '123qwe', 'code': '000000'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        req = requests.post(url=login_path, data=login_data, headers=login_header)
        return req.json()['data']['access_token']

    def get_agent_token(self):
        login_path = 'http://121.58.234.210:19093/uaa/apid/plat/login'
        login_data = {'grant_type': 'password', 'username': 'victorq', 'password': '123456', 'code': '000000'}
        login_header = {'Origin': 'http://121.58.234.210:19091',
                        'Referer': 'http://121.58.234.210:19091',
                        'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        req = requests.post(url=login_path, data=login_data, headers=login_header)
        print(req.text)
        return req.json()['data']['access_token']

# print('Bearer', PathConfig().get_agent_token())
