import sys
from io import StringIO
import boto3
import paramiko

class GraciousPush:
	def __init__(self,hostname,pkey_filename,username,packetsize,port=22):
		self.hostname=hostname
		self.username=username
		self.packetsize=packetsize
		self.port=port

	def get_pkeyfile(self,keybucket,keyprefix,keyfilename):
		s3 = boto3.resource('s3')
		s3response = s3.Object(keybucket, keyprefix+'/'+keyfilename)
		keystring = s3response.get()['Body'].read().decode("utf-8") 
		return keystring

	def get_connection(self,keybucket,keyprefix,keyfilename):
		keystring=self.get_pkeyfile(keybucket,keyprefix,keyfilename)
		pkey = paramiko.RSAKey.from_private_key(StringIO(keystring))
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(self.hostname, port=self.port, username=self.username, pkey=pkey)
		transport=client.get_transport()
		transport.default_max_packet_size=self.packetsize
		sftp = transport.open_sftp_client()
		return sftp

	def get_from_s3(self,bucket,object_name,file_name):
		s3_client = boto3.client('s3')
		try:
			response = s3_client.download_file(bucket, object_name,file_name)
		except ClientError as e:
			return (False,e)
		return (True,"Success")	

	def put_file(self,keybucket,keyprefix,keyfilename,l_filename):
		sftp=self.get_connection(keybucket,keyprefix,keyfilename)
		sftp.put(l_filename,l_filename)

	

if __name__ == '__main__':
    print("Session Started")
    pkey_filename="sftpuser"
    pushdata=GraciousPush('s-0314b7e0e5f1466da.server.transfer.us-east-2.amazonaws.com',pkey_filename,'testuser',1024)
    s3_download_status,s3_download_msg=pushdata.get_from_s3('client1-datastore','hello.txt','hello.txt')
    pushdata.put_file('gluejobstore','filestore','sftpuser','hello.txt')
    print("S3 Upload Status: "+s3_download_msg)