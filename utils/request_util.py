import requests
import time

# Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY5ODg4MDMsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiIwYWY0NWMxYy1mYWQ4LTQ5N2YtODgzMy03YThkMjJiYzcxZGQiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.mzm602lXxcuNJ1kqJhnK-t5QDANU0Xjn7nEzVpHGk1zVC8ax94Us03YF3842U5SVSUpn9c_orO0xieb_dIlm9zxfm51i618z0np_Md_0MBY3fzax0yxY7e_8bJ5jVFPG_RIEyvzEj5gBF2enCJNR82-J_DIXtstEraTqN1QpyDnY3CQkQonmCNUXF4rMC9xYVjQEWJKfkaLChE_aWfit-xY2p3ZTGsR-X8luCFsa3LjAfuwPbyJgd_3v2BjRnMrVoCDzGEOagS-LGIhP2M0fsWqj7TBwoj9DE_NQmylhGIdrrKthM4H8oAyvlak4rKygwhL_tfr4SVv3QCpz07Gedg'

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTczMTA0MDEsInVzZXJfbmFtZSI6IkFHRU5UX3hxX2RvdWJsZXx2aWN0b3JxIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BR0VOVCJdLCJqdGkiOiJlMzVkY2VlOC03MTY0LTQ0ZWQtOWE4Zi1kYjk1OTczZDY5MWUiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.olnA619DD0-PM9xFq8QmFw-44TY5R6ItMJbNd1IQ27cVbYaOkDpFSOYDFdgjX_cTvpso5pzWsHdeHKp1UlA7G-YeqwrGv3WQQuFdGb0Q2ED4Ly5Q0TlCwTlNTx5QX5a_ytfRIQLt3q42UPU9Izfb3NV_Kurnrw_hYXhyrF7mF4w13MnDWJy6HrKGVi5dzxqBE7VvcKQZa4IRZr67gGE6YKzfpsZlNUKHx9JFDQYYZG8UldWBPLc2HXFohWBN14x3ro8N-iE5JW-kygm7R0i_nx3S4nAi9gNS3wj9AYPS1L-7lFH7p_ndDlN6ysRDqt2f6L-sucyipuUJA3UMfMiH9g'
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
