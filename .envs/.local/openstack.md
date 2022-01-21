[S3 compatible - Infomaniak Openstack Public Cloud Guide](https://docs.infomaniak.cloud/user-guide/object-storage/0002.S3/)

## List S3 credentials

`openstack ec2 credentials list`

The server to connect to is : https://s3.pub1.infomaniak.cloud/

## Setting up aws client

```
taylor@laptop:~$ apt install awscli
taylor@laptop:~$ aws configure
AWS Access Key ID [None]: <your access key>
AWS Secret Access Key [None]: <your secret key>
Default region name [None]:
Default output format [None]:
```

### Listing buckets using aws-cli

`taylor@laptop:~$ aws --endpoint-url=https://s3.pub1.infomaniak.cloud s3api list-buckets`

Output:

```
{
    "Buckets": [
        {
            "Name": "volumebackups",
            "CreationDate": "2009-02-03T16:45:09.000Z"
        }
    ],
    "Owner": {
        "DisplayName": "taylor:taylor",
        "ID": "taylor:taylor"
    }
}
```

Note

The creationDate while listing directories will always be 2009-02-03T16:45:09.000Z'' which correpsonds to the date of the first commit of the s3api. it is a hardcoded value.

[Bug #1889386](https://bugs.launchpad.net/swift/+bug/1889386)

### Creating a bucket

creating the bucket "plesk"

`taylor@laptop:~$ aws --endpoint-url=https://s3.pub1.infomaniak.cloud s3api create-bucket --bucket plesk`

Output:

```
{
    "Location": "/plesk"
}
```

### Uploading a directory

`taylor@laptop:~$aws s3 cp --endpoint-url=https://s3.pub1.infomaniak.cloud <your-directory> s3://<your-bucket>/ --recursive`

Warning

The header 100-continue isn't supported. In case your uploads show no progress with the information `Waiting for 100 Continue response` then you have to modify your s3api tool:

`sudo vim /usr/lib/python3/dist-packages/botocore/awsrequest.py`

```
def _send_request(self, method, url, body, headers, *args, **kwargs):
self._response_received = False
if headers.get('Expect', b'') == b'100-continue':
    self._expect_header_set = False
```

Set the line self.\_expect\_header_set to False instead of True

```bash

openstack project list
+----------------------------------+-------------+
| ID                               | Name        |
+----------------------------------+-------------+
| 49855f7c5a564d6bb79826b5472c90f0 | PCP-33W6JPH |
+----------------------------------+-------------+
❯ openstack ec2 credentials create
+------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field      | Value                                                                                                                                                |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| access     | 944bb862281a43d2813cf4f3f7dab729                                                                                                                     |
| links      | {'self': 'https://api.pub1.infomaniak.cloud/identity/v3/users/e392f05a06bd456b807eaab7f9142a3d/credentials/OS-EC2/944bb862281a43d2813cf4f3f7dab729'} |
| project_id | 49855f7c5a564d6bb79826b5472c90f0                                                                                                                     |
| secret     | 200d6635395a42cc9018d82e54547de9                                                                                                                     |
| trust_id   | None                                                                                                                                                 |
| user_id    | e392f05a06bd456b807eaab7f9142a3d                                                                                                                     |
+------------+------------------------------------------------------------

```
