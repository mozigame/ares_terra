import sys
import os
from exportmongo.core import user_order_exec

if __name__ == '__main__':
    if sys.argv.__len__() == 0:
        raise Exception("--> no pdate!!")

    print('--> params :{}'.format(str(sys.argv)))
    pdate = int(sys.argv[1].strip())
    user_order_exec.start(pdate)
