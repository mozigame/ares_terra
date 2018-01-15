import os
import pymysql
from com.bc.cp.util.properties_util import PropertiesLoad


def __get_conn_config():
    mysql_pro_obj = PropertiesLoad(os.getcwd() + "/", "mysql.properties")
    return mysql_pro_obj.get_properties()


def get_conn():
    # 链接配置信息
    conn_config = __get_conn_config()
    print(conn_config)
    # 打开数据库链接
    try:
        db = pymysql.connect(conn_config['host'],
                             conn_config['user'],
                             conn_config['password'],
                             conn_config['database'],
                             int(conn_config['port']),
                             charset='utf8')
        return db
    except Exception as e:
        print(str(e))
        return None


get_conn()
