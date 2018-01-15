import os
from pymongo import MongoClient
from com.bc.cp.util.properties_util import PropertiesLoad


def __conn_config():
    pro_obj = PropertiesLoad(os.getcwd() + "/", "mongo.properties")
    return pro_obj.get_properties()


def get_conn():
    conn_config = __conn_config()
    conn = MongoClient(conn_config['host'])
    return conn.venus


db=get_conn()
print(db.collection_names())
