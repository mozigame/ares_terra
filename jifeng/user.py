import hashlib
import re

import requests
import time


class UserService:
    X_FORWARDED_FOR = "163.125.70.177"
    PROXY_CLIENT_IP = "163.125.70.177"
    WL_PROXY_CLIENT_IP = "163.125.70.177"

    ip_headers = ["123.161.16.20",
                  "122.136.212.132",
                  "113.110.229.185",
                  "1.195.60.182",
                  "113.200.214.164",
                  "122.72.18.35",
                  "119.28.152.208",
                  "114.215.95.188",
                  "118.212.137.135",
                  "202.38.92.100",
                  "139.224.80.139",
                  "122.72.18.34",
                  "120.26.110.59",
                  "1.196.161.172",
                  "114.113.126.82",
                  "14.115.107.99",
                  "218.241.234.48",
                  "112.250.65.222",
                  "183.56.177.130",
                  "1.196.161.170",
                  "120.77.254.116",
                  "120.78.78.141",
                  "125.46.0.62",
                  "114.250.25.19",
                  "59.50.68.34",
                  "27.37.46.19",
                  "203.174.112.13",
                  "27.37.47.173",
                  "124.237.83.14",
                  "163.125.194.26",
                  "27.191.234.69",
                  "101.37.79.125",
                  "222.186.34.206",
                  "110.172.220.197",
                  "110.52.8.172",
                  "220.186.177.93",
                  "1.192.241.110",
                  "58.255.38.124",
                  "113.106.195.98",
                  "183.33.192.247",
                  "115.229.93.149",
                  "180.105.127.42",
                  "121.231.154.135",
                  "115.239.79.37",
                  "116.19.98.117",
                  "123.139.56.238",
                  "121.34.19.125",
                  "106.113.242.247",
                  "163.125.157.178",
                  "220.186.143.103",
                  "222.64.130.239",
                  "120.92.119.120",
                  "163.125.115.243",
                  "222.223.96.122",
                  "118.81.248.214",
                  "121.201.33.100",
                  "183.172.172.172",
                  "113.118.98.140",
                  "221.217.52.2",
                  "171.37.174.59",
                  "123.14.229.81",
                  "1.119.193.36",
                  "14.115.107.148",
                  "211.80.62.74",
                  "218.20.54.56",
                  "112.95.22.248",
                  "14.115.105.249",
                  "14.115.107.13",
                  "163.125.253.155",
                  "180.106.86.33",
                  "123.138.89.133",
                  "121.34.48.157",
                  "101.6.97.134",
                  "110.85.245.203",
                  "59.78.2.140",
                  "118.81.68.149",
                  "14.115.105.19",
                  "14.117.208.66",
                  "14.118.204.208",
                  "157.0.95.57",
                  "182.88.47.241",
                  "218.6.145.11",
                  "182.88.130.77",
                  "210.42.41.54",
                  "120.92.119.187",
                  "112.67.174.11",
                  "115.229.113.221",
                  "222.186.45.132",
                  "163.125.253.156",
                  "114.228.74.81",
                  "114.228.74.222",
                  "114.101.43.129",
                  "202.98.197.245",
                  "59.78.34.119",
                  "222.186.21.43",
                  "222.186.12.102",
                  "171.36.173.250",
                  "27.44.168.156",
                  "115.183.11.158",
                  "222.186.31.157"]

    def __init__(self, account, password, code=None):
        self.account = account
        self.password = password

    def login(self):
        server = "http://115.144.238.217:8082"
        # server = "http://192.168.8.113:8080"
        # r = requests.get(server + "/login")
        # r.encoding = 'utf8'
        # print(r.text)
        # m = re.search('data-token=".*"', r.text)
        # token = ''
        # if m:
        #     m = re.search('".*"', m.group())
        #     m = re.search('[^"].*[^"]', m.group())
        #     token = m.group()
        #     print(token)
        token = 'null'
        m = hashlib.md5()
        m.update(self.password.encode(encoding='utf8'))
        md5Pwd = m.hexdigest()
        print("first md5 : %s" % md5Pwd)
        m1 = hashlib.md5()
        m1.update((md5Pwd + token).encode(encoding='utf8'))
        md5Pwd2 = m1.hexdigest()
        print("second sour : %s, result : %s" % (md5Pwd + token, md5Pwd2))
        for ip in UserService.ip_headers:
            headers = {"Content-Type": 'application/json;charset=UTF-8',
                       'User-Agent': 'Chrome/64.0.3282.167',
                       'x-forwarded-for': ip,
                       'Proxy-Client-IP': ip,
                       'WL-Proxy-Client-IP': ip}
            # url = "http://115.144.238.217:8082/login"
            url = server + "/login?account=%s&password=%s" % (self.account, md5Pwd2)
            print("url: %s " % url)
            result = requests.post(url, headers=headers, timeout=50)
            print(result.text)
            time.sleep(1)


if __name__ == '__main__':
    userService = UserService(account='jasontest', password='123456789')
    result = userService.login()
    print(result.text)

# import hashlib
# data='123456789'
# m = hashlib.md5(data.encode(encoding='gb2312'))
# print(m.hexdigest())
#
#
#
# m = hashlib.md5()
# m.update(b"123456789") #参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
# md5value=m.hexdigest()
# print(md5value)  #bb649c83dd1ea5c9d9dec9a18df0ffe9
