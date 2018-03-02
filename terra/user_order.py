from terra.config import *
from utils.request_util import *

path = {
    'user_order_get_count': ['/apis/user_order/get_count', (), 'get', '获取订单数量', 'UserOrderResource'],
    'user_order_file_get_files': ['/apis/user_order_file/get_file_names', ('pdate'), 'get',
                                  '获取mongo中执行完成的订单文件名称', 'UserOrderResource'],
    'user_order_import_hdfs_data': ['/apis/user_order/import_hdfs_data', ('pdate'), 'post',
                                    '导入hdfs的order文件', 'UserOrderResource'],
}


# 获取订单数量
def user_order_get_count():
    pc = PathConfig(path_name='user_order_get_count', path=path, Config=Config)
    return RequestServer(pc, None).request()


# 获取mongo中执行完成的订单文件名称
def user_order_file_get_files(pdate):
    pc = PathConfig(path_name='user_order_file_get_files', path=path, Config=Config)
    param = {'pdate': pdate}
    return RequestServer(pc, param).request()


# 导入hdfs的order文件
def user_order_import_hdfs_data(pdate):
    pc = PathConfig(path_name='user_order_import_hdfs_data', path=path, Config=Config)
    param = {'pdate': pdate}
    return RequestServer(pc, param).request()


if __name__ == '__main__':
    result = user_order_get_count()
    # result = user_order_file_get_files(20171118)
    for month in range(11, 13):
        for day in range(1, 32):
            if day < 10:
                str_day = '0{}'.format(day)
            else:
                str_day = str(day)
            pdate = '2017{}{}'.format(month, str_day)
            result = user_order_import_hdfs_data(pdate)
            print(result.text)
    for day in range(1, 32):
        if day < 10:
            str_day = '0{}'.format(day)
        else:
            str_day = str(day)
        pdate = '2018{}{}'.format('01', str_day)
        result = user_order_import_hdfs_data(pdate)
        print(result.text)

    for day in range(1, 30):
        if day < 10:
            str_day = '0{}'.format(day)
        else:
            str_day = str(day)
        pdate = '2018{}{}'.format('02', str_day)
        result = user_order_import_hdfs_data(pdate)
        print(result.text)

