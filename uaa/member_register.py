from time import sleep
import urllib
from urllib import request, parse
import utils.request_util as request_util
from uaa.config import *
from concurrent.futures import ThreadPoolExecutor
import random
import os
import threading
import threadpool
import multiprocessing
import uaa.qr.cp_discern_qr as cp_qr
import json
from constains import AresTerraCons, getRootPath

path = {
    'check_account': ['/apid/data/member/check_account', ('appid', 'login'), 'post',
                      '检查账号是否存在', 'MemberRegistResource'],
    'create_member': ['/apid/data/member/checkOrCreateMemberBcbaochi', (
        'acType', "appid", "curType", "referrals", "login", "method", "oddType", "password", "realName", "mobile",
        'passwordPay', "bankId", "code", "bankCode", "bankAddress", "bankCard", "source"), 'post',
                      '创建账号', 'CurrentUserResource'],
    'member_login': ['/apid/member/login', ('grant_type', "username", "password", "code", "source",), 'post',
                     '会员登录', 'CurrentUserResource'],
}

aresCons = AresTerraCons()


class switch_c():
    """根据数字返回账号"""

    def case(self, andomNum, num):
        if andomNum == 1:
            return '{}aes{}NUB'.format(num, int(num / 5.3))
        if andomNum == 2:
            return '{}MED{}uIE'.format(num, int(num / 7.2))
        if andomNum == 3:
            return '{}POfeN{}ERD'.format(num, int(num / 9.8))
        if andomNum == 4:
            return '{}PeN{}ERD'.format(num, int(num / 6.6))

    def get_pwd(self, member_name):
        return member_name + '1'


def check_account(appid=None, login=None, origin=None):
    """检查账号是否已经存在"""
    if configureRead.configObj is None:
        configureRead.configObj = configureRead.initConfig()
    if origin is None:
        origin = configureRead.configObj.get('member', 'origin')
        if not origin:
            raise Exception('no origin')
    if appid is None:
        appid = aresCons.getDefaultAppId()
    pc = request_util.PathConfig(Config=Config, path_name='check_account', path=path)
    headers = {'Origin': origin}
    params = {'appid': appid, 'login': login}
    result = request_util.RequestServer(pc, params).request(self_headers=headers)
    return result


# acType=1, appid=appid, curType="CNY", referrals="", login="pefft_1", method="mc",
#                   oddType="a", password="pefft_11", realName="匹配", mobile="15566773455", passwordPay="1111",
#                   bankId=11, code=4444, bankCode="NBB", bankAddress="名博银行", bankCard=7777999988880099,
#                   source=2 , origin=None
# 创建账号
def create_member(acType="1", appid=None, curType="CNY", referrals="", login="pefft_1", method="mc",
                  oddType="a", password="pefft_11", realName=None, mobile="15566773455", passwordPay="1111",
                  bankId=11, code=4444, bankCode="NBB", bankAddress="名博银行", bankCard=7777999988880099,
                  source=2, origin=None):
    if configureRead.configObj is None:
        configureRead.configObj = configureRead.initConfig()
    if origin is None:
        origin = aresCons.getDefaultOrigin()
        if not origin:
            raise Exception('--> no origin')
    if appid is None:
        appid = aresCons.getDefaultAppId()
    pc = request_util.PathConfig(Config=Config, path_name='create_member', path=path)
    vcode = cp_qr.get_current_code()
    if not vcode[0] or not vcode[1]:
        raise Exception('--> code is null')

    headers = {'Origin': origin, "Content-Type": 'application/json;charset=UTF-8',
               'Authorization': 'Basic d2ViX2FwcDo=', 'User-Agent': 'Chrome/64.0.3282.167',
               'clientId': vcode[0], 'x-forwarded-for': AresTerraCons.X_FORWARDED_FOR,
               'Proxy-Client-IP': AresTerraCons.PROXY_CLIENT_IP,
               'WL-Proxy-Client-IP': AresTerraCons.WL_PROXY_CLIENT_IP}
    params = {'acType': acType, 'appid': appid, 'curType': "CNY", 'referrals': "", 'login': login, 'method': "mc",
              'oddType': "a", 'password': password, 'realName': realName, 'mobile': mobile,
              'passwordPay': "1111", 'code': vcode[1], 'source': source, 'origin': origin}
    self_proxies = {'http': 'http://119.28.152.208:80'}
    result = request_util.RequestServer(pc, str(params).replace("'", '"').encode('utf-8')). \
        request(self_headers=headers, self_proxies=self_proxies)
    return result


def create_member_account(num):
    """生成登录的会员账号"""
    switch = switch_c()
    account = switch.case(random.randint(1, 4), num)
    result = check_account(login=account)
    result = result.json()
    print('--> checkout_account result :', account, result, sep='\t')
    if not result['data']:
        return (True, account)
    else:
        print('--> {} has exist'.format(account))
        return (False, account)


def get_real_name():
    """生成真实名字"""
    c = random.randint(2, 5)
    real_name = ''
    t1 = request_util.name_cans[random.randint(0, request_util.name_cans_len - 1)]
    t2 = request_util.name_cans[random.randint(0, request_util.name_cans_len - 1)]
    t3 = request_util.name_cans[random.randint(0, request_util.name_cans_len - 1)]
    t4 = request_util.name_cans[random.randint(0, request_util.name_cans_len - 1)]
    t5 = request_util.name_cans[random.randint(0, request_util.name_cans_len - 1)]
    if c == 2:
        real_name = t1 + t2
    elif c == 3:
        real_name = t1 + t2 + t3
    elif c == 4:
        real_name = t1 + t2 + t3 + t4
    elif c == 5:
        real_name = t1 + t2 + t3 + t4 + t5
    return real_name


def get_phone_number():
    """随机生成电话号码"""
    c1 = random.randint(0, 9)
    c2 = random.randint(0, 9)
    c3 = random.randint(0, 9)
    c4 = random.randint(0, 9)
    c5 = random.randint(0, 9)
    c6 = random.randint(0, 9)
    c7 = random.randint(0, 9)
    c8 = random.randint(0, 9)
    return "151{}{}{}{}{}{}{}{}".format(c1, c2, c3, c4, c5, c6, c7, c8)


def get_password(account):
    """生成会员密码"""
    return account + '1'


def create_member_core(i):
    """批量注册会员"""
    regist_mem_file_path = "{}uaa{}conf{}{}{}member_{}_{}.txt".format(getRootPath(), os.sep, os.sep, Config.env, os.sep,
                                                                      aresCons.getDefaultPlatInfoId(), i)
    regist_suc_file_path = "{}uaa{}conf{}{}{}regist_suc_{}.txt".format(getRootPath(), os.sep, os.sep, Config.env,
                                                                       os.sep, aresCons.getDefaultPlatInfoId())
    regist_mem_file = open(regist_mem_file_path, 'a', encoding='utf-8')
    regist_suc_file = open(regist_suc_file_path, 'a', encoding='utf-8')
    try:
        for k in range(47, 67):
            login = create_member_account(num=k)
            if not login[0]:
                continue
            real_name = get_real_name()
            mobile = get_phone_number()
            str = "{}\t{}\t{}\t{}\n".format(aresCons.getDefaultPlatInfoId(), aresCons.getDefaultAppId(), login[1],
                                            real_name)
            regist_mem_file.writelines(str)
            account = login[1]
            result = create_member(login=account, password=get_password(account), realName=real_name,
                                   mobile=mobile)
            print("--> checkOrCreateMemberBcbaochi result : " + result.text)
            result = result.json()
            if result['err'] == 'SUCCESS':
                print('--> create user success', account, result)
                regist_suc_file.write(account + '\n')
            else:
                print('--> create user failed : ', account, result['cnMsg'])

    finally:
        regist_mem_file.close()
        regist_suc_file.close()


def member_login(appid=None, account=None):
    """会员登录"""
    if not appid:
        appid = aresCons.getDefaultAppId()
    password = get_password(account)
    vcode = cp_qr.get_current_code()
    if not vcode[0] or not vcode[1]:
        raise Exception('--> code is null')
    params = {'grant_type': AresTerraCons.GRANT_TYPE, 'username': appid + "|" + account, "password": password,
              'code': vcode[1], 'source': AresTerraCons.SOURCE}
    headers = {'Origin': aresCons.getDefaultOrigin(),
               "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
               'Authorization': 'Basic d2ViX2FwcDo=',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Mobile Safari/537.36',
               'clientId': vcode[0], 'x-forwarded-for': AresTerraCons.X_FORWARDED_FOR,
               'Proxy-Client-IP': AresTerraCons.PROXY_CLIENT_IP,
               'WL-Proxy-Client-IP': AresTerraCons.WL_PROXY_CLIENT_IP}
    pc = request_util.PathConfig(Config=Config, path_name='member_login', path=path)
    # print(json.dumps(params))
    # params = str(params).replace("'",'"')
    result = request_util.RequestServer(pc, params ). \
        request(self_headers=headers)
    return result


def urllib_create_mem(proxy_ip=None):
    """urllib 测试注册会员"""
    real_name = get_real_name()
    mobile = get_phone_number()

    account = 'b33f' + request_util.timestamp_datestr()

    vcode = cp_qr.get_current_code()
    if not vcode[0] or not vcode[1]:
        raise Exception('--> code is null')

    clientId = vcode[0]
    code = vcode[1]
    headers = {'Origin': aresCons.getDefaultOrigin(), "Content-Type": 'application/json;charset=UTF-8',
               'Authorization': 'Basic d2ViX2FwcDo=', 'User-Agent': 'Chrome/64.0.3282.167',
               'clientId': clientId}
    params = {'acType': "1", 'appid': aresCons.getDefaultAppId(), 'curType': "CNY", 'referrals': "",
              'login': account,
              'method': "mc",
              'oddType': "a", 'password': "11111", 'realName': real_name, 'mobile': mobile,
              'passwordPay': "1111", 'code': code, 'source': "2", 'origin': aresCons.getDefaultOrigin()}
    if not proxy_ip:
        proxy_ip = {'http': 'http://110.73.7.28:9999'}
    proxy_handler = urllib.request.ProxyHandler(proxy_ip)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    print(params)
    data = str(params).replace("'", '"').encode('utf-8')
    req = urllib.request.Request(url="http://121.58.234.210:19093/uaa/apid/data/member/checkOrCreateMemberBcbaochi",
                                 data=data, headers=headers)
    response = urllib.request.urlopen(req, timeout=25)
    html = response.read().decode('utf-8')
    print("-->  regist member result : ", html)
    global null
    null = ''
    html = eval(html)


if __name__ == '__main__':
    Config.env = 'prod'
    aresCons = AresTerraCons(env=Config.env)
    """批量创建会员"""
    create_member_core(1)
    # urllib_create_mem()
    # result = member_login(account='48MED6uIE').json()
    # if result['err']=='SUCCESS':
    #     print(result['data']['access_token'])
    # print(result)

