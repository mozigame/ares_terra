import requests
import time
from uaa import configureRead


class RequestServer():
    _Authorization = ''

    def __init__(self, pc, data):
        self.pc = pc
        self.data = data

    def request(self, self_headers=None):
        headers = {'Authorization': RequestServer._Authorization}
        if self_headers:
            headers = dict(headers, **self_headers)
        # print('login_model='+login_model+' Origin='+self_headers['Origin'])
        # print(headers)
        result = {}
        if self.pc.get_method() == 'get':
            result = requests.get(url=self.pc.get_path(), params=self.data, headers=headers)
        elif self.pc.get_method() == 'post':
            result = requests.post(self.pc.get_path(), data=self.data, headers=headers)
        else:
            raise Exception('未指定请求方法')
        return result


# 合并功能，支持所有登入类型
def get_token(login_model):
    loginType = login_model
    apiRoot = configureRead.getConfig('api', 'apiRoot')
    print(apiRoot)

    if apiRoot.find('9999') < 0:
        apiRoot = apiRoot + '/uaa'

    if login_model == 'member':
        login_path = apiRoot + '/apid/member/login'
    if (login_model == 'agent' or login_model == 'plat'):
        login_path = apiRoot + '/apid/plat/login'
    elif login_model == 'control':
        login_path = apiRoot + '/apid/control/login'
    else:
        raise Exception('Inivalid loginModel:' + login_model)

    grant_type = 'password'
    account = configureRead.getConfig(loginType, 'account')
    pw = configureRead.getConfig(loginType, 'pw')

    params = ['grant_type', 'username', 'password', 'code']
    login_data = {params[0]: grant_type, params[1]: account, params[2]: pw, params[3]: '000000_test'}
    if login_model == 'control':
        login_header = {'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    else:
        origin = configureRead.getConfig(loginType, 'origin')
        login_header = {'Origin': origin, 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    result = requests.post(url=login_path, data=login_data, headers=login_header)
    if not RequestServer._Authorization and result and result.json()['err'] == 'SUCCESS':
        RequestServer._Authorization = 'Bearer ' + result.json()['data']['access_token']
        # print(RequestServer._Authorization)
    else:
        print(result.text)
    return result


class PathConfig():
    def __init__(self, Config=None, path_name='', path=None):
        if not path:
            raise Exception('no path')
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


def datetime_timestamp(dt):
    # dt为字符串
    # 中间过程，一般都需要将字符串转化为时间数组
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
    # 将"2012-03-28 06:53:40"转化为时间戳
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)
