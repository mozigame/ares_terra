import os

import pathlib

folder_path = '/home/sundy/data/mongo/current_data/user_order_data/'
user_order_file_coll = 'user_order_file'


def order_list(platInfoId, lotteryId, pdate, mongoUtil):
    colleName = "UserOrderPO_%d" % pdate
    print("--> start query colleName : {}, platInfoId : {}, lotteryId : {}, pdate : ".format(colleName, platInfoId,
                                                                                             lotteryId, pdate))
    param = {}
    if platInfoId and platInfoId != 0:
        param["platInfoId"] = platInfoId

    if lotteryId and lotteryId != 0:
        param["lotteryId"] = lotteryId

    if pdate and pdate != 0:
        param["pdate"] = pdate

    print("--> param : " + str(param))
    filename = "UserOrderPo_%d_%d_%d" % (platInfoId, lotteryId, pdate)
    dataFilePath = "{}{}{}{}".format(folder_path, pdate, os.sep, filename)

    print("--> filePath : " + dataFilePath)
    try:
        path = pathlib.Path(dataFilePath)
        if path.exists():
            os.remove(dataFilePath)
            print("--> remove file : " + dataFilePath)
        else:
            print("--> file doesn't exist , doesn't remove ::" + dataFilePath)
    except Exception as err:
        print("--> remove file failed : {}, e :{}".format(dataFilePath, str(err)))

    print("--> query colleName : %s_%d_%d" % (colleName, platInfoId, lotteryId))
    query_coll(mongoUtil.get_conn(), colleName, param, dataFilePath)


def query_coll(db, colleName, param, filePath=None):
    user_order = db[colleName]
    file = open(filePath, 'w')
    try:
        for order in user_order.find(param):
            if order:
                order_str = assemOrderStr(order)
                print("--> order : " + order_str)
                file.write(order_str + "\n")
            else:
                print("--> order is null")
    except Exception as err:
        print('--> write file error , filePath :{}, err:{}'.format(filePath, str(err)))
    finally:
        if file:
            file.close()
    print("--> write file success : " + filePath)
    try:
        if os.stat(filePath).st_size <= 1:
            os.remove(filePath)
            print("--> file is empty ,remove file : " + filePath)
    except Exception as err:
        print("--> remove file failed : {}, e :{}".format(filePath, str(err)))


def add_order_files(db, pdate, file_names):
    try:
        user_order_file = db[user_order_file_coll]
        add_obj = {'pdate': pdate, 'fileNames': file_names}
        result = user_order_file.insert_one(add_obj)
        print("--> insert {} success, result :{}, pdate:{}, file_names:{}".
              format(user_order_file_coll, result, pdate, file_names))
    except:
        print("--> insert {} failed, pdate:{}, file_names:{}", user_order_file_coll, pdate, file_names)


def assemOrderStr(order):
    order_str = '{}'.format(order['cid']) + "\t"
    order_str += '{}'.format('0' if 'orderId' not in order else order['orderId']) + "\t"
    order_str += '{}'.format('0' if 'memberId' not in order else order['memberId']) + "\t"
    order_str += '{}'.format('0' if 'agentId' not in order else order['agentId']) + "\t"
    order_str += '{}'.format('0' if 'pcode' not in order else order['pcode']) + "\t"
    order_str += '{}'.format('0' if 'pdate' not in order else order['pdate']) + "\t"
    order_str += '{}'.format('0' if 'playId' not in order else order['playId']) + "\t"
    order_str += '{}'.format('0' if 'betTime' not in order else order['betTime']) + "\t"
    order_str += '{}'.format('0' if 'betMode' not in order else order['betMode']) + "\t"
    order_str += '{}'.format('0' if 'sideType' not in order else order['sideType']) + "\t"
    order_str += '{}'.format('0' if 'acType' not in order else order['acType']) + "\t"
    order_str += '{}'.format('0' if 'betCount' not in order else order['betCount']) + "\t"
    order_str += '{}'.format('0' if 'betAmount' not in order else order['betAmount']) + "\t"
    order_str += '{}'.format('0' if 'validBetAmount' not in order else order['validBetAmount']) + "\t"
    order_str += '{}'.format('0' if 'betContent' not in order else order['betContent']) + "\t"
    order_str += '{}'.format('0' if 'multiple' not in order else order['multiple']) + "\t"
    order_str += '{}'.format('0' if 'moneyMode' not in order else order['moneyMode']) + "\t"
    order_str += '{}'.format('0' if 'ifChase' not in order else order['ifChase']) + "\t"
    order_str += '{}'.format('0' if 'chaseSeq' not in order else order['chaseSeq']) + "\t"
    order_str += '{}'.format('0' if 'chaseCount' not in order else order['chaseCount']) + "\t"
    order_str += '{}'.format('0' if 'chaseWinStop' not in order else order['chaseWinStop']) + "\t"
    order_str += '{}'.format('0' if 'payoff' not in order else order['payoff']) + "\t"
    order_str += '{}'.format('0' if 'winPayRate' not in order else order['winPayRate']) + "\t"
    order_str += '{}'.format('0' if 'orderStatus' not in order else order['orderStatus']) + "\t"
    order_str += '{}'.format('0' if 'source' not in order else order['source']) + "\t"
    order_str += '{}'.format('0' if 'modifyTime' not in order else order['modifyTime']) + "\t"
    order_str += '{}'.format('0' if 'cancelFee' not in order else order['cancelFee']) + "\t"
    order_str += '{}'.format('0' if 'winNumber' not in order else order['winNumber']) + "\t"
    order_str += '{}'.format('0' if 'issueAlias' not in order else order['issueAlias']) + "\t"
    order_str += '{}'.format('0' if 'memberName' not in order else order['memberName']) + "\t"
    order_str += '{}'.format('0' if 'levelId' not in order else order['levelId']) + "\t"
    order_str += '{}'.format('0' if 'firstPrizeNum' not in order else order['firstPrizeNum']) + "\t"
    order_str += '{}'.format('0' if 'secondPrizeNum' not in order else order['secondPrizeNum']) + "\t"
    order_str += '{}'.format('0' if 'thirdPrizeNum' not in order else order['thirdPrizeNum']) + "\t"
    order_str += '{}'.format('0' if 'forthPrizeNum' not in order else order['forthPrizeNum']) + "\t"
    order_str += '{}'.format('0' if 'fifthPrizeNum' not in order else order['fifthPrizeNum']) + "\t"
    order_str += '{}'.format('0' if 'isZodiacYear' not in order else order['isZodiacYear']) + "\t"
    order_str += '{}'.format('0' if 'remark' not in order else order['remark']) + "\t"
    order_str += '{}'.format('0' if 'reforwardPoint' not in order else order['reforwardPoint']) + "\t"
    order_str += '{}'.format('0' if 'modifyUser' not in order else order['modifyUser']) + "\t"
    order_str += '{}'.format('0' if 'parentOrderId' not in order else order['parentOrderId']) + "\t"
    order_str += '{}'.format('0' if 'createTime' not in order else order['createTime']) + "\t"
    order_str += '{}'.format('0' if 'createUser' not in order else order['createUser']) + "\t"
    order_str += '{}'.format('0' if 'lotteryId' not in order else order['lotteryId']) + "\t"
    order_str += '{}'.format('0' if 'platInfoId' not in order else order['platInfoId']) + "\t"
    order_str += '{}'.format('0' if 'pdate' not in order else order['pdate'])
    return order_str


def mkdir_local_folders():
    for month in range(11, 13):
        for day in range(1, 32):
            if day < 10:
                str_day = '0{}'.format(day)
            else:
                str_day = str(day)
            pdate = '2017{}{}'.format(month, str_day)
            create_sh = "mkdir {}{}".format(folder_path, pdate)
            # os.system(create_sh)
            print(create_sh)
    for day in range(1, 32):
        if day < 10:
            str_day = '0{}'.format(day)
        else:
            str_day = str(day)
        pdate = '2018{}{}'.format('01', str_day)
        create_sh = "mkdir {}{}".format(folder_path, pdate)
        print(create_sh)

    for day in range(1, 30):
        if day < 10:
            str_day = '0{}'.format(day)
        else:
            str_day = str(day)
        pdate = '2018{}{}'.format('02', str_day)
        create_sh = "mkdir {}{}".format(folder_path, pdate)
        print(create_sh)


def mkdir_hdfs_folders():
    for month in range(11, 13):
        for day in range(1, 32):
            if day < 10:
                str_day = '0{}'.format(day)
            else:
                str_day = str(day)
            pdate = '2017{}{}'.format(month, str_day)
            create_sh = " /hive/data/user_order/{}".format(pdate)
            print(create_sh, end="")
    for day in range(1, 32):
        if day < 10:
            str_day = '0{}'.format(day)
        else:
            str_day = str(day)
        pdate = '2018{}{}'.format('01', str_day)
        create_sh = " /hive/data/user_order/{}".format(pdate)
        print(create_sh, end="")

    for day in range(1, 30):
        if day < 10:
            str_day = '0{}'.format(day)
        else:
            str_day = str(day)
        pdate = '2018{}{}'.format('02', str_day)
        create_sh = " /hive/data/user_order/{}".format(pdate)
        print(create_sh, end="")
