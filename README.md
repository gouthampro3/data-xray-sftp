# Lambda function to pull file from an SFTP server and transfer it to S3 bucket.

**Lambda handler function name:** sftpget_paramiko.handler

**Sample input json format for given lambda code:**
{
	"endpoint":"<endpoint url>",
	"port":22,
	"username":"",
	"remote_filename":"<name of the file in sftp bucket>",
	"dest_bucket":"<Destination s3 bucket name>",
	"aws_access_key_id":"<aws access id>"
	"aws_secret_access_key":"<your aws secret access key>"
}