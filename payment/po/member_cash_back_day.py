class MemberCashBackDayPO():
    def __init__(self, cid=None, cashBackId=None, memberId=None, memberAccount=None, agentId=None, agentAccount=None,
                 platInfoId=None, levelId=None, validBetAmount=None, payoff=None, cashBackAmount=None, pdate=None,
                 status=None, createUser=None, createTime=None, modifyTime=None, remark=None, procStatus=None,
                 balance=None, lotteryId=None):
        self.cid = cid
        self.cashBackId = cashBackId
        self.memberId = memberId
        self.memberAccount = memberAccount
        self.agentId = agentId
        self.agentAccount = agentAccount
        self.platInfoId = platInfoId
        self.levelId = levelId
        self.validBetAmount = validBetAmount
        self.payoff = payoff
        self.cashBackAmount = cashBackAmount
        self.pdate = pdate
        self.status = status
        self.createUser = createUser
        self.createTime = createTime
        self.modifyTime = modifyTime
        self.remark = remark
        self.procStatus = procStatus
        self.balance = balance
        self.lotteryId = lotteryId


class MemberTradePO():
    def __init__(self, id=None, memberId=None, memberName=None, agentId=None, agentName=None, levelId=None,
                 levelName=None, platInfoId=None, orderId=None, orderNo=None,
                 orderParentNo=None, tradeAmount=None, balance=None, remark=None, cashRemark=None,
                 merchantName=None, source=None, tradeType=None, actionType=None, dealType=None, flowType=None,
                 chargeType=None,
                 pdate=None, state=0, createTime=None, updateTime=None, times=None, total=None, sumAmount=None,
                 startTime=None, endTime=None):
        self.id = id
        self.memberId = memberId
        self.memberName = memberName
        self.agentId = agentId
        self.agentName = agentName
        self.levelId = levelId
        self.levelName = levelName
        self.platInfoId = platInfoId
        self.orderId = orderId
        self.orderNo = orderNo
        self.orderParentNo = orderParentNo
        self.tradeAmount = tradeAmount
        self.balance = balance
        self.remark = remark
        self.cashRemark = cashRemark
        self.merchantName = merchantName
        self.source = source
        self.tradeType = tradeType
        self.actionType = actionType
        self.dealType = dealType
        self.flowType = flowType
        self.chargeType = chargeType
        self.pdate = pdate
        self.state = state
        self.createTime = createTime
        self.updateTime = updateTime
        self.times = times
        self.total = total
        self.sumAmount = sumAmount
        self.startTime = startTime
        self.endTime = endTime


# 人工取款
class SystemDrawCondition():
    def __init__(self, ipAddr=None,
                 memberId=None,
                 memberName=None,
                 agentId=None,
                 agentName=None,
                 levelId=None,
                 levelName=None,
                 actionType=None,
                 drawAmount=None,
                 drawRemark=None):
        self.ipAddr = ipAddr
        self.memberId = memberId
        self.memberName = memberName
        self.agentId = agentId
        self.agentName = agentName
        self.levelId = levelId
        self.levelName = levelName
        self.actionType = actionType
        self.drawAmount = drawAmount
        self.drawRemark = drawRemark
