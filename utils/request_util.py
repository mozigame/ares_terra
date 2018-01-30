import requests
import time

# Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY5ODg4MDMsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiIwYWY0NWMxYy1mYWQ4LTQ5N2YtODgzMy03YThkMjJiYzcxZGQiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.mzm602lXxcuNJ1kqJhnK-t5QDANU0Xjn7nEzVpHGk1zVC8ax94Us03YF3842U5SVSUpn9c_orO0xieb_dIlm9zxfm51i618z0np_Md_0MBY3fzax0yxY7e_8bJ5jVFPG_RIEyvzEj5gBF2enCJNR82-J_DIXtstEraTqN1QpyDnY3CQkQonmCNUXF4rMC9xYVjQEWJKfkaLChE_aWfit-xY2p3ZTGsR-X8luCFsa3LjAfuwPbyJgd_3v2BjRnMrVoCDzGEOagS-LGIhP2M0fsWqj7TBwoj9DE_NQmylhGIdrrKthM4H8oAyvlak4rKygwhL_tfr4SVv3QCpz07Gedg'

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTczOTc5NTIsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiIwZWMxNDVlNS00NzY2LTQ4OTgtOGU2OC1hNDNjYzM4ZGNmMjYiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.Cb4od13h6e1iuqHBkGFP4Ed6ljkgkfNp4R2OTdLUGzwcm0TkiSM005s3LN-v-5elyJbrud_RrB2JA_2vN2JmktppPdl5DaC2DJoumFejgSsC1YEnoLIs2ZezQnKngfhxtkvpfuC5THBkeFYVRKEWSlJkd2FOCFQQUaxoxy9v96YU0Sdfn9ItSBAtFSHE1FITQpAGHQKd86-oTbnRmYLoXeKopHPu2Joeb5sz1s4vC79c_tqBKApl1xMuqIDjfYYW0dHKTFLgjBGyjNbsvX-7I362Fc7kXxlEHEsC_TBxkch0RKW9CWlr4Okow7d42BHN6RWbbsaZHeJz_ko-Zu9VQw'
agent_authorization = ''


class RequestServer():
    def __init__(self, pc, data):
        self.pc = pc
        self.data = data

    def request(self, self_headers=None, is_agent=False):
        if is_agent:
            headers = {'Authorization': agent_authorization}
        else:
            headers = {'Authorization': Authorization}
        if self_headers:
            headers = dict(headers, **self_headers)
        if self.pc.get_method() == 'get':
            return requests.get(url=self.pc.get_path(), params=self.data, headers=headers)
        elif self.pc.get_method() == 'post':
            return requests.post(self.pc.get_path(), data=self.data, headers=headers)
        else:
            Exception('未指定请求方法')

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


def datetime_timestamp(dt):
    # dt为字符串
    # 中间过程，一般都需要将字符串转化为时间数组
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
    # 将"2012-03-28 06:53:40"转化为时间戳
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)
