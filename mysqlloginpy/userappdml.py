#!/usr/bin/python37
# -*- coding:utf-8 -*-
import os
import time
import mysql_login
os.system("clear")
while True:
        a=input("项目库名称（例如：zilongmaster）：")
        b=input("user:")
        c=input("pass:")
        d=input("host:")
        e=input("port:")
        f=input("项目库描述：")
        mysql_path='/usr/local/mysql/bin/mysql'
        dataapp={a:{"user":b,"pass":c,"host":d,"port":e,"exta":f}}
        print(dataapp)
        dict_u=dataapp[a]
        mysqllogin = f'{mysql_path} -u{dict_u["user"]} -p\'{dict_u["pass"]}\' -h {dict_u["host"]} -P {dict_u["port"]} mysql   -e "select 1"'
        print(mysqllogin)
        osa=os.system(mysqllogin)
        if osa==0:
            a=mysql_login.add_json(dataapp)
            if  a=="doubleeppname":
                print("项目库名称冲突，请重新输入！")
            else:
                print("项目库信息添加成功！！！")
                time.sleep(3)
        else:
            print("输入登录信息有误，请重新输入")
            time.sleep(3)
