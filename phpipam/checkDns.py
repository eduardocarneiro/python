import os

count = 1
for count in range(1,5):
    hostname = 'master0' + str(count) + '.devops.lab'
    print(hostname)
    returnedValue =  os.system('nslookup ' + hostname + ' 10.11.58.11 &> /dev/null ')
    print(returnedValue)
    if returnedValue == 0:
        print("Nome indisponivel")
    else:
        print(hostname + " esta disponivel pra uso")

