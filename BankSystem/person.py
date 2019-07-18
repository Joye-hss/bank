'''

类名：Person
属性：姓名  身份证号   手机号  卡 
行为：开户,查询,取款,存款,转账,改密，挂失,解锁,销户,（补卡未实现），销户,退出

'''
# from atm import ATM  

class Person(object):

    def __init__(self,name,identity,phoneNum,card=None):
        self.name = name
        self.identity = identity
        self.phoneNum = phoneNum
        self.card = card

    def newAccount(self,atm):
        atm.newAccount()

    def checkMoney(self, atm):
        atm.checkMoney()

    def saveMoney(self, atm):
        atm.saveMoney()

    def getMoney(self, atm):
        atm.getMoney()

    def transferMoney(self, atm):
        atm.transferMoney()

    def closeAccount(self, atm):
        atm.closeAccount()

    def lockAccount(self, atm):
        atm.lockAccount()

    def unlockAccount(self, atm):
        atm.unlockAccount()

    def changePassword(self, atm):
        atm.changePassword()
    
    # 此部分未实现
    # def reissueCard(self, atm):
    #     atm.reissueCard()

    def exit(self, atm):
        atm.exit()
