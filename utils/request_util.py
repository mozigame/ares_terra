import requests
import time
from uaa import configureRead


class RequestServer():
    _Authorization = ''

    def __init__(self, pc, data):
        self.pc = pc
        self.data = data

    def request(self, self_headers=None, self_proxies=None):
        if RequestServer._Authorization=='' or RequestServer._Authorization is None:
            RequestServer._Authorization='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MjAwNjQ4NDEsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiI1NWM4MDRlNC0wNTkwLTQxZWUtOGM1Yi03ZTdiYTg1M2Q2M2YiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.WOOrcX2SbjmaDzt4Zrk0hV-JxqvPOZLAohyGvIoPR06mfdv01at76VDRsqP6hXZeMFT5jmzNNELrZ5Ucxh7Rd1fXzbnOd-RTEnSZWqp9kr2WLA7-0_N0kq3it7AZX6jyeQdtRMbzOz5yofyP8fvzXOOLECjsIRtTKWXtuE3SzWaFkJhrQu910jpAkpw7bEVyBa5tYsrUx0_MQGPW_sQxnRNfw3GodU7p2j3KPm9MZTP-H0VKFHuP_QPYhHhqz0em_FqJZfB5Mu7EAMtv_2613JNbdNM8UqPHoVpsu7heoSP33R_crU2Hd5OGf_gbrvpYHXkaa-R9nGePRK2z1RXF0w'
        headers = {'Authorization': RequestServer._Authorization}
        if self_headers:
            headers = dict(headers, **self_headers)
        # print('login_model='+login_model+' Origin='+self_headers['Origin'])
        # print(headers)
        result = {}
        print("--> request : {}, method : {}, params :{}".format(self.pc.get_path(), self.pc.get_method(), self.data))
        if self.pc.get_method() == 'get':
            result = requests.get(url=self.pc.get_path(), params=self.data, headers=headers, proxies=self_proxies,
                                  timeout=25)
        elif self.pc.get_method() == 'post':
            result = requests.post(self.pc.get_path(), data=self.data, headers=headers, proxies=self_proxies,
                                   timeout=25)
        else:
            raise Exception('未指定请求方法')
        return result


name_cans = '战国秦王王去除宫中的装饰避免视野死角并下令没有人可以靠近秦王百步之内征战其中以秦国最强而秦王也就成无名朝李抵达宫中向秦王讲述他如伟何杀死残剑飞雪和长空作为奖赏无名得以走至距秦王十步之遥' \
            '无名讲述他如秦何先在秦国侍卫王面前杀了长曼空然后至赵国找匿居在书法学院秦中的残剑和飞雪无名向残剑求字试图从一个剑字中看出残剑的剑法说到这时宫中侍卫就将那张字展开给秦王观看无名接着说他得知残剑和飞雪原本一对恋人因飞雪曾与长空有一段情而疏远所以就向两人说出自己的身份并利用两人的心结制造弱点约定在隔天决战无名故意提出飞雪定会为长空报仇而使残剑忌妒残剑因为中了无名的计而心生愤怒便借由和他的书僮如月章子怡交欢来泄愤却被飞雪撞见飞雪于是在愤怒中杀了残剑隔天飞雪情绪大乱无名便在秦军面前杀了他' \
            '听完无名的讲述后名不相信无连在先前的刺杀末期六国子了各国的杰的故事秦王说敌人因为残剑梁飞雪张玉长空甄丹等人试图刺杀行动中他看出残剑是个正直的人不会背叛飞雪秦王于是讲了他认为的事实无名和残剑飞雪以及长空安排了假对决三人牺牲自己的性命让无名有机会走近可以刺杀秦王的距离无名的剑法藏有一招可以在十步内绝对命中所以三人都愿意牺牲另外无名告诉残剑和飞雪他只需要两人之一在秦军面前中剑再带着另一人的武器秦王就会相信他也杀了另一人残剑和飞雪于是争论谁该牺牲最后飞雪刺伤残剑自己前去赴死'
name_cans_len = name_cans.__len__()


# 合并功能支持所有登入类型
def get_token(login_model):
    loginType = login_model
    apiRoot = configureRead.getConfig('api', 'apiRoot')
    print('--> apiRoot : ' + apiRoot)

    if apiRoot.find('9999') < 0:
        apiRoot = apiRoot + '/uaa'

    if login_model == 'member':
        login_path = apiRoot + '/apid/member/login'
    elif (login_model == 'agent' or login_model == 'plat'):
        login_path = apiRoot + '/apid/plat/login'
    elif login_model == 'control':
        login_path = apiRoot + '/apid/control/login'
    else:
        raise Exception('Inivalid loginModel:' + login_model)

    grant_type = 'password'
    account = configureRead.getConfig(loginType, 'account')
    pw = configureRead.getConfig(loginType, 'pw')

    params = ['grant_type', 'username', 'password', 'code']
    login_data = {params[0]: grant_type, params[1]: account, params[2]: pw, params[3]: '000000'}
    if login_model == 'control':
        login_header = {'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    else:
        origin = configureRead.getConfig(loginType, 'origin')
        login_header = {'Origin': origin, 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
    result = requests.post(url=login_path, data=login_data, headers=login_header)
    print("get token : " + result.text)
    if not RequestServer._Authorization and result and result.json()['err'] == 'SUCCESS':
        RequestServer._Authorization = 'Bearer ' + result.json()['data']['access_token']
        print(RequestServer._Authorization)
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


# 返回毫秒时间戳
def datetime_timestamp_ms(dt):
    return datetime_timestamp(dt) * 1000


def datetime_timestamp(dt):
    # dt为字符串
    # 中间过程一般都需要将字符串转化为时间数组
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
    # 将"2012-03-28 06:53:40"转化为时间戳
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)


def timestamp_datestr():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())
