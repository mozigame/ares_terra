def proc():
    file = open("orderId2.txt", 'r')
    orders = file.readlines()
    for order in orders:
        order = order.strip()
        order_ = order.split(',')
        print('"{}",'.format(order_[0]))

proc()