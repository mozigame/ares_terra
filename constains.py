import os

global_cons = {
    "local": {

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
        "default_appid": 'xqtest',
        "default_origin": 'http://cs.88bccp.com',
        "default_plat_info_id": 45,
        "download_pic": 'http://api.88bccp.com/uaa/apid/member/code/get?width=142&height=50'
    }
}


class ENV():
    LOCAL = 'local'
    TEST = 'test'
    PROD = 'prod'


class AresTerraCons():
    X_FORWARDED_FOR = "163.125.70.177"
    PROXY_CLIENT_IP = "163.125.70.177"
    WL_PROXY_CLIENT_IP = "163.125.70.177"
    DEFAULT_ADD_MEM_COUNT = 100
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
