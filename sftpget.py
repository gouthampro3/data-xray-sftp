import pysftp
import boto3

r_filepath='<path to directory of remote file>'
r_filename='<name of remote file>'
l_file=r_filename
s3_bucket_name='<name of s3 bucket>'
s3=boto3.client('s3')

def handler(event,context):
	with pysftp.Connection('hostname', username='me', password='secret',port='') as sftp:
		with sftp.cd(r_filepath): 
			sftp.get(r_filename,localpath=l_file)
	s3.upload(l_file,s3_bucket_name)