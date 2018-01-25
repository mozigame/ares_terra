import requests

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY5ODg4MDMsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiIwYWY0NWMxYy1mYWQ4LTQ5N2YtODgzMy03YThkMjJiYzcxZGQiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.mzm602lXxcuNJ1kqJhnK-t5QDANU0Xjn7nEzVpHGk1zVC8ax94Us03YF3842U5SVSUpn9c_orO0xieb_dIlm9zxfm51i618z0np_Md_0MBY3fzax0yxY7e_8bJ5jVFPG_RIEyvzEj5gBF2enCJNR82-J_DIXtstEraTqN1QpyDnY3CQkQonmCNUXF4rMC9xYVjQEWJKfkaLChE_aWfit-xY2p3ZTGsR-X8luCFsa3LjAfuwPbyJgd_3v2BjRnMrVoCDzGEOagS-LGIhP2M0fsWqj7TBwoj9DE_NQmylhGIdrrKthM4H8oAyvlak4rKygwhL_tfr4SVv3QCpz07Gedg'


class RequestServer():
    def __init__(self, pc, data):
        self.pc = pc
        self.data = data

    def request(self, self_headers=None):
        headers = {'Authorization': Authorization}
        if self_headers:
            headers = dict(headers, **self_headers)
        if self.pc.get_method() == 'get':
            return requests.get(url=self.pc.get_path(), params=self.data, headers=headers)
        elif self.pc.get_method() == 'post':
            return requests.post(self.pc.get_path(), data=self.data, headers=headers)
        else:
            Exception('未指定请求方法')
