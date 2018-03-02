import multiprocessing

from hermes.config import *
from utils.request_util import *
import urllib
from urllib import request
import os

path = {
    'agent_r_com_day_stat': ['/apis/internal/test/agent_r_com_day_stat', ('startTime', 'endTime'), 'post',
                             '每日退佣统计,手动执行，将代理的每日的退佣入库',
                             'InternalCommandResource.agentRComDayStat'],
    'month_bill_list': ['/apis/plat/agent/r_com/month_bill_list', ('year', 'rows', 'page'), 'get', '代理月结账单，代理显示',
                        'AgentRComResource.queryAgentMonthBillList'],
    'month_bill_detail': ['/apis/plat/agent/r_com/month_bill_detail', ('rComPcodeId',), 'get', '代理月结账单，退佣详情',
                          'AgentRComResource.queryAgentMonthBillDetail'],
    'stat_list': ['/apis/plat/agent/r_com/stat_list', ('pcode', 'agentName', 'rComJudge', 'rComStatus', 'rows', 'page'),
                  'get', '代理退佣统计', 'AgentRComResource'],
    'current_pcode_summary': ['/apis/plat/agent/r_com/current_pcode_summary',
                              ('agentName', 'rComJudge', 'rComStatus', 'rows', 'page'),
                              'get', '资金管理，退佣当期报表', 'AgentRComResource'],
    'update_status': ['/apis/plat/agent/r_com/update', ('rComPcodeId', 'rComStatus'),
                      'post', '退佣状态修改', 'AgentRComResource'],
}

# default_appid = 'xqtest'
# default_origin = 'http://cs.88bccp.com'
# default_plat_info_id = 45
# batch_count = 100

default_appid = 'xq_double'
default_origin = 'http://cp.baochi888.com'
default_plat_info_id = 38


# 每日退佣统计，手动执行
def agent_r_com_day_stat(startTime, endTime):
    pc = PathConfig(path_name='agent_r_com_day_stat', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: startTime, params[1]: endTime}
    return RequestServer(pc, data).request()


# 代理月结账单，代理显示
def month_bill_list(self_proxies=None):
    try:
        pc = PathConfig(path_name='month_bill_list', path=path, Config=Config)
        params = pc.get_param()
        data = {params[0]: 2018}
        result = RequestServer(pc, data).request(self_proxies=self_proxies, )
        print("--> proxies_ip is success : {}, \n result : {}".format(self_proxies["http"], result.text))
        return result
    except Exception as err:
        print("--> proxies_ip is failed : {}".format(self_proxies['http']))


# 代理月结账单，退佣详情
def month_bill_detail():
    pc = PathConfig(path_name='month_bill_detail', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: 2018013175}
    return RequestServer(pc, data).request()


# 代理退佣统计
def stat_list():
    pc = PathConfig(path_name='stat_list', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: 49}
    return RequestServer(pc, data).request()


# 退佣当期报表
def current_pcode_summary():
    pc = PathConfig(path_name='current_pcode_summary', path=path, Config=Config)
    params = pc.get_param()
    data = {}
    return RequestServer(pc, data).request()


# 退佣状态修改
def update_status():
    pc = PathConfig(path_name='update_status', path=path, Config=Config)
    params = pc.get_param()
    data = {params[0]: 20180125334, params[1]: 3}
    return RequestServer(pc, data).request()


def urllib_month_bill_list(proxy_ip=None):
    params = {'year': 2018}
    if not proxy_ip:
        proxy_ip = {'http': 'http://110.73.7.28:9999'}
    proxy_handler = urllib.request.ProxyHandler(proxy_ip)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    print('--> params : ', params)
    login_header = {'Origin': default_origin,
                    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MjAwNjA3NjQsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiJmOTE4NmNiNC03NThmLTRmN2UtOTNlZi05NDM3ZWI2MDdlODAiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.I8ex1xhEfPHiarzQJcIP5xZ3NNTtgouRz6wdFTYnPDD86OEATSpXUJBjZjIG4LoxRNs17f9CMvKnKpuT243PGYEFJ1InGgS9m8gMpWWtqeuqHNl6TnW1AKrbEdGvIGip8TIL6_xw0fn3uCSaBzh7ymXTLAFPHQFTRGR1Dv3_H5aPKllsfHvhySgB5QzGWzFSfBUeP3O1xsxDZ0xAD93kJBQKWo-AZFly5WZ30s4LQvGXxIJ9KNAnl7u808y-3TRpjsrEBJ1NUFAhlu0xyT-MWur_s1pSbgaSpsGMF6_kJtuRXSJyUqRP5KQj3OMOYBaGSH5box4G8Xfw5amt6m1p4g',
                    'clientId': 'clientId'}
    print("--> headers : ", login_header)
    data = str(params).replace("'", '"').encode('utf-8')
    req = urllib.request.Request(
        url="http://121.58.234.210:19093/hermes/apis/plat/agent/r_com/month_bill_list?year=2018",
        method="GET", data=data, headers=login_header)
    response = urllib.request.urlopen(req, timeout=25)
    html = response.read().decode('utf-8')
    print("-->  month_bill_list result : ", html)
    global null
    null = ''
    html = eval(html)


# 批量跑代理退佣
def batch_agent_r_com_day_stat():
    for i in range(1, 29):
        if i < 10:
            date_start = '2018-02-0{} 00:00:00'.format(i)
            date_end = '2018-02-0{} 23:59:59'.format(i)
        else:
            date_start = '2018-02-{} 00:00:00'.format(i)
            date_end = '2018-02-{} 23:59:59'.format(i)
        print(date_start)
        print(date_end)
        result = agent_r_com_day_stat(datetime_timestamp(date_start) * 1000,
                                      datetime_timestamp(date_end) * 1000)
        print(result.text)


root_path = os.getcwd()
uaa_root_path = root_path[0:root_path.find('ares_terra')] + 'ares_terra%suaa' % os.sep

if __name__ == '__main__':
    file = open(uaa_root_path + "{}conf{}valid_proxy_ip.txt".format(os.sep, os.sep), 'r')
    ip_list = []
    for line in file:
        ip_list.append({"http": "http://" + line.strip()})
        print(line.strip())
    file.close()
    print(ip_list.__len__())
    print(ip_list)
    Config.env = 'test'
    token = get_token('plat')
    # print('Bearer', token)
    # 代理每日退佣统计，手动执行
    #
    # result = agent_r_com_day_stat(datetime_timestamp('2018-02-01 00:00:00') * 1000,
    #                               datetime_timestamp('2018-02-01 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-02-02 00:00:00') * 1000,
    #                               datetime_timestamp('2018-02-02 23:59:59') * 1000)
    # result = agent_r_com_day_stat(datetime_timestamp('2018-02-03 00:00:00') * 1000,
    #                               datetime_timestamp('2018-02-03 23:59:59') * 1000)

    # 代理月结账单详情，代理显示
    # result = month_bill_detail()
    # 代理退佣统计

    # result = stat_list()
    # 资金管理，退佣当期报表
    # result = current_pcode_summary()
    # 退佣状态修改
    # result = update_status()
    # print(result.json())

    # 代理月结账单列表，代理显示
    for k in range(1, 7):
        # 多进程代码开了16个进程
        pool = multiprocessing.Pool(processes=16)
        results = []
        for i in range((k - 1) * 150, k * 150):
            results.append(pool.apply_async(month_bill_list, (ip_list[i],)))
        pool.close()
        pool.join()
    file.close()
    #
    # for ip in ip_list:
    #     proxy_ip = {"http": "http://" + ip}
    #     try:
    #         result = month_bill_list(proxy_ip)
    #         print("proxy_ip success : " + ip, result.text)
    #     except Exception as err:
    #         print("--> req month_bill_list failed, err : " + str(err))
