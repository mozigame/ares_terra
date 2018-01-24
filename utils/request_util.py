import requests

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY4OTM1MTgsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiJiZTM4OTgxZi1jNjc0LTQ2YjItYTlmYy02Njk3MzMyMjRlMDkiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.B1w2VYIvL2QhtdpA0a2RXlWeLFGsf0FtpuUkjGacNZCc5ecbV12bd_Av6tul77nrL4v064ga22BLMQ9ucNIiu7HCA3ZtXNOP78zDradmHMxP1c6xw5ca4hKj6JIY-0uJatj24rTx0vgoMLAHdodz3co9vnCC74l6EZYQ_m1u1DdwxWnCwNGx1NIrnTHwYwR689CxLfaa9rcQbTN4pMwR7OEdPyToz9QhdweYWMV47Okz4ZSEu9wW2qTtAPIMff1MgK3pSd3RxG4MSzrfvmXaXsZ4HbkZzcwCj6vhC7S-mThitsTTMgXry1nPRHH_ECjQEbWJNfbBGLBleHxC6djWKw'


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
