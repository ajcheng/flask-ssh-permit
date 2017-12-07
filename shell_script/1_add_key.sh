#!/bin/bash
###Create By ChengAnjing
###Create At 2016-10-31
#遇到错误退出
#set -e
set -x
cat << EOF
+-------------------------------------------------+
|参数示例  dns0110.aliyun wanglei root            |
+-------------------------------------------------+
EOF
#sleep 3 
#如果脚本需要指定参数，给出说明
if [ -z $1 ]; then
   echo "请输入正确的参数: [hostname username hostuser]"
   exit
fi

date=`date '+%Y%m%d %H:%M:%S'`


key_list="/home/aj/shell/key_list_1"
user_key=`grep $2 $key_list`

if [ "$3" == "root" ]
then
    for i in $1;do
        ssh root@$i "echo '#$2 $date' >> .ssh/authorized_keys;echo "$user_key" >> .ssh/authorized_keys"
    done
    echo "$1 上 $3 权限添加成功，请测试"
else
    for i in $1;do
        ssh root@$i "grep $3 /etc/passwd" >/tmp/p.log
        path=`awk -F ':' '{print $6}' /tmp/p.log`
        echo $path
        ssh root@$i "echo '#$2 $date' >> $path/.ssh/authorized_keys;echo "$user_key" >> $path/.ssh/authorized_keys"
    done
    echo "$1 上 $3 权限添加成功，添加信息如下:"
    ssh root@$1 "grep $2 $path/.ssh/authorized_keys" 
fi

