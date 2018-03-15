class UserOrderPO():
    def __init__(self, betAmount, betContent, betCount, betMode, chaseCount, ifChase, moneyMode, multiple, payoff,
                 playId, remark):
        self.betAmount = betAmount
        self.betContent = betContent
        self.betCount = betCount
        self.betMode = betMode
        self.chaseCount = chaseCount
        self.ifChase = ifChase
        self.moneyMode = moneyMode
        self.multiple = multiple
        self.payoff = payoff
        self.playId = playId
        self.remark = remark


class UserOrderReq():
    def __init__(self, UserOrderPO, list, amount, lotteryId, operType, pcode, pdate, remark, source, sourceType):
        self.UserOrderPO = UserOrderPO
        self.list = list
        self.amount = amount
        self.lotteryId = lotteryId
        self.operType = operType
        self.pcode = pcode
        self.pdate = pdate
        self.remark = remark
        self.source = source
        self.sourceType = sourceType
