# host = 'http://localhost:8083'
host = 'http://192.168.1.109:8083'
test_host = 'http://192.168.0.223:8083'
prod_host = 'http://10.1.10.82:8083'

path = {
    'agent_r_com_day_stat': ['/apis/internal/test/agent_r_com_day_stat', ('startTime', 'endTime'), 'post', '每日退佣统计',
                             'InternalCommandResource.agentRComDayStat'],
    'month_bill_list': ['/apis/plat/agent/r_com/month_bill_list', ('year', 'rows', 'page'), 'get', '代理月结账单，代理显示',
                        'AgentRComResource.queryAgentMonthBillList'],
    'month_bill_detail': ['/apis/plat/agent/r_com/month_bill_detail', ('rComPcodeId',), 'get', '代理月结账单，退佣详情',
                          'AgentRComResource.queryAgentMonthBillDetail'],
    'stat_list': ['/apis/plat/agent/r_com/stat_list', ('agentName', 'pcode', 'rComJudge', 'rComStatus', 'rows', 'page'),
                  'get', '代理退佣统计', 'AgentRComResource'],
}


class PathConfig():
    def __init__(self, dev='local', path_name=''):
        if dev == 'text':
            self.host = test_host
        elif dev == 'proc':
            self.host = prod_host
        else:
            print('--> 默认为local环境')
            self.host = host
        self.path_name = path_name

    def get_path(self):
        return self.host + path[self.path_name][0]

    def get_param(self):
        return path[self.path_name][1]

    def get_method(self):
        return path[self.path_name][2]

    def get_token(self, requests):
        login_path = 'http://121.58.234.210:19093/uaa/apid/plat/login'
        login_data = {'grant_type': 'password', 'username': 'test2', 'password': '123qwe', 'code': '000000'}
        login_header = {'Origin': 'http://pt2.bccp.co:19091', 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        req = requests.post(url=login_path, data=login_data, headers=login_header)
        return req.json()['data']['access_token']
