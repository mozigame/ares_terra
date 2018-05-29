import json


def proc():
    file = open('./a1', mode='r')
    balances = file.readlines()
    for bal in balances:
        # print(bal.strip() + "", )
        if bal.strip() is not None:
            obj = json.loads(str(bal).strip())
            print(obj['memberId'], ',')


# proc()

def proc_1():
    file = open('a3', mode='r')
    balances = json.loads(file.read())
    print(balances.__len__())
    amount = 0
    for bal in balances:
        amount += bal['data']['amount']
        print(bal['data']['memberId'], bal['data']['amount'])
    print("amount", amount)


def proc_2():
    file = open('b1', mode='r')
    members = json.loads(file.read().strip())
    for mem in members:
        print("[{},{}],".format(mem['memberId'], mem['amount']))


proc_2()
