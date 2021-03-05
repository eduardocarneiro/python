#!/usr/bin/env python
# coding=UTF-8

import paramiko
import os
from datetime import date


zone = "ns1.devops.lab.zone"

host = '10.11.58.11'
username='root'
password='P@ssw0rd'


# check and allocated a free dns hostname
#import os

serverPreffix = "srv"
serverSuffix = ".devops.lab"
dnsServer = "10.11.58.11"

count = 1
for count in range(110,230):
    hostname = serverPreffix + str(count) + serverSuffix
    print(hostname)
    returnedValue =  os.system('nslookup ' + hostname + dnsServer + ' &> /dev/null ')
    print(returnedValue)
    if returnedValue == 0:
        print("Nome indisponivel")
    else:
        print(hostname + " esta disponivel pra uso")
        hostnamePreffix = str(serverPreffix + str(count))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        #stdin, stdout, stderr = ssh.exec_command("echo -e " + "'" + hostnamePreffix + "\t\t" + "IN" + "\t" + "A" + "10.11.58.252" + zone + "'")
        stdin, stdout, stderr = ssh.exec_command("cat /var/named/ns1.devops.lab.zone")
        for out in stdout:
            print(out.strip('\n'))
        ssh.close()
        break

"""



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command("grep -i serial /var/named/" + zone +  | awk "'{ print $1}'")

todayDate = date.today()

server = "server01.devops.lab"

for currentRemoteBindSerialNumber in stdout:
    checkRemoteBindSerialNumber = currentRemoteBindSerialNumber[0:8]
    localDate = todayDate.strftime("%Y%m%d")
    if localDate == checkRemoteBindSerialNumber:
        newSerialNumber = int(int(localDate) + 1)
        print(newSerialNumber)
        newRemoteBindSerialNumber = ("sed -i 's/%i/%i/g' /var/named/ns1.devops.lab.zone" %(int(currentRemoteBindSerialNumber), int(newSerialNumber)))
        print(newRemoteBindSerialNumber)
        stdin, stdout, stderr = ssh.exec_command(newRemoteBindSerialNumber)
    else:
        newSerialNumber = int(str(localDate) + str(1))
        newRemoteBindSerialNumber = ("sed -i 's/%i/%i/g' /var/named/ns1.devops.lab.zone" %(int(currentRemoteBindSerialNumber), int(newSerialNumber)))
        print(newRemoteBindSerialNumber)
        stdin, stdout, stderr = ssh.exec_command(newRemoteBindSerialNumber)

ssh.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command("grep -i serial /var/named/" + zone +  | awk "'{ print $1}'")

todayDate = date.today()

server = "server01.devops.lab"

ssh.close()






#stdin, stdout, stderr = ssh.exec_command("sed -i 's/' /var/named/ns1.devops.lab.zone")

#ssh.close()

#for line in stdout:
#        print(line.strip('\n'))
#ssh.close()

"""
"""
all_lines = ''
for line in stdout.readlines():
        all_lines += line
        new_line = all_lines + 'add more or edit'
        print new_line
        stdin, stdout, stderr = ssh.exec_command("echo '{}' >> path_of_file_to_write".format(new_line))
        ssh.close()
"""
"""
reference:
    https://stackoverflow.com/questions/47252339/how-to-edit-the-remote-file-via-sshlibrary
    https://www.programiz.com/python-programming/datetime/current-datetime
    https://www.tutorialspoint.com/python/python_numbers.htm
    https://stackoverflow.com/questions/5863999/python-cut-example
    https://www.unix.com/shell-programming-and-scripting/270693-sed-command-inside-paramiko-python.html
    https://stackoverflow.com/questions/5863999/python-cut-example

"""
