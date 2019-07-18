'''
验证类：
用户名，密码，卡号，密码，身份证，手机号验证
输入确认
'''


class Check(object):
    def __init__(self):
       pass
    #用户验证
    def userName(self,admin,password):
        self.admin = admin
        self.password = password
        while True:
            admin = input("请输入用户名：")
            if admin != self.admin:
                print("该用户名不存在，请重新输入！")
                continue
            else:
                break
        while True:
            password = input("请输入密码：")
            if password != self.password:
                print("密码错误，请重新输入！")
                continue
            else:
                break

    # def userName(self,admin,password):
    #     self.admin = admin
    #     self.password = password
    #     adminFlag = False
    #     admin = input("请输入用户名：")
    #     while True:
    #         # 如果用户名输对，但密码输错，那么重新输入时只需输入密码验证即可
    #         if adminFlag:
    #             admin = input("请输入用户名：")
    #         password = input("请输入密码：")
    #         if admin != self.admin:
    #             print("该用户名不存在，请重新输入！")
    #             adminFlag = True
    #             continue
    #         elif password != self.password:
    #             print("输入的密码不对，请重新输入！")
    #             adminFlag = False
    #             continue
    #         else:
    #             return

    #是否确认某操作
    def isSure(self,operate):
        while True:
            res = input("是否确认%s?(y/n)"%operate)
            if res not in ['y','n']:
                print("输入有误，请重新输入！")
                continue
            elif res == 'y':
                return True
            else:
                return False
    
    # 卡片限制长度，应由6位数字组成
    def isCard(self, card):
        if len(card) != 6:
            print("账户长度应为6位，请重新输入！")
            return False
        elif not card.isdigit():
            print("账户由数字组成，请重新输入！")
            return False
        else:
            return True

    # 手机号限制为11位数字组成，且首位必为1
    def isPhoneNum(self,phonenum):
        if phonenum[0] != '1' :
            print("手机号开头不为1，请重新输入！")
            return False
        elif len(phonenum) != 11 :
            print("手机号长度应为11位，请重新输入！")
            return False
        # .isdigit()检测字符串是否只由数字组成
        elif not phonenum.isdigit():
            print("手机号必须为数字组成，请重新输入！")
            return False
        else:
            return True

    def phoneNumInput(self):
        while True:
            pnum = input("请输入您的手机号：")
            if self.isPhoneNum(pnum):
                return pnum
    
    # 身份证号限制为6位，且最后一位可为X
    def isIdentity(self,identy):
        if len(identy) != 6:
            print("身份证号应为6位，请重新输入！")
            return False
        #此处判定不够精确，身份证最后一位校验位可能为X
        elif not identy.isdigit():
            iden_ = []
            iden_ = identy[0:4]
            if iden_.isdigit() == True and identy[5] =='X':
                return True
            else:
                print("身份证号应为数字组成，请重新输入！")
                return False
        else:
            return True


    def identifyInput(self):
        while True:
            iden = input("请输入您的身份证号：")
            if self.isIdentity(iden):
                return iden

    # 卡号和密码是否正确
    # def isCardExist(self,cards):
    #     cardId = input("请输入账号：")
    #     password = input("请输入密码：")

    #     while True:
    #         for card in cards:
    #             if cardId == card.cardId:
    #                 if password == card.cardPassword:
    #                     return card
    #                 else:
    #                     password = input("密码有误，请重新输入密码：\n")
    #                     break
    #         else:
    #             cardId = input("账号不存在，请重新输入账号：\n")
    #             password = input("请输入密码：")
    
    # 卡号及密码是否正确 （密码输入第3次时还有错误，想让他返回至主页面 怎么办？）
    def isCardExist(self,cards):
        cardId = input("请输入账号：")
        for card in cards:
            if cardId == card.cardId:
                count = 3
                while count:
                    password = input('请输入密码：')
                    if password == card.cardPassword:
                        return card
                    else:                                            
                        count -= 1
                        if count != 0:
                            print("密码有误，您还有%d机会输入密码!"%count)
                            continue
                        elif count ==0:
                            print("你输入的密码有误，已为您结束本次服务！")
                            break

    
    # 卡号是否存在
    def isCardIdExist(self,cards,cardId):
        for card in cards:
            if cardId == card.cardId:
                return card
        else:
            return False

    #身份证号是否存在
    def isIdExist(self,cards,identityId):
        for card in cards:
            if identityId == card.identityId:
                print(identityId)
                return True
            else:
                return False


    # 卡号密码是否正确
    def isCardPasswordSure(self, newassword,oldpassword):
        if newassword == oldpassword:
            return True
        else:
           return False

    def isCardInfoSure(self,cards):
        # 卡号和密码是否正确
        card = self.isCardExist(cards)
        idenId = self.identifyInput()
        pnum = self.phoneNumInput()
        while True:
            if card.identityId == idenId:
                if card.phoneNum != pnum:
                    print("预留手机号输入错误！")
                    if self.isSure("继续注销账户%s"%card.cardId):
                        pnum = self.phoneNumInput()
                        continue
                    else:
                        return False
                else:
                    return card
            else:
                print("身份证号输入不对。")
                if self.isSure("继续注销卡号%s" % card.cardId):
                    idenId = self.identifyInput()
                    continue
                else:
                    return False


    # 卡号是否锁定
    def isCardLock(self,cards,cardId):
        card = self.isCardIdExist(cards,cardId)
        # print(card.cardLock)
        if card != False:
            if card.cardLock == "False":
                return False
            else:
                print("此卡已挂失！")
                return True
        else:
            return "卡号不存在"


# 测试
def main():
    check = Check()
    # print(check.isSure('注销'))
    print(check.phoneNumInput())
    print(pnum)


if __name__ == '__main__':
    main()
