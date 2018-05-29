def proc():
    file = open('d1', 'r')
    order_strs = file.readlines()
    for or_str in order_strs:
        if or_str.strip() is not "" and or_str is not None:
            order_obj = or_str.strip().split("|")
            # print(order_obj)
            # print(order_obj[8].strip(), order_obj[4].strip(), order_obj[5].strip(), order_obj[6].strip(),
            #       order_obj[7].strip())
            print(
                'db.UserOrderPO_20180511_bak_1_1.update({orderId:"%s"},{$set:{orderId:"%s",betTime:NumberLong("%s"),createTime:NumberLong("%s"),modifyTime:NumberLong("%s")}});' % (
                    order_obj[8].strip(), order_obj[4].strip(), order_obj[5].strip(), order_obj[6].strip(),
                    order_obj[7].strip()
                ))


proc()
