import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIA22EHG7RB2IAUOKDK',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

print(s3)

def upload(file):
    s3 = boto3.client('s3', aws_access_key_id='AKIA22EHG7RB2IAUOKDK',
                      aws_secret_access_key='TfjaX9cSfnpa8uJX87hkLU4NsWT0Vrs4Ahg/IUXe')

    try:
        s3.upload_file(file, "newbucket3099", 'example.txt')
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def download(file):
    s3.Bucket('newbucket3099').download_file(file, 'example.txt')
    print('Success')


def replace(file):
    obj = s3.Object('newbucket3099', file)
    result = obj.put(Body="File is replaced By New Content")
    res = result.get('ResponseMetadata')

    if res.get('HTTPStatusCode') == 200:
        print('File Conntent Replaced Successfully')
    else:
        print('File Could Not Be Replaced')


upload('r.txt')
download('example.txt')
replace('example.txt')
download('example.txt')