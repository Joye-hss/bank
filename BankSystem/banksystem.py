'''
类名：Person
属性：姓名  身份证号   手机号  卡 
行为：开户,查询,取款,存款,转账,改密，挂失,解锁,销户,（补卡未实现），销户,退出

卡:
类名:Card
属性：卡号(6位随机)，密码，余额，绑定身份证号，绑定手机号，卡状态（正常/锁定）

取款机：
类名：ATM
属性：
行为：开户,查询,取款,存储,转账,销户,挂失,解锁,改密,退出

管理员界面
类名：View
属性：账号，密码
行为：管理员界面   管理员登陆    系统功能界面
'''
from view import View
from atm import ATM
from person import Person

view = View("hss",'666')
view.interface()
atm = ATM()
view.login()
while True:
    view.funcInterface()
    choice = input("请选择您要办理的业务：")
    if choice == '1':
        atm.newAccount()
    elif choice == '2':
        atm.checkMoney()
    elif choice == '3':
        atm.saveMoney()
    elif choice == '4':
        atm.getMoney()
    elif choice == '5':
        atm.transferMoney()
    elif choice == '6':
        atm.changePassword()
    elif choice == '7':
        atm.lockAccount()
    elif choice == '8':
        atm.unlockAccount()
    # elif choice == '9':
    #     atm.reissueCard()
    elif choice == '9':
        atm.closeAccount()
    # elif choice == 'R'
    #     atm.ruturn()
    elif choice == 'Q':
        if atm.exit():
            if view.logout():
                 break
    else:
        print("您的输入有误！")
