#!/bin/bash
#pass=
while true
do 
  
  read -p '请输入密码：' password
  echo -n  $password|openssl md5>.md5.txt
  a=(`cat .md5.txt`)
  b=(`cat .md.txt`)
  no_1=${a[1]}
  no_2=${b[0]}
  if [ $no_1 = $no_2 ];then
	./.login.sh exec
	echo "">.user
	break 
    else
    echo "密码错误！！"
    fi

done
