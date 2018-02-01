import os
import sys
import time

import redis
from rediscluster import StrictRedisCluster

from com.bc.cp.common.mars_constant import MarsConstant
from com.bc.cp.util.properties_util import PropertiesLoad


def get_conn():
    pro_obj = PropertiesLoad("/Users/alex/romance_pro/myPython/first_python_test/com/config/dev/", "redis.properties")
    pro_config = pro_obj.get_properties()
    pool = redis.ConnectionPool(host=pro_config[MarsConstant.REDIS_HOST], port=int(pro_config[MarsConstant.REDIS_PORT]),
                                decode_responses=True)  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    r = redis.Redis(connection_pool=pool)

    # r = redis.StrictRedis(host=pro_config[MarsConstant.REDIS_HOST], port=int(pro_config[MarsConstant.REDIS_PORT]))
    return r


def get_cluster_conn():
    try:
        pro_obj = PropertiesLoad(os.getcwd() + "/com/config/dev/", "redis.properties")
        # pro_obj = PropertiesLoad("/Users/alex/romance_pro/myPython/first_python_test/com/config/dev/",
        #                          "redis.properties")
        pro_config = pro_obj.get_properties()
        hosts = str(pro_config[MarsConstant.REDIS_CLUSTER_HOST]).split(",")
        redis_nodes = []
        for h in hosts:
            node = h.split(":")
            redis_nodes.append({'host': node[0], 'port': node[1]})

        # pool = redis.ConnectionPool(host=pro_config[MarsConstant.REDIS_HOST],
        #                                 port=int(pro_config[MarsConstant.REDIS_PORT]),
        #                                 decode_responses=True)  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379

        redis_conn = StrictRedisCluster(startup_nodes=redis_nodes, decode_responses=True)
        return redis_conn
    except Exception as e:
        print('--> get redis cluster conn failed,', str(e))
        sys.exit(1)


def exe_del_redis_keys():
    redis_obj = get_cluster_conn()
    keys = redis_obj.keys('v_c_chase_lock_2018010*')
    start_time = time.time()
    for key in keys:
        redis_obj.delete(key)

    print('expendTime : ', (time.time() - start_time))


def exe_pipeline_del_redis_keys(match_key):
    redis_obj = get_cluster_conn()
    pipe = redis_obj.pipeline()
    keys = redis_obj.keys(match_key)
    start_time = time.time()
    print('keys len is : ', len(keys))
    for i in range(len(keys)):
        pipe.delete(keys[i])
        if i % 200 == 0:
            pipe.execute()
            print('expend time : ', time.time() - start_time, i)
    for i in range(len(keys)):
        pipe.delete(keys[i])
    pipe.execute()


def exe_keys(match_key):
    redis_obj = get_cluster_conn()
    keys = redis_obj.keys(match_key)
    print('keys size :', len(keys))
    for key in keys:
        print(key)
    print('keys size : ', len(keys))


def get_keys(key):
    redis_obj = get_cluster_conn()
    value =redis_obj.get(key)
    
    print('key :', key)
   
    print('value : ', value)


def set_keys(key,value):
    redis_obj = get_cluster_conn()
    value =redis_obj.set(key,value,3000)
    
    print('key :', key)
   
    print('value : ', value)
print(os.getcwd())

exe_keys('v_c_chase_lock_*2018011*')
