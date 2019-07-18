'''
提款机：
类名：ATM
属性：
行为：开户,查询,取款,存储,转账,销户,挂失,解锁,改密,退出
'''
from check import Check
from card import Card
from readAppendCard import ReadCard,AppendCard
import random
import time


class ATM(object):
    # 开户
    def __init__(self):
        self.check = Check()
        self.readCard = ReadCard()
        self.appendCard = AppendCard()
        self.cards = self.readCard.read()
    def newAccount(self):
        # 输入身份证号和手机号
        pnum = self.check.phoneNumInput()
        iden = self.check.identifyInput()
        print("正在执行开户程序，请稍候...")

        while True:
            # cardId = str(random.randrange(100000, 10000000))
            # cardId = str(random.sample(["0","1","2","3","4","5","6","7","8","9"],6))
            # zfill()生成指定位数随机数，右对齐，前边0补齐
            # random.randint(start,end)生成随机数
            cardId = str(random.randint(0,999999)).zfill(6)

            if cardId[0] == '0':
                continue
            if self.check.isCardIdExist(self.cards,cardId) == False:
                break
            else:
                continue

        # 初始化卡号密码，卡里的钱，卡的锁定状态
        card = Card(cardId, '000000', 0, iden, pnum , 'False')

        self.appendCard.append(card)
        print("开户成功！")
        print("您的卡号为%s，密码为%s,余额为%d。"%(cardId,'000000',0))
        print("请牢记密码，不要把密码泄露给他人。")
        # 更新卡号列表
        self.cards = self.readCard.read()
        return True

    # 查询
    def checkMoney(self):
        card = self.check.isCardExist(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        print("您的余额为%d元！" % card.cardMoney)
        time.sleep(1)
        return card.cardMoney
    
    # 存款
    def saveMoney(self):
        cardId = input("请输入您的账户：")
        card = self.check.isCardIdExist(self.cards,cardId)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        for card in self.cards:
            if cardId ==card.cardId:
                count = 3
                while count:
                    count -=1
                    password = input("请输入您的账户密码：\n")
                    if password == card.cardPassword:
                        money =int(input("请输入您要存的钱数：\n"))
                        index = self.cards.index(card)
                        self.cards[index].cardMoney += money
                        self.writeCard()
                        print("存款成功！您的账户余额为%d元！"%self.cards[index].cardMoney)
                        time.sleep(1)
                        return  
                    else:
                        if count !=0:
                            print("密码错误！您还有%s次机会输入密码！"%count)
                            time.sleep(1)
                        elif count == 0:
                            print("密码错误！已结束本次服务！")
                            time.sleep(1)
                            break
                            continue
                break


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

        # mon = int(input("请输入您要取的钱："))
        # # index()索引找到
        # # if isinstance(mon,int):
        # index = self.cards.index(card)
        # if mon > self.cards[index].cardMoney:
        #     print("余额不足，您当前余额为%d元!"%self.cards[index].cardMoney)
        #     time.sleep(1)
        #     return
        # self.cards[index].cardMoney -= mon
        # self.writeCard()

        # print("取款成功！你卡上的余额为%d元!"%self.cards[index].cardMoney)
        # time.sleep(1)
        # pass

    # def getMoney(self):
    #     card = self.check.isCardExist(self.cards)
    #     if self.check.isCardLock(self.cards,card.cardId):
    #         return
    #     mon = input("请输入您要取的钱：")
    #     # index()索引找到
    #     if isinstance(mon, str):
    #         print("您的输入有误！")
    #         pass

    #     if isinstance(mon,int):
    #         index = self.cards.index(card)
    #         if mon > self.cards[index].cardMoney:
    #             print("余额不足，您当前余额为%d元!"%self.cards[index].cardMoney)
    #             time.sleep(1)
    #             return
    #         self.cards[index].cardMoney -= mon
    #         self.writeCard()
    #         print("取款成功！你卡上的余额为%d元!"%self.cards[index].cardMoney)
    #         time.sleep(1)
    #         pass

        # return



    # 转账
    def transferMoney(self):
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
                        while True:
                            cardId_another = input("请输入对方账户:\n")
                            card_another = self.check.isCardIdExist(self.cards, cardId_another)
                            if card_another == False:
                                print("该账户不存在！")
                                if self.check.isSure("继续转账"):
                                    continue
                                else:
                                    time.sleep(1)
                                    return
                            else:
                                break
                        index = self.cards.index(card)
                        while True:
                            money = int(input("您当前账户余额为%s，请输入转账金额：\n"%self.cards[index].cardMoney))
                            if money > self.cards[index].cardMoney:
                                print("您的账户余额不足！您当前余额为%s"%self.cards[index].cardMoney)
                                if self.check.isSure("继续转账"):
                                    continue
                                else:
                                    return
                            else:
                                self.cards[index].cardMoney -= money
                                break
                        index_another = self.cards.index(card_another)
                        self.cards[index_another].cardMoney += money
                        self.writeCard()

                        print("转账成功！您卡上余额为%d元！"%self.cards[index].cardMoney)
                        time.sleep(1)
                        return
                    else:
                        if count != 0:
                            print("密码错误！您还有%s次机会输入密码！"%count)
                            continue
                        else: 
                            # count == 0:
                            print("密码错误！已结束本次服务！")
                            break
                            # continue

        # while True:
        #     cardId = input("请输入对方的账号：")
        #     cardOther = self.check.isCardIdExist(self.cards,cardId)
        #     if cardOther == False:
        #         print("账号不存在")
        #         if self.check.isSure("继续转账"):
        #             continue
        #         else:
        #             time.sleep(1)
        #             return
        #     else:
        #         break
        # index = self.cards.index(card)
        # while True:
        #     mon = int(input("您当前的账户余额为%d,请输入转账金额："%self.cards[index].cardMoney))

        #     if mon > self.cards[index].cardMoney:
        #         print("余额不足，您当前余额为%d元!" % self.cards[index].cardMoney)
        #         if self.check.isSure("继续转账"):
        #             continue
        #         else:
        #             time.sleep(1)
        #             return
        #     else:
        #         self.cards[index].cardMoney -= mon
        #         break
        # indexOther = self.cards.index(cardOther)
        # self.cards[indexOther].cardMoney += mon
        # self.writeCard()

        # print("转账成功！你卡上的余额为%d元!" % self.cards[index].cardMoney)
        # time.sleep(1)
        # pass
    
    # 销户
    def closeAccount(self):
        card = self.check.isCardInfoSure(self.cards)
        if card:
            self.cards.remove(card)
            self.writeCard()

            print("销户成功！")
            time.sleep(1)
        pass
    # 挂失
    def lockAccount(self):
        card = self.check.isCardInfoSure(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        if card:
            index = self.cards.index(card)
            self.cards[index].cardLock = "True"
            self.writeCard()

            print("挂失成功！")
            time.sleep(1)
        pass
    # 解锁
    def unlockAccount(self):
        card = self.check.isCardInfoSure(self.cards)
        index = self.cards.index(card)
        self.cards[index].cardLock = "False"
        self.writeCard()

        print("解锁成功！")
        time.sleep(1)
        pass
    
    # 改密
    def changePassword(self):
        card = self.check.isCardInfoSure(self.cards)
        if self.check.isCardLock(self.cards, card.cardId):
            return
        # 输入旧密码
        while True:
            password = input("请输入旧密码")
            if self.check.isCardPasswordSure(password,card.cardPassword):
                break
            else:
                print("卡号密码输入错误！")
                if self.check.isSure("修改密码"):
                    continue
                else:
                    return
        #输入新密码
        while True:
            try:
                newpassword = input("请输入6位数字新密码：\n")
                #此处只能确保输入全为数字时，当输入有字母时会报错
                if type(int(newpassword)) == int and len(newpassword)==6:
                    break
            except:
                print("密码必须由6位数字组成！")
                # continue
        index = self.cards.index(card)
        self.cards[index].cardPassword = newpassword
        while True:
            #加入控制次数？
            newpassword_2 = input("请再次输入新密码以确认您的密码：\n")
            if newpassword_2 == self.cards[index].cardPassword:
                # self.cards[index].cardPassword = str(self.cards[index].cardPassword)
                self.writeCard()
                print("修改密码成功！")
                break
            else:
                print("密码错误，请重新输入！")
                continue
        time.sleep(1)
        pass
    
    #补卡
    def reissueCard(self):
        # card = self.check.isCardInfoSure(self.cards)
        rnum = self.check.phoneNumInput()
        ridnum = self.check.identifyInput()
        print("正在为您补办银行卡，请稍后...")
        while True:
            # cardId = str(random.randrange(100000,10000000))
            cardId = str(random.randint(0,999999)).zfill(6)
            if self.check.isCardIdExist(self.cards,cardId) == False:
                break
            else:
                continue
        card = Card(cardId,'000000', 0, ridnum, rnum , 'False')
        self.appendCard.append(card)
        print("补卡成功！您的卡号为为:%s,密码为：%s,余额为：%d。" %(cardId,'000000',0))
        print("请牢记密码，不要把密码泄露给他人。")
        self.cards = self.readCard.read()
        return True

    
   

    # 写入文件
    def writeCard(self):
        self.appendCard.append('', w='w')
        for card in self.cards:
            self.appendCard.append(card)
    # 退出
    def exit(self):
        if self.check.isSure("退出"):
            return True
        else:
            return False
        pass

# 测试
def main():
    atm = ATM()
    print(atm.newAccount())

if __name__ == '__main__':
    main()


