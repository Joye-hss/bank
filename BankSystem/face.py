# class Face(object):
#     """docstring for face"""
#     def __init__(self, arg):
#         super(face, self).__init__()
#         self.arg = arg
        

#     def funcInterface(self):
#         # print("\n\n\n")
#         print("*----------Welcome To The Bank----------*")
#         print("|                                       |")
#         print("|      (1)开户           (6)改密        |")
#         print("|      (2)查询           (7)挂失        |")
#         print("|      (3)存款           (8)解锁        |")
#         print("|      (4)取款           (9)补卡        |")
#         print("|      (5)转账           (10)销户       |")
#         print("|      (R)返回           (Q)退出        |")
#         print("|                                       |")
#         print("*---------------------------------------*")


while True:
    ten = input("X：")
    try:
        x = eval(ten)
        if type(x) == int :
            break
    except:
        print("输入错误！")


    pass

#3次怎么判断啊！！
def isCardExist(self,cards):
        cardId = input("请输入账号：")
        for card in cards:
            if cardId == card.cardId:
                count = 3
                while count:
                    try:
                        password = input('请输入密码：')
                        if password == card.cardPassword:
                            return card
                        else:                                            
                            count -= 1
                            if count ==0:
                                break
                                # pass
                            #第三次密码输入错误时，应跳出整个应用
                            # return view.funcInterface()
                            # task = input("请输入您要办理的业务：")
                            # return view.funcInterface()
                            # else:
                            print("密码有误，您还有%s机会输入密码!"%count)
                            # continue
                    except:
                        pass


    # 取款
    def getMoney(self):
        cardId = input("请输入您的账户：\n")
        card = self.check.isCardIdExist(self.cards,cardId)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        for card in self.cards:
            if cardId == card.cardId:
                count = 3
                while count:
                    count -=1
                    password = input("请输入您的账户密码：\n")
                    if password == card.cardPassword:
                        money = int(input("请输入您要取的钱数：\n"))
                        index = self.cards.index(card)
                        if money > self.cards[index].cardMoney:
                            print("您的账户余额不足！您当前余额为%d元！"%self.cards[index].cardMoney)
                            time.sleep(1)
                            return
                        self.cards[index].cardMoney -= money
                        self.writeCard()

                        print("取款成功！您的账户余额为%d元！"%self.cards[index].cardMoney)
                        time.sleep(1)
                        return
                    else:
                        if count != 0:
                            print("密码错误！您还有%s次机会输入密码！"%count)
                        elif count == 0:
                            print("密码错误！已结束本次服务！")
                            break
                            continue
                break