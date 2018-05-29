import multiprocessing

from hermes.config import *
from utils.request_util import *
from constains import AresTerraCons, ENV

path = {
    'repeal_draw': ['/apis/order/exc/pcode/repeal/draw_win', ('lotteryId', "pcode", "pdate",),
                    'post', '撤销一期内的开奖结果', 'MemberBalanceResource'],
    'draw_win_anew': ['/apis/repair/order/number_wrong/draw_win_anew', ('pcode', "pdate", "lotteryId", "winNumber",),
                      'post', '重新开奖', ''],
    'take_back_win_wrong_payoff': ['/apis/repair/order/take_back/win_wrong_payoff',
                                   ('pcode', "pdate", "lotteryId"), 'post', '收回派彩', ''],
    'number_wrong_draw_win_anew': ['/apis/repair/order/number_wrong/draw_win_anew',
                                   ('pcode', "pdate", "lotteryId", "winNumber", "page"), 'post', '重新开奖', ''],
}


# 撤销一期内的开奖结果
def repeal_draw(lotteryId=None, pcode=None, pdate=None):
    pc = PathConfig(path_name='repeal_draw', path=path, Config=Config)
    data = {"lotteryId": lotteryId, "pcode": pcode, "pdate": pdate}
    return RequestServer(pc, data).request()


# 重新开奖
def draw_win_anew(lotteryId=None, pcode=None, pdate=None, winNumber=None):
    pc = PathConfig(path_name='draw_win_anew', path=path, Config=Config)
    data = {"lotteryId": lotteryId, "pcode": pcode, "pdate": pdate, "winNumber": winNumber, "page": 1}
    return RequestServer(pc, data).request()


# 收回派彩
def take_back_win_wrong_payoff(lotteryId=None, pcode=None, pdate=None):
    pc = PathConfig(path_name='take_back_win_wrong_payoff', path=path, Config=Config)
    data = {"lotteryId": lotteryId, "pcode": pcode, "pdate": pdate}
    return RequestServer(pc, data).request()


# 重新开奖
def number_wrong_draw_win_anew(pcode=None, pdate=None, lotteryId=None, winNumber=None, page=None):
    pc = PathConfig(path_name='number_wrong_draw_win_anew', path=path, Config=Config)
    data = {"lotteryId": lotteryId, "pcode": pcode, "pdate": pdate, "winNumber": winNumber, "page": page}
    return RequestServer(pc, data).request()


if __name__ == "__main__":
    get_token('plat')
    # result = repeal_draw(lotteryId=16, pcode=20180403043, pdate=20180403)
    # print(result.text)
    # result = draw_win_anew(lotteryId=106, pcode=201804120982, pdate=20180412, winNumber="1,1,1")
    # print(result.text)
    # result = take_back_win_wrong_payoff(lotteryId=32, pcode=201804261013, pdate=20180426)
    # print(result.text)
    result = number_wrong_draw_win_anew(lotteryId=32, pcode=201804261074, pdate=20180426, winNumber="8,9,9,8,9", page=1)
    print(result.text)
