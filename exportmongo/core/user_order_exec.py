import sys
import os
from exportmongo.core import user_order_base
from exportmongo.util.mongo_util import MongoUtil


def getFolderFiles(folder_path):
    files = []
    try:
        for f in os.listdir(folder_path):
            files.append(f)
    except:
        print("--> getFolderCount error, folderPath :" + folder_path)
    return files


def start(pdate):
    platInfoIds = [2, 10, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 58, 59, 60, 61, 62, 65, 66, 67, 68, 69,
                   70, 71]
    lotteryIds = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 102, 104, 106, 108, 110]

    # print("{}:{}:{}".format(lotteryIds.__len__(), platInfoIds.__len__(), (17 * 27)))
    mongoUtil = MongoUtil()
    for platId in platInfoIds:
        for lotteryId in lotteryIds:
            print("{} : {}".format(platId, lotteryId))
            user_order_base.order_list(platId, lotteryId, pdate, mongoUtil)

    order_path = '{}{}'.format(user_order_base.folder_path, pdate)
    proc_order_files = getFolderFiles(order_path)
    if proc_order_files.__len__() > 0:
        hadoop_sh = "hadoop fs -put {}{}/* /hive/data/user_order/{}".format(user_order_base.folder_path, pdate, pdate)
        try:
            print("--> execute hadoop sh : " + hadoop_sh)
            os.system(hadoop_sh)
            # 将文件名称插入mongodb
            user_order_base.add_order_files(mongoUtil.get_conn(), pdate, proc_order_files)
        except:
            raise Exception("--> execute hadoop sh error :: " + hadoop_sh)
    else:
        print("--> folder_count is 0 , don't execute hadoop sh , folder : " + order_path)
