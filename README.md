# Lambda function to pull file from an SFTP server and transfer it to S3 bucket.

The packaged lambda code is in sftppull.zip which can be directly uploaded to AWS Lambda through console.
**Lambda handler function name:** sftpget_paramiko.handler

**Sample event input json format for given lambda code:**
{
	"endpoint":"<endpoint url>",
	"port":22,
	"username":"",
	"remote_filename":"<name of the file in sftp bucket>",
	"dest_bucket":"<Destination s3 bucket name>",
	"aws_access_key_id":"<aws access id>"
	"aws_secret_access_key":"<your aws secret access key>"
}
	
**Wondering if large files can be transfered through this method before the lambda times out?**
Yeah 500MB works just fine. 


But GB's? Hell Nah!
 
