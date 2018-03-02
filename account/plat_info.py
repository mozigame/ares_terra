from account.config import *
from utils.request_util import *

path = {
    'plat_info_list': ['/apis/platinfo/list',
                       ('sideType', 'platAccount', 'platName', 'settleType', 'settlePlanName', 'settlePlanId', 'status',
                        'rows', 'page'), 'get', '查询平台商列表', 'PlatInfoResource'],
}


# 查询平台商列表
def plat_info_list(sideType=None, platAccount=None, platName=None, settleType=None, settlePlanName=None,
                   settlePlanId=None, status=None,
                   rows=None, page=None):
    pc = PathConfig(path_name='plat_info_list', path=path, Config=Config)
    data = {'sideType': sideType, 'platAccount': platAccount, 'platName': platName, 'settleType': settleType,
            'settlePlanName': settlePlanName, 'settlePlanId': settlePlanId, 'status': status,
            'rows': rows, 'page': page}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    Config.env = 'prod'
    get_token('plat')
    result = plat_info_list().json()
    print(result)
    for plat in result['data']['rows']:
        # print(plat)
        print(plat['platInfoId'],plat['account'],plat['appid'],plat['platName'], sep='\t')
