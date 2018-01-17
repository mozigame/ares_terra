import requests
import json
from hermes.config import *

Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTYyMjUxNjcsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiJlZjE2OTUxMS0zMzMzLTQ2OTktOTFkZi04Yzc5OTg4YWZkM2IiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.GH_BVbWqh9Nt6s4NRYLXcGrW5KsZuqCwB_aqhxCiTHxHuCC-8Arcnyw51ATFmZS5sgwOT75d1JEa2vfWWQnlld-oT_3saRuI7RCafmROBYsFRA_vGPsk5e_PQ7SpjHYCwSxEF401XNm3YrrAEDgaUuuv3ToDK9pngUjLs03Z5GBjyVFusr061ERforkBtj3PAC4-BlsZNZBAKfjGAuTKCQKoGkSpWVq9UkDe2sRE8c8-tCHs9z6a7BCY_V0Xw1yMs4B58MwQ9QMenkaNVHczHESZ7_S4pTd9XyHrKZu2IWhZaBKE2p6KdMPDj4SZyZ0_EeI2QvxCciCX2ohbDNExlg'

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
