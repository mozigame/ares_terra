import requests

# Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTcwMjE5MDksInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiI1MmZlNjk5Ni1iZWZhLTQzZTItOGNhZC1mNjE1NzljMTlhMTgiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.jLXSEes9HKncxzmjFwA9F6jeAS6SUWiNppLCDWjyR_0M3qVS_KDFUB2hS7nQVBdv4idybQu91DLV6FNrd5aT9NHhA3v92LtvQjp0P5UOwpfYNxhusAHm4iGmFerzZJFyo0ZXwY8IZuD7eafr0y1jaYpWOsda15iPfc5M5rjfJ3TOmVITZ9EM-uWkYM-wdZyb1vAl4IMFkNdxjCz1UdhqXm3CfM-zJCznsJtfXaiIMQMqG8po3SWZxrdIzXXnfv8M4wbuD2zFtioJ_wjP-4Gv4i4xSf3AM6OWfmq_g9C_WrPm_u9so4pUU-7fGGmAPc88GrScvVlMhk0IK9FL4rUH7w'
Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTcwNDMzNTgsInVzZXJfbmFtZSI6IkFHRU5UX3hxX2RvdWJsZXx2aWN0b3JxIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BR0VOVCJdLCJqdGkiOiI3M2U1NzQ5Yy1mYTA0LTRjZWItYTA0Yy01MTE2NzM2ZGUwYmMiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.P8x2WZa2vfftIg2Y3Y1w9DWwynmwhIKPtxvaKp5vDB6dtpzEVeCDJuENkgT-OC5LWdFMJtpzg7oOnl-weoOtuv-2CRXaEceJJ_Q_e-vY7GtGa0BUsC6R3bYSeUQH_n7VBGgRzhad_08VTXsKDaKKYn-qfxqacaCYM9H6M1k_OIZAK-Tuc9g0qJp0XQoEXBC3Vkv34RVfafOaJCiPy9ZMl4y75MN8tg0S9Qn4o1PhHOfonmNyyVWRHfvT0AWuC4HdhJvrArhx8-r8VSqvqjlfCxc5SqRL94JxEFRjVYXn-0LHEfZS9rq2ZYSZbXcmH3G8Nth4ZCOIxLDAVaOCpRyE_A'


class Config():
    host = 'http://localhost:8083'
    # host = 'http://192.168.1.109:8083'
    test_host = 'http://192.168.0.223:8083'
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

    def get_token(self):
        login_path = 'http://121.58.234.210:19093/uaa/apid/plat/login'
        login_data = {'grant_type': 'password', 'username': 'test2', 'password': '123qwe', 'code': '000000'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        req = requests.post(url=login_path, data=login_data, headers=login_header)
        return req.json()['data']['access_token']

    def get_agent_token(self):
        login_path = 'http://121.58.234.210:19093/uaa/apid/plat/login'
        login_data = {'grant_type': 'password', 'username': 'victorq', 'password': '123456', 'code': '000000'}
        login_header = {'Origin': 'http://121.58.234.210:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        req = requests.post(url=login_path, data=login_data, headers=login_header)
        return req.json()['data']['access_token']


# print(PathConfig().get_agent_token())
