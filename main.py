from  com.bc.cp.util.redis_util import *
from lxml import etree
import sys

if __name__ == '__main__':

    # exe_pipeline_del_redis_keys('_bet_userOrStatusSet*')
    if len(sys.argv) > 1:
        if sys.argv[1] == 'delete':
            exe_pipeline_del_redis_keys(sys.argv[2] + "*")
        elif sys.argv[1] == 'get':
            exe_keys(sys.argv[2] + "*")
        else:
            print('use valid command')
    else:
        print('no redis match key')



