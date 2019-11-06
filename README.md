# AWS Glue Python shell Job to acheive data transfer between S3 to SFTP server [Maybe, a hack! ;)]

In this scenario the client has >5GB sized files on their sftp server. We are given cerdentials for the sftp user and we are to pull those files and upload them to S3. Then those files have to be processed and to be pushed to another SFTP server from S3.<br/>

 - I tried to use AWS Glue ETL job(python) because we cab attach temporary s3 storage to it which makes our life easier. Later figured that one of the libraries I use(Paramiko) has C based libraries as dependecies which arent supported by Glue ETL job.
 - So I decided to use PythonShell. You can store the files locally temporarily(I dont know the limit though).
 - **glue_sftp_pull.py** pulls the file from the the client SFTP saves it locally and then pushes it to AWS S3.
 - **glue_sftp_push.py** pulls the file from S3, saves it locally and pushes to client SFTP.
 - Donot forget to add dependent library wheel/egg/zip to S3 and give path to them in the job configuration. <br/>

The Glue jobs can also be invoked from lambda.<br/>
**I could transfer a 7GB file from an SFTP Server(used AWS SFTP for simulation purpose) to S3, it took 1hour 9mins to finish the job.**
![Preview](https://github.com/gouthampro3/data-xray-sftp/blob/master/img/7gb_pull.png)

**I could transfer a 7GB file from S3 tp an SFTP Server(used AWS SFTP for simulation purpose), it took 57mins to finish the job.**
![Preview](https://github.com/gouthampro3/data-xray-sftp/blob/master/img/7gb_push.png)

# Lambda function to pull file from an SFTP server and transfer it to S3 bucket. [sftpget_paramiko.py]

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

But GB's? Hell Nah! Because the /tmp directory can hold only 512mb and also the timeout is 30sec<br/>

1GB file failure Screenshot:
![Preview](https://github.com/gouthampro3/data-xray-sftp/blob/master/img/1gb.PNG)