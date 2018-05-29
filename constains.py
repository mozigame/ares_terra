import os

global_cons = {
    "local": {
        "default_appid": 'xq_double',
        "default_origin": 'http://cp.baochi888.com',
        "default_plat_info_id": 45,
        "download_pic": 'http://121.58.234.210:19093/uaa/apid/member/code/get?width=142&height=50'
    },
    "test": {
        "default_appid": 'xq_double',
        "default_origin": 'http://cp.baochi888.com',
        "default_plat_info_id": 45,
        "download_pic": 'http://121.58.234.210:19093/uaa/apid/member/code/get?width=142&height=50'
    },
    "prod": {
        "uaa": {},
        "hermes": {},
        # "default_appid": 'dafacai1188',
        # "default_origin": 'http://www.106235.com',
        # "default_plat_info_id": 48,
        #
        # "default_appid": 'dafacai1188',
        # "default_origin": 'http://www.106235.com',
        # "default_plat_info_id": 48,

        "default_appid": 'blc888',
        "default_origin": 'http://7747bb.com',
        "default_plat_info_id": 44,
        "download_pic": 'http://api.88bccp.com/uaa/apid/member/code/get?width=142&height=50'
    },
    "lottery": [
        {'lotteryId': 1, 'issue': "cq_ssc", 'acType': 1, 'lotteryName': "重庆时时彩"},
        {'lotteryId': 2, 'issue': "cq_ssc", 'acType': 2, 'lotteryName': "重庆时时彩双面彩"},
        {'lotteryId': 3, 'issue': "jx_11x5", 'acType': 1, 'lotteryName': "江西11选5"},
        {'lotteryId': 4, 'issue': "jx_11x5", 'acType': 2, 'lotteryName': "江西11选5双面彩"},
        {'lotteryId': 5, 'issue': "js_k3", 'acType': 1, 'lotteryName': "江苏快3"},
        {'lotteryId': 6, 'issue': "js_k3", 'acType': 2, 'lotteryName': "江苏快3双面彩"},
        {'lotteryId': 7, 'issue': "bj_pk10", 'acType': 1, 'lotteryName': "北京PK10"},
        {'lotteryId': 8, 'issue': "bj_pk10", 'acType': 2, 'lotteryName': "北京PK10双面彩"},
        {'lotteryId': 9, 'issue': "xg_lhc", 'acType': 1, 'lotteryName': "香港六合彩"},
        {'lotteryId': 10, 'issue': "xg_lhc", 'acType': 2, 'lotteryName': "香港六合彩双面彩"},
        {'lotteryId': 11, 'issue': "tj_ssc", 'acType': 1, 'lotteryName': "天津时时彩"},
        {'lotteryId': 12, 'issue': "tj_ssc", 'acType': 2, 'lotteryName': "天津时时彩双面彩"},
        {'lotteryId': 13, 'issue': "xj_ssc", 'acTyp': 1, 'lotteryName': "新疆时时彩"},
        {'lotteryId': 14, 'issue': "xj_ssc", 'acType': 2, 'lotteryName': "新疆时时彩双面彩"},
        {'lotteryId': 15, 'issue': "gd_11x5", 'acType': 1, 'lotteryName': "广东11选5"},
        {'lotteryId': 16, 'issue': "gd_11x5", 'acType': 2, 'lotteryName': "广东11选5双面彩"},
        {'lotteryId': 17, 'issue': "sd_11x5", 'acType': 1, 'lotteryName': "山东11选5"},
        {'lotteryId': 18, 'issue': "sd_11x5", 'acType': 2, 'lotteryName': "山东11选5双面彩"},
        {'lotteryId': 19, 'issue': "ah_k3", 'acType': 1, 'lotteryName': "安徽快3"},
        {'lotteryId': 20, 'issue': "ah_k3", 'acType': 2, 'lotteryName': "安徽快3双面彩"},
        {'lotteryId': 21, 'issue': "hub_k3", 'acType': 1, 'lotteryName': "湖北快3"},
        {'lotteryId': 22, 'issue': "hub_k3", 'acType': 2, 'lotteryName': "湖北快3双面彩"},
        {'lotteryId': 23, 'issue': "luckship", 'acType': 1, 'lotteryName': "幸运飞艇"},
        {'lotteryId': 24, 'issue': "luckship", 'acType': 2, 'lotteryName': "幸运飞艇双面彩"},
        {'lotteryId': 25, 'issue': "ssc_beijing", 'acType': 1, 'lotteryName': "北京时时彩"},
        {'lotteryId': 26, 'issue': "ssc_beijing", 'acType': 2, 'lotteryName': "北京时时彩双面彩"},
        {'lotteryId': 27, 'issue': "ssc_taiwan", 'acType': 1, 'lotteryName': "台湾5分彩"},
        {'lotteryId': 28, 'issue': "ssc_taiwan", 'acType': 2, 'lotteryName': "台湾5分彩双面彩"},
        {'lotteryId': 29, 'issue': "pc_dd", 'acType': 1, 'lotteryName': "PC蛋蛋"},
        {'lotteryId': 30, 'issue': "pc_dd", 'acType': 2, 'lotteryName': "PC蛋蛋双面彩"},
        {'lotteryId': 31, 'issue': "qq_ffc", 'acType': 1, 'lotteryName': "QQ分分彩"},
        {'lotteryId': 32, 'issue': "qq_ffc", 'acType': 2, 'lotteryName': "QQ分分彩双面彩"},

        {'lotteryId': 101, 'issue': "bc_ssc", 'acType': 1, 'lotteryName': "秒速时时彩"},
        {'lotteryId': 102, 'issue': "bc_ssc", 'acType': 2, 'lotteryName': "秒速时时彩双面彩"},
        {'lotteryId': 103, 'issue': "bc_11x5", 'acType': 1, 'lotteryName': "秒速11选5"},
        {'lotteryId': 104, 'issue': "bc_11x5", 'acType': 2, 'lotteryName': "秒速11选5双面彩"},
        {'lotteryId': 105, 'issue': "bc_k3", 'acType': 1, 'lotteryName': "秒速快3"},
        {'lotteryId': 106, 'issue': "bc_k3", 'acType': 2, 'lotteryName': "秒速快3双面彩"},
        {'lotteryId': 107, 'issue': "bc_pk10", 'acType': 1, 'lotteryName': "秒速赛车"},
        {'lotteryId': 108, 'issue': "bc_pk10", 'acType': 2, 'lotteryName': "秒速赛车双面彩"},
        {'lotteryId': 109, 'issue': "bc_lhc", 'acType': 1, 'lotteryName': "五分六合彩"},
        {'lotteryId': 110, 'issue': "bc_lhc", 'acType': 2, 'lotteryName': "五分六合彩双面彩"},
        {'lotteryId': 111, 'issue': "bc_ssc_korea", 'acType': 1, 'lotteryName': "韩国1.5分彩"},
        {'lotteryId': 112, 'issue': "bc_ssc_korea", 'acType': 2, 'lotteryName': "韩国1.5分彩双面彩"},
        {'lotteryId': 113, 'issue': "bc_ssc_tokyo", 'acType': 1, 'lotteryName': "东京1.5分彩"},
        {'lotteryId': 114, 'issue': "bc_ssc_tokyo", 'acType': 2, 'lotteryName': "东京1.5分彩双面彩"}
    ]
}


class ENV():
    LOCAL = 'local'
    TEST = 'test'
    PROD = 'prod'


class AresTerraCons():
    X_FORWARDED_FOR = "163.125.70.177"
    PROXY_CLIENT_IP = "163.125.70.177"
    WL_PROXY_CLIENT_IP = "163.125.70.177"
    DEFAULT_ADD_MEM_COUNT = 4
    GRANT_TYPE = 'password'
    SOURCE = '2'
    ENV = ENV.PROD

    def __init__(self, env=None):
        if env:
            AresTerraCons.ENV = env

    def getDefaultAppId(self):
        """获取默认appId"""
        return global_cons[AresTerraCons.ENV]['default_appid']

    def getDefaultOrigin(self):
        """获取默认origin"""
        return global_cons[AresTerraCons.ENV]['default_origin']

    def getDefaultPlatInfoId(self):
        """获取默认平台商id"""
        return global_cons[AresTerraCons.ENV]['default_plat_info_id']

    def getDownloadPic(self):
        """获取验证码接口"""
        return global_cons[AresTerraCons.ENV]['download_pic']


def getRootPath():
    """获取项目的根路径"""
    root_path = os.getcwd()
    return "{}{}{}".format(root_path[0:root_path.find('ares_terra')], "ares_terra", os.sep)
