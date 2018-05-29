from payment.config import *
from utils.request_util import *

path = {
    'plat_trad_stat_list': ['/apis/plat/trade/statList',
                            ('startTime', 'endTime'), 'get', '出入款账目汇总',
                            ''],
}


class PaymentResource:

    def plat_trad_stat_list(self, startTime=None, endTime=None):
        pc = PathConfig(path_name='plat_withhold_stats', path=path, Config=Config)
        data = {'startTime': startTime, 'endTime': endTime}
        return RequestServer(pc, data).request()
