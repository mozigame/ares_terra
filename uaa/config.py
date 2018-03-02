from uaa import configureRead

constains = {
    "local": {},
    "test": {

    },
    "prod": {}
}


class Config():
    host = 'http://localhost:9999'
    # host = 'http://192.168.1.109:8083'
    test_host = 'http://121.58.234.210:19093/uaa'
    # test_host = 'http://192.168.0.217:9999'
    prod_host = 'http://api.88bccp.com/uaa'
    LOCAL = 'local'
    TEST = 'test'
    PROD = 'proc'
    env = TEST

    default_appid = 'xqtest'
    default_origin = 'http://cs.88bccp.com'
    default_plat_info_id = 45
    batch_count = 100
