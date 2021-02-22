#!/bin/bash
mysqllog(){
user=`cat  .user|grep "user"|cut -d ':' -f 2`
pass=`cat  .user|grep "pass"|cut -d ':' -f 2`
host=`cat  .user|grep "host"|cut -d ':' -f 2`
port=`cat  .user|grep "port"|cut -d ':' -f 2`
mysqllogin='/usr/local/mysql/bin/mysql'
$mysqllogin -u${user} -p${pass} -h${host} -P${port}
}
while true
do
echo  "">.user
clear
echo -e  '请选择数据库环境::::::	\n premaster：预发主库 \n \t |___preslave1：预发从库1  \n scrmmaster：scrm主库 \n \t |___scrmslave1：scrm从库1 	\n zilongmaster：zilong主库 \n \t |___zilongslave1：zilong从库1  \n \t |___zilongslave2：zilong从库2   \n \t |___zilongslave3：zilong从库3	\n 0:退出)' 
read  -p '输入选项：' name
case $name in 
	premaster) echo -e  "你选择的是：\033[30;43m  pre 主库  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
	preslave1) echo -e  "你选择的是：\033[30;43m  pre 从库1  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
	scrmmaster) echo -e  "你选择的是：\033[30;43m  scrm 主库  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
	scrmslave1) echo -e  "你选择的是：\033[30;43m  scrm 从库1  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
	zilongmaster) echo -e  "你选择的是：\033[30;43m  zilong  主库  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
	zilongslave1) echo -e  "你选择的是：\033[30;43m  zilong  从库1  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
	zilongslave2) echo -e  "你选择的是：\033[30;43m  zilong  从库2  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
	zilongslave3) echo -e  "你选择的是：\033[30;43m  zilong  从库3  \033[0m"
	     cp .username/${name} .user 
             mysqllog
             ;;
        0)   echo "结束程序"
		 break
	;;
	*)   echo "输入错误，请重新输入！"
esac
done
