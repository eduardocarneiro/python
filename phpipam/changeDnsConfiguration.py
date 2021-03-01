import paramiko

host = 'test.example.com'
username='host_user_name'
password='host_password'
ssh = paramiko.SSHClient()
print(ssh)
