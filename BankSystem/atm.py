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
            if self.check.isCardIdExist(self.cards,cardId) == False:
                break
            else:
                continue
        # 初始化卡号密码，卡里的钱，卡的锁定状态
        card = Card(cardId, '000000', 0, iden, pnum , 'False')
        self.appendCard.append(card)
        print("开户成功！")
        print("您的卡号为%s，密码为%s,余额为%.2f。"%(cardId,'000000',0))
        print("请牢记密码，请勿将密码泄露给他人！")
        # 更新卡号列表
        self.cards = self.readCard.read()
        return True

    # 查询
    def checkMoney(self):
        while True:
            cardId = input("请输入您的账户信息：\n")
            if self.check.isCardIdExist(self.cards, cardId):
                break
            else:
                print("您输入的账户信息有误！")
                if self.check.isSure("继续查询"):
                    continue
                else:
                    print("已为您结束本次服务！")
                    time.sleep(1)
                    return
        card = self.check.isCardIdExist(self.cards,cardId)
        # card = self.check.isCardExist(self.cards)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        if cardId ==card.cardId:
            count = 3
            while count:
                password = input("请输入您的账户密码：\n")
                if password == card.cardPassword:
                    print("您的账户余额为%.2f元！" % card.cardMoney)
                    time.sleep(1)
                    return card.cardMoney
                else:
                    count -=1
                    if count !=0:
                        print("密码错误！您还有%d次机会输入密码！"%count)
                        continue
                        time.sleep(1)
                    elif count == 0:
                        print("密码错误！已为您结束本次服务！")
                        time.sleep(1)
              
    
    # 存款
    def saveMoney(self):
        while True:
            cardId = input("请输入您的账户：\n")
            if self.check.isCardIdExist(self.cards,cardId):
                break
            else:
                print("您输入的账户信息有误！")
                if self.check.isSure("继续存款"):
                    continue
                else:
                    print("已为您结束本次服务！")
                    time.sleep(1)
                    return
        card = self.check.isCardIdExist(self.cards,cardId)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        # cardId = input("请输入您的账户：")
        # card = self.check.isCardIdExist(self.cards,cardId)
        # if self.check.isCardLock(self.cards,card.cardId):
        #     return
        # 你错在这里了！ card为字符串，例：账户为“123456”，在for循环中，print("1")会循环6次！
        # for card in self.cards:
        #     print("1")
        if cardId ==card.cardId:
            count = 3
            while count:
                password = input("请输入您的账户密码：\n")
                if password == card.cardPassword:
                    money =float(input("请输入您要存的钱数：\n"))
                    index = self.cards.index(card)
                    self.cards[index].cardMoney += money
                    self.writeCard()
                    print("存款成功！您的账户余额为%.2f元！"%self.cards[index].cardMoney)
                    time.sleep(2)
                    return  
                else:
                    count -=1
                    if count !=0:
                        print("密码错误！您还有%d次机会输入密码！"%count)
                        continue
                        time.sleep(1)
                    elif count == 0:
                        print("密码错误！已为您结束本次服务！")
                        time.sleep(1)
                        #可有可无
                        #break


    # 取款  
    '''
     首先，判定账户是否为有效账户，若是，继续执行，
     接着判定账户是否存在表单中，如存在，检测账户状态是否正常，
     若正常，接着输入密码，有3次机会：若失败，结束本次服务；
     若有一次密码正确，输入要取钱数，判定余额是否够用，若够，则取出相应金额，并打印余额；
     否则，退出
    '''
    def getMoney(self):
        while True:
            cardId = input("请输入您的账户：\n")
            if self.check.isCardIdExist(self.cards,cardId):
                break
            else:
                print("您输入的账户信息有误！")
                if self.check.isSure("继续取款"):
                    continue
                else:
                    print("已为您结束本次服务！")
                    time.sleep(1)
                    return
        card = self.check.isCardIdExist(self.cards,cardId)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        #上段是假如判断的
        # cardId = input("请输入您的账户：\n")
        # card = self.check.isCardIdExist(self.cards,cardId)
        # if self.check.isCardLock(self.cards,card.cardId):
        #     return
        if cardId == card.cardId:
            count = 3
            while count:
                password = input("请输入您的账户密码：\n")
                if password == card.cardPassword:
                    money = float(input("请输入您要取的钱数：\n"))
                    index = self.cards.index(card)
                    if money > self.cards[index].cardMoney:
                        print("您的账户余额不足！您当前余额为%.2f元！"%self.cards[index].cardMoney)
                        time.sleep(1)
                        return
                    self.cards[index].cardMoney -= money
                    self.writeCard()

                    print("取款成功！您的账户余额为%.2f元！"%self.cards[index].cardMoney)
                    time.sleep(1)
                    return
                else:
                    count -= 1
                    if count != 0:
                        print("密码错误！您还有%d次机会输入密码！"%count)
                        continue
                    elif count == 0:
                        print("密码错误！已为您结束本次服务！")
                        time.sleep(1)
                        break


    # 转账
    '''
     首先，判定账户是否为有效账户，若是，继续执行，
     接着判定账户是否存在表单中，如存在，检测账户状态是否正常，
     若正常，接着输入密码，有3次机会：若失败，结束本次服务。
     若有一次密码输入正确，输入对方账户：若存在，输入转账金额，
     若小于余额，则完成转账并打印剩余余额；若大于余额可判定是否继续转账并继续操作。
     若不存在，可重新输入对方账户，再完成转账。
    '''
    def transferMoney(self):
        while True:
            cardId = input("请输入您的账户：\n")
            if self.check.isCardIdExist(self.cards,cardId):
                break
            else:
                print("您输入的账户有误！")
                if self.check.isSure("继续转账"):
                    continue
                else:
                    print("已为您结束本次服务！")
                    time.sleep(1)
                    return       
        card = self.check.isCardIdExist(self.cards,cardId)
        if self.check.isCardLock(self.cards,card.cardId):
            return
        if cardId == card.cardId:
            count = 3
            while count:
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
                        money = float(input("您当前账户余额为%.2f，请输入转账金额：\n"%self.cards[index].cardMoney))
                        if money > self.cards[index].cardMoney:
                            print("您的账户余额不足！您当前余额为%.2f"%self.cards[index].cardMoney)
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

                    print("转账成功！您卡上余额为%.2f元！"%self.cards[index].cardMoney)
                    time.sleep(2)
                    return
                else:
                    count -=1
                    if count != 0:
                        print("密码错误！您还有%d次机会输入密码！"%count)
                        continue
                    elif count == 0:
                        print("密码错误！已为您结束本次服务！")
                        time.sleep(1)
                        break

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
 

    # 修改密码
    '''
    判定账户是否为有效账户(在用户表单中)，若是，继续执行，
     接着判定账户是否存在表单中，如存在，检测账户状态是否正常，
     若正常，接着输入旧密码，3次机会：若失败，结束本次服务。
     若有一次密码输入正确，接着输入新密码，限定只能由6数字组成
     （异常时抛出提醒，返回继续输入密码），再次输入新密码进行二次确认
     （输入错误时可循环多次输入直至正确）。
    '''
    def changePassword(self):
        while True:
            #账户判定
            cardId = input("请输入您的账户：\n")
            if self.check.isCardIdExist(self.cards,cardId):
                break
            else:
                print("您输入的账户有误！")
                if self.check.isSure("继续修改密码"):
                    continue
                else:
                    print("已为您结束本次服务！")
                    time.sleep(1)
                    return
        card = self.check.isCardIdExist(self.cards, cardId)
        if self.check.isCardLock(self.cards, card.cardId):
            return
        # 输入旧密码
        count = 3
        while count:
            password = input("请输入6位数字旧密码：\n")
            if self.check.isCardPasswordSure(password,card.cardPassword):
                break
            else:
                count -= 1
                if count != 0:
                    print("密码错误！您还有%d次机会输入密码！"%count)
                    time.sleep(1)
                    continue
                elif count == 0:
                    print("密码错误！已为您结束本次服务！")
                    time.sleep(1)
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
                continue
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
                # 想多次再次输入密码时
                continue
                time.sleep(1)
                return
        time.sleep(1)
        pass


    # 销户
    '''
    从表单删去账户信息
    '''
    def closeAccount(self):
        card = self.check.isCardInfoSure(self.cards)
        if card:
            self.cards.remove(card)
            self.writeCard()

            print("销户成功！")
            time.sleep(1)
        pass

    # 挂失
    '''
     首先，判定账户是否为有效账户，若是，继续执行，
     接着判定账户是否存在表单中，如存在，检测账户状态是否正常，
     若正常，接着输入密码，有3次机会：若失败，结束本次服务。
     若有一次密码输入正确，接着判定账户状态：若正常，对账户挂失。
    '''

    def lockAccount(self):
        while True:
            #账户判定
            cardId = input("请输入您的账户：\n")
            if self.check.isCardIdExist(self.cards,cardId):
                break
            else:
                print("您输入的账户有误！")
                if self.check.isSure("继续挂失"):
                    continue
                else:
                    print("已为您结束本次服务！")
                    time.sleep(1)
                    return
        card = self.check.isCardIdExist(self.cards, cardId)
        if self.check.isCardLock(self.cards, card.cardId):
            return
        if cardId == card.cardId:
            count = 3
            while count:
                password = input("请输入您的账户密码：\n")
                if password == card.cardPassword:
                    index = self.cards.index(card)
                    if self.cards[index].cardLock =="False":
                        print("您当前账户状态正常！")
                        if self.check.isSure("继续挂失"):
                            self.cards[index].cardLock = "True"
                            self.writeCard()
                            print("挂失成功！")
                            time.sleep(1)
                            return
                        else:
                            break
                    #这一部分有重复
                    else:
                        ("您的账户当前为锁定状态！")
                        break                        
                else:
                    count -=1
                    if count != 0:
                        print("密码错误！您还有%d次机会输入密码！"%count)
                        continue
                    elif count == 0:
                        print("密码错误！已为您结束本次服务！")
                        time.sleep(1)
                        break
        # card = self.check.isCardInfoSure(self.cards)
        # if self.check.isCardLock(self.cards,card.cardId):
        #     return
        # if card:
        #     index = self.cards.index(card)
        #     self.cards[index].cardLock = "True"
        #     self.writeCard()

        #     print("挂失成功！")
        #     time.sleep(1)
        # pass

    # 解锁
    '''
    首先，判定账户是否为有效账户，若是，继续执行，
     接着判定账户是否存在表单中，如存在，检测账户状态是否正常，
     若正常，接着输入密码，有3次机会：若失败，结束本次服务。
     若有一次密码输入正确，接着判定账户状态：若锁定，对账户解挂。
    '''
    def unlockAccount(self):
        while True:
            #账户判定
            cardId = input("请输入您的账户：\n")
            if self.check.isCardIdExist(self.cards,cardId):
                break
            else:
                print("您输入的账户有误！")
                if self.check.isSure("继续解锁"):
                    continue
                else:
                    print("已为您结束本次服务！")
                    time.sleep(1)
                    return
        card = self.check.isCardIdExist(self.cards, cardId)
        # if self.check.isCardLock(self.cards, card.cardId):
        #     return
        if cardId == card.cardId:
            count = 3
            while count:
                password = input("请输入您的账户密码：\n")
                if password == card.cardPassword:
        # card = self.check.isCardInfoSure(self.cards)
                    index = self.cards.index(card)
                    #待优化！
                    if self.cards[index].cardLock =="True":
                        print("您的账户当前为锁定状态！")
                        if self.check.isSure("继续解锁"):
                            self.cards[index].cardLock = "False"
                            self.writeCard()
                            print("解锁成功！")
                            time.sleep(1)
                            return
                        else:
                            break
                    else:
                        print("您的账户当前状态正常！")
                        break
                else:
                    count -=1
                    if count != 0:
                        print("密码错误！您还有%d次机会输入密码！"%count)
                        continue
                    elif count == 0:
                        print("密码错误！已为您结束本次服务！")
                        time.sleep(1)
                        break
    
    
    
    #补卡  有错误，补卡时还需将原卡钱转入当前账户（此部分未实现）
    # def reissueCard(self):
    #     # card = self.check.isCardInfoSure(self.cards)
    #     r_pnum = self.check.phoneNumInput()
    #     r_idnum = self.check.identifyInput()
    #     print("请稍候")
    #     if self.check.isIdExist(self.cards, r_idnum) == True:

    #         print("正在为您补办银行卡，请稍后...")
    #         while True:
    #         # cardId = str(random.randrange(100000,10000000))
    #             cardId = str(random.randint(0,999999)).zfill(6)
    #             if self.check.isCardIdExist(self.cards,cardId) == False:
    #                 break
    #             else:
    #                 continue
    #         card = Card(cardId,'000000', 0, r_idnum, r_pnum , 'False')
    #         self.appendCard.append(card)
    #         print("补卡成功！您的卡号为为:%s,密码为：%s,余额为：%.2f。" %(cardId,'000000',0))
    #         print("请牢记密码，不要把密码泄露给他人。")
    #         self.cards = self.readCard.read()
    #         return True

    # def reissueCard(self):
    #     # card = self.check.isCardInfoSure(self.cards)
    #     r_pnum = self.check.phoneNumInput()
    #     r_idnum = self.check.identifyInput()
    #     print("请稍候")
    #     if self.check.isIdExist(self.cards, r_idnum) == True:
    #         return
    #     print("正在为您补办银行卡，请稍后...")
    #     while True:
    #         # cardId = str(random.randrange(100000,10000000))
    #         cardId = str(random.randint(0,999999)).zfill(6)
    #         if self.check.isCardIdExist(self.cards,cardId) == False:
    #             break
    #         else:
    #             continue
    #     card = Card(cardId,'000000', 0, r_idnum, r_pnum , 'False')
    #     self.appendCard.append(card)
    #     print("补卡成功！您的卡号为为:%s,密码为：%s,余额为：%.2f。" %(cardId,'000000',0))
    #     print("请牢记密码，不要把密码泄露给他人。")
    #     self.cards = self.readCard.read()
    #     return True

    
   

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


