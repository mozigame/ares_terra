import requests
import json
from hermes.config import *

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTYyODM4OTQsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiI0ZDMzYmQ0MC0zNmNjLTQ1MWYtOWJjMi04YTNmM2MyZTM5ZTkiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.cAJ9cEhwxaMiM5rF0JR3xQ0O-YhitaHC2MKdsnQ5MBNnoy8cHvQGQbYSf7FQO14CdU-4d6oipZrB1gD8PLiZSZ92bUfRr8TFx2VXZh5CdeC9chn9xBxwbm2QHxGnjL6iiNPLQMrJPpCM-iXijhUJxSn62PXgTt384P15BaSqlcLsLb0v71sGuzmgGIixyRzA0PA9P8zj3W44fRZ-PqM97OnsmD2U2KFC_POQCHQHz-WU2wWVnrfljtzIZTB-wRxMHd0KJy8dXReeiGKbPi66jS9T-__ls9vZgB8wJobtmjTsbFQ_f4zcp1VYX5aeVGJ1tPSASUFIlvZhEwzgVFUgow'

url = ''


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


# 每日退佣统计，手动执行
def agent_r_com_day_stat():
    pc = PathConfig(path_name='agent_r_com_day_stat')
    params = pc.get_param()
    data = {params[0]: 1515945600000, params[1]: 1517414399000}
    return RequestServer(pc, data).request()


# 代理月结账单，代理显示
def month_bill_list():
    pc = PathConfig(path_name='month_bill_list')
    params = pc.get_param()
    data = {params[0]: 2018}
    return RequestServer(pc, data).request()


# 代理月结账单，退佣详情
def month_bill_detail():
    pc = PathConfig(path_name='month_bill_detail')
    params = pc.get_param()
    data = {params[0]: 2018013175}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # token = PathConfig().get_token(requests)
    # print('Bearer',token)
    # 代理每日退佣统计，手动执行
    # result = agent_r_com_day_stat()
    # 代理月结账单列表，代理显示
    # result = month_bill_list()
    # 代理月结账单详情，代理显示
    result = month_bill_detail()
    print(result.json())
    print(result.text)
