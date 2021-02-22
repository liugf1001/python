#!/usr/bin/python37
import json
import os
import hashlib
import pymysql
lpljsoin="/data/pt/soft/mysqlloginpy/.lpl.json"
mysql_path='/usr/local/mysql/bin/mysql'

def logina(test):
    with open(lpljsoin, encoding="utf-8") as f:
        data= json.load(f)
    dict_u=data[test]
#    mysql_path='/usr/local/mysql/bin/mysql'
    mysqllogin=f'{mysql_path} -u{dict_u["user"]} -p{dict_u[r"pass"]} -h {dict_u["host"]} -P {dict_u["port"]} '
    os.system(mysqllogin)
    os.system("clear")


def md5_func(passwd):
    hash=hashlib.md5()
    hash.update(passwd.encode('utf-8'))
    a=hash.hexdigest()
    return a

def connect_mysql():
    with open(lpljsoin, encoding="utf-8") as f:
        data1= json.load(f)
    dict_u1=data1["test"]
    db = pymysql.connect(
                host=dict_u1["host"],
                user=dict_u1["user"],
                port=int(dict_u1["port"]),
                db="dba",
                password=dict_u1["pass"])
    cursor=db.cursor()
    cursor.execute("select name from lg")
    b=cursor.fetchone()
    c=b[0]
    return c


def add_json(argadd):
    with open(lpljsoin,'r',encoding="utf-8") as f:
        dataadd=json.load(f)
    appnamelist=list(dataadd.keys())
    appnamedata=list(argadd.keys())[0]
    if appnamedata not in appnamelist:
        print("项目不冲突")
        dataadd[appnamedata]=argadd[appnamedata]
        with open(lpljsoin, "w", encoding="utf-8") as f2:
            json.dump(dataadd, f2, indent=2, sort_keys=True, ensure_ascii=False)
        return "Successfull"
    else:
        return "doubleeppname"

def app_infoindex():
    with open(lpljsoin,'r',encoding="utf-8") as f:
        dataadd=json.load(f)
    appnamelist=list(dataadd.keys())[1:]
    print("请选择项目：")
    for i in range(len(appnamelist)):
        dataexta=appnamelist[i]
        try:
            print(f"    {dataexta}: {dataadd[dataexta]['exta']}")
        except:
            print(f"    {dataexta}: 无描述信息")
    return appnamelist


