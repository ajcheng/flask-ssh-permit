import paramiko
import os
import sys

host = '192.168.1.196'
port = 22
username = 'root'
pkey_file = '/home/aj/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)

cmd = 'whoami'
s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(host,port,username,pkey=key,timeout=5)
stdin,stdout,stderr = s.exec_command(cmd)
cmd_result = stdout.read(),stderr.read()
for line in cmd_result:
    print line,
s.close()