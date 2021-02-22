#!/usr/bin/python37
import mysql_login
import os
import getpass
import time

def main():
    list1 = mysql_login.app_infoindex()
    list2 = ["0", "exit"]
    while True:
        os.system("clear")
        print("数据库环境一共有：")
        print(list1)
        mysql_login.app_infoindex()
        print("""0 or exit: 退出数据库登录界面""")
        test = input("请选择数据库：")
        if test in list1:
            mysql_login.logina(test)
            os.system("clear")
        elif test in list2:
            exit()

os.system("clear")
n=0
while True:
        password = getpass.getpass("请输入管理密码：")
        if mysql_login.md5_func(password)==mysql_login.connect_mysql() and n<2:
            print("您输入的管理密码是正确！")
            print("正在切换到，数据库登录选项界面，请稍后！！！")
            time.sleep(1)
            main()
        elif n<4:
            n+=1
            print("账号密码输入错误，请重新输入！！！")
            continue
        else:
            print("已经连续5次输入密码错，确认退出登录！")
            exit()




