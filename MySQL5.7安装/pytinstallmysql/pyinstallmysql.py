# -*- coding: utf-8 -*-
import os
import time
import socket

port=input("请输入New实例port:")
#模板配置文件
mycnfinit="my.cnf"
softtar="mysql-5.7.32-linux-glibc2.12-x86_64.tar.gz"
#取出解压后的目录名，字符串截取
mysqlsoft=softtar[:-7]
#获取安装脚本所在的目录
pwd_path=os.getcwd()
datadir="/data"



def IsOpen(port1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1",int(port1)))
        s.shutdown(2)
        return ("open")
    except:
        return ("down")
    s.close()

def install_mysql():
    #依赖包、软件包加载
    os.system("yum install libaio -y")
    os.system(f"tar -xvzf {softtar}")
    os.system(f"mv  {mysqlsoft} mysql57 ")
    os.system("groupadd mysql")
    os.system("useradd -r -g mysql -s /bin/false mysql")

    #配值文件更改
    with open(f"{mycnfinit}",mode="r",encoding="utf-8") as f ,open(f"my{port}.cnf",mode="a+",encoding="utf-8") as f2:
        lst=f.readlines()
        for line in lst:
            new_line=line.replace("13308",f"{port}")
            f2.write(new_line)
    #os.remove(f"{mycnfinit}")


    #初始化数据库、启动数据库
    os.symlink(f"{pwd_path}/mysql57","/usr/local/mysql")
    os.system(f"/usr/local/mysql/bin/mysqld --defaults-file={pwd_path}/my{port}.cnf  --initialize-insecure   --user=mysql")
    os.system(f"mv {pwd_path}/my{port}.cnf  /data/mysql{port}/")
    os.system(f"/usr/local/mysql/bin/mysqld_safe --defaults-file=/data/mysql{port}/my{port}.cnf  &")



#判断数据库目录是否存在如果不存在，就退出程序
def isdatadir():
    try:
        if os.path.isdir(f"{datadir}") is False:
#            print(f"{datadir}目录存在")
 #       else:
 #           print(f"{datadir}目录不存在，正在创建！！")
            os.makedirs(f"{datadir}")
 #           print(f"{datadir}已经创建")
    except:
            return "failed"


#验证端口号是否被占用，如果被占用就退出安装程序，验证是否启动成功数据，如果启动成功就表明安装成功
portstr=IsOpen(port)
datasort=isdatadir()
if portstr == "open" :
    print(f"请重新输入端口号 port，{port} 已经被占用")
else:
    if datasort == "failed":
        print("数据目录创建失败")
    else:
        print(f"{port} 未被占用！！！！")
        install_mysql()
        time.sleep(5)
        portstr2=IsOpen(port)
        if portstr2 == "open" :
            print("数据库启动成功！！！")
            print("安装成功！！！")
        else:
            print("数据库启动失败！！！")
            print("安装失败！！！")