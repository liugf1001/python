#!/bin/bash
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel gcc
tar -xvf Python-3.7.3.tgz
cd Python-3.7.3
./configure --prefix=/usr/local/python37
make  
make install
ln -s /usr/local/python37/bin/python3.7 /usr/bin/python37
ln -s /usr/local/python37/bin/pip3.7 /usr/bin/pip37
