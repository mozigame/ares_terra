from hermes.config import *
from utils.request_util import *

path = {
    'today_list_order': ['/apis/order/management/today/list',
                         ('condition',), 'get',
                         '管理后台-方案管理-方案记录列表-今天的列表', 'OrderManageResource'],

}


# 管理后台-方案管理-方案记录列表-今天的列表
def today_list_order(side_type=1, page=1, count=15, order_id=None, play_id=None, plat_info_id=38, member_name=None):
    pc = PathConfig(path_name='today_list_order', path=path, Config=Config)
    params = pc.get_param()
    condition = {"sideType": side_type, "page": page, "count": count, "platInfoId": plat_info_id}
    if order_id:
        order = {"orderId": order_id}
        dict(condition, **order)
    if member_name:
        member_name_dict = {"memberName": member_name}
        dict(condition, **member_name_dict)
    if play_id:
        play_id_dict = {"playId": play_id}
        dict(condition, **play_id_dict)

    condition = str(condition).replace("'", '"')
    print(str(condition))
    data = {params[0]: condition}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    result = today_list_order()
    print(result.text)
