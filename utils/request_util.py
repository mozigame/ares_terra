import requests

# Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY5ODg4MDMsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiIwYWY0NWMxYy1mYWQ4LTQ5N2YtODgzMy03YThkMjJiYzcxZGQiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.mzm602lXxcuNJ1kqJhnK-t5QDANU0Xjn7nEzVpHGk1zVC8ax94Us03YF3842U5SVSUpn9c_orO0xieb_dIlm9zxfm51i618z0np_Md_0MBY3fzax0yxY7e_8bJ5jVFPG_RIEyvzEj5gBF2enCJNR82-J_DIXtstEraTqN1QpyDnY3CQkQonmCNUXF4rMC9xYVjQEWJKfkaLChE_aWfit-xY2p3ZTGsR-X8luCFsa3LjAfuwPbyJgd_3v2BjRnMrVoCDzGEOagS-LGIhP2M0fsWqj7TBwoj9DE_NQmylhGIdrrKthM4H8oAyvlak4rKygwhL_tfr4SVv3QCpz07Gedg'
Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTcwNDQ2OTEsInVzZXJfbmFtZSI6IkFHRU5UX3hxX2RvdWJsZXx2aWN0b3JxIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BR0VOVCJdLCJqdGkiOiJmNDg5MzMxZS1hN2QzLTRkYzUtYjMzNS03YTFkMjA4MDYwMWYiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.PZss9CdPNDfTE5lDLCxZbedCYeGR6bLWHc0xZROZVJj217mtHyAyXb3FYmE4ki0AErxw3uZHql0FCZ218OqaBCTIULsfplmvgAmjZYGR8SxEXudVe9zE4-bVt-mlgBAc-pv1jGMuYyPdy4UQwspa2UjzN9VqackbEcTx8bVpAgFv3342DnU6oNzOcpcCjzinqDy89EGuwafWMvSxBXSv-HYG_fcL-qBBrIlDdmNeesfydkN4L37bKhEtQ8Y1KsGEoJxErJa7O9aQp9hmyUIeXsO5F2zUvydZkl701f1fOd9W5BacQGNWsDGmKnJkpGUSoRsoqRPOg78C0vOmJgZJHA'


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
