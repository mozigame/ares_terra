import random

str_num = '098123765qwertyuiopasdfghjlzxcvbnm'
str_letter = ''


def proc():
    file = open("orderId2.txt", 'r')
    orders = file.readlines()
    orders = ['213c20180513121965350prn,111', '213k1526213941891655d0q8d,111']
    str4_old = []
    str4_new = []
    order_ids_new = []
    order_ids_old = []
    member_ids = []
    for orderIdJoin in orders:
        orderIdJoin = orderIdJoin.strip()
        orderId = orderIdJoin.split(",")[0]
        member_id = orderIdJoin.split(",")[1]
        member_ids.append(member_id)
        a_old = orderId.strip()[-4:]
        str4_old.append(a_old)
        a_join = get_range_num() + get_range_num() + get_range_num() + get_range_num()
        print("orderId:{}, a_ori:{}, a_join:{}".format(orderId.strip(), a_old, a_join))
        while True:
            flag = check_same(str4_new, a_join, str4_old, a_old)
            if flag:
                break
            else:
                a_join = get_range_num() + get_range_num() + get_range_num() + get_range_num()
        str4_new.append(a_join)

        print()
        order_ids_new.append(orderId.strip()[:-4] + a_join)
        order_ids_old.append(orderId.strip())
    print(order_ids_new)
    print(order_ids_old)
    print("\n\n")
    for i in range(0, order_ids_new.__len__()):
        print("insert into test.temp_balance(cidfrombalance,order_id, order_id_new ) values({},'{}','{}');".
              format(member_ids[i], order_ids_old[i], order_ids_new[i]))

    for i in order_ids_new:
        if order_ids_old.__contains__(i):
            print('has exist')


def check_same(str4_new, a_join, str4_old, a_old):
    if str4_new.__contains__(a_join) or str4_old.__contains__(a_join):
        print("has same str4_o , a_join:{}, a_ori:{}".format(a_join, a_old))
        return False
    # if str4_old.__contains__(a_join):
    #     print("has same str4_ori , a_join:{}, a_ori:{}".format(a_join, a_old))
    #     return False
    return True


def get_range_num():
    return str_num[random.randint(0, str_num.__len__() - 1)]
    # ind = random.randint(0, 1)
    # if ind == 0:
    #     return str_num[random.randint(0, str_num.__len__() - 1)]
    # elif ind == 1:
    #     return str_letter[random.randint(0, str_letter.__len__() - 1)]


proc()
