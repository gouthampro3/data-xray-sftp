import pysftp
#import boto3

r_filepath='/quarantine-file-store'
r_filename='test2.txt'
l_file=r_filename
s3_bucket_name='<name of s3 bucket>'
#s3=boto3.client('s3')

def handler():
	cnopts = pysftp.CnOpts()
	cnopts.hostkeys = None
	with pysftp.Connection('s-66dd554c71f047eea.server.transfer.us-east-1.amazonaws.com', username='testuser', private_key='sftpuser',cnopts=cnopts) as sftp:
		with sftp.cd(r_filepath): 
			sftp.get(r_filename,localpath=l_file)
	#s3.upload(l_file,s3_bucket_name)

handler()