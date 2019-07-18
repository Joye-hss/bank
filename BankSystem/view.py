'''
管理员界面
类名：View
属性：账号，密码
行为：管理员界面   管理员登陆    系统功能界面  管理员注销

系统功能：开户  查询  取款  存储  转账  改密 销户  退出
'''
from check import Check
import time

class View(object):

    def __init__(self,admin,password):
        self.admin = admin
        self.password = password
    # 管理员界面
    def interface(self):
        print("*------------------------------------*")
        print("|                                    |")
        print("|                                    |")
        print("|     系统界面正在启动，请稍候...    |")
        print("|                                    |")
        print("|                                    |")
        print("*------------------------------------*")
        time.sleep(1)
        return

    #管理员登录界面
    def login(self):
        print("*------------------------------------*")
        print("|                                    |")
        print("|                                    |")
        print("|           管理员登陆界面           |")
        print("|                                    |")
        print("|                                    |")
        print("*------------------------------------*")
        check = Check()
        check.userName(self.admin,self.password)
        print("*            登陆成功！              *")
        print("                                      ")
        print("   正在跳转至系统功能界面，请稍候...  ")
        del check
        time.sleep(1)
        return

    # 管理员注销界面
    def logout(self):
        print("*------------------------------------*")
        print("|                                    |")
        print("|           管理员注销界面           |")
        print("|                                    |")
        print("*------------------------------------*")
        #确认是否注销
        check = Check()
        if not check.isSure('注销'):
            return False

        check.userName(self.admin,self.password)
        print("*             注销成功！             *")
        print("                                      ")
        print("        正在关闭系统，请稍候...       ")
        del check
        time.sleep(3)

        return True

    #系统功能界面
    '''
    开户,查询,取款,存款,转账,改密，挂失,解锁,销户,（补卡未实现），销户,退出
    '''
    def funcInterface(self):
        print("*----------Welcome To The Bank----------*")
        print("|                                       |")
        print("|                                       |")
        print("|      (1)开户           (6)改密        |")
        print("|      (2)查询           (7)挂失        |")
        print("|      (3)存款           (8)解锁        |")
        print("|      (4)取款           (9)销户        |")
        print("|      (5)转账           (Q)退出        |")
        print("|                                       |")
        print("|                                       |")
        print("*---------------------------------------*")



