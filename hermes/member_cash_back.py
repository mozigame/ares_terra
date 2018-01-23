from hermes.config import *

path = {
    'agent_r_com_day_stat': ['/apis/internal/test/mem_cash_back/detail_to_cash_day', ('pdate',), 'post',
                             '每日执行一次，将每个用户每个彩种的返水统计入库',
                             'InternalCommandResource'],
    'grant_balance': ['/apis/internal/test/mem_cash_back/grant_balance', ('date',), 'post',
                      '手动执行返水，给用户金额',
                      'InternalCommandResource'],
}


# 每日执行一次，将每个用户每个彩种的返水统计入库
def agent_r_com_day_stat(pdate):
    pc = PathConfig(path_name='agent_r_com_day_stat', path=path)
    params = pc.get_param()
    data = {params[0]: pdate}
    return RequestServer(pc, data).request()


# 手动执行返水，给用户金额
def grant_balance(date):
    pc = PathConfig(path_name='grant_balance', path=path)
    params = pc.get_param()
    # 时间为年月日时分秒
    data = {params[0]: date}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    # token = PathConfig().get_token(requests)
    # print('Bearer', token)
    # 每日执行一次，将每个用户每个彩种的返水统计入库
    # for i in range(1, 10):
    #     result = agent_r_com_day_stat(20180113 + i)
    #     print(result.text)

    # 手动执行返水，给用户金额
    for i in range(1, 14):
        result = grant_balance(int('%s010101' % (20180110 + i)))
        print(result.text)
