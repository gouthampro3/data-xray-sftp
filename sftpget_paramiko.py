import paramiko

hostname = 's-66dd554c71f047eea.server.transfer.us-east-1.amazonaws.com'
port = 22
user_name='testuser'
r_filename='test2.txt'

def handler(event,context):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname, port=port, username=user_name, key_filename='sftpuser')
	sftp = client.open_sftp()
	#sftp.get(r_filename,'test2.txt')
	#sftp.put('/home/lone/Documents/job_se/data-xray-sftp/paramiko.log','paramiko.log')
	return (sftp.listdir())