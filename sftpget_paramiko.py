import paramiko
import boto3
import timeit
from botocore.exceptions import ClientError
"""
hostname = 's-66dd554c71f047eea.server.transfer.us-east-1.amazonaws.com'
port = 22
user_name='testuser'
r_filename='test2.txt'
"""
def uploadToS3(file_name,bucket,object_name,awskeyid,awskey):
    s3_client = boto3.client('s3',aws_access_key_id=awskeyid,aws_secret_access_key=awskey)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        return (False,e)
    return (True,"Success")

def handler(event,context):
	hostname = event['endpoint']
	port = int(event['port'])
	user_name = event['username']
	r_filename = event['remote_filename']
	dest_bucket = event['dest_bucket']
	awskeyid = event['aws_access_key_id']
	awskey = event['aws_secret_access_key']

	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname, port=port, username=user_name, key_filename='sftpuser')
	sftp = client.open_sftp()
	sftp_downstart = timeit.default_timer()
	sftp.get(r_filename,'/tmp/'+r_filename)
	sftp_downstop = timeit.default_timer()
	s3_uploadstart = timeit.default_timer()
	s3_upload_status,s3_upload_msg =uploadToS3('/tmp/'+r_filename,dest_bucket,r_filename,awskeyid,awskey)
	s3_uploadstop = timeit.default_timer()
	return {
		"Time took for sftp pull":(sftp_downstop - sftp_downstart),
		"Time took to upload to client s3 bucket":(s3_uploadstop - s3_uploadstart),
		"S3 Upload Status" : s3_upload_msg
	}

	#sftp.put('/home/lone/Documents/job_se/data-xray-sftp/paramiko.log','paramiko.log')
	#return (sftp.listdir())
#event={"endpoint":"s-aa08898534784533a.server.transfer.us-east-1.amazonaws.com","port":22,"username":"testuser","remote_filename":"hello.txt","dest_bucket":"client2-datastore"}
#handler(event,1)