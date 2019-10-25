# Lambda function to pull file from an SFTP server and transfer it to S3 bucket.

The packaged lambda code is in **sftppull.zip** which can be directly uploaded to AWS Lambda through console. I have included my sftp user public key and private key for reference. The private key must be embeded in the package. If you are using my zip as it is use my public key for your user.<br /><br />

**Lambda handler function name:** sftpget_paramiko.handler <br />

**Sample input json format for given lambda code:** <br />
```json
{
	"endpoint":"<endpoint url>",
	"port":22,
	"username":"",
	"remote_filename":"<name of the file in sftp bucket>",
	"dest_bucket":"<Destination s3 bucket name>",
	"aws_access_key_id":"<aws access id>",
	"aws_secret_access_key":"<your aws secret access key>"
}
```	
**Wondering if large files can be transfered through this method before the lambda times out?**<br/>
Yeah 500MB works just fine. 
![Preview](https://github.com/gouthampro3/data-xray-sftp/blob/master/img/500mb.PNG)

But GB's? Hell Nah!<br/>

1GB file failure Screenshot:
![Preview](https://github.com/gouthampro3/data-xray-sftp/blob/master/img/1gb.PNG)