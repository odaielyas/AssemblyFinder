import boto3
import time
import csv



def stop_model(model_arn):

    with open ('mkal_accessKeys.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        
        for row in reader:
            access_key_id = row[0]
            secret_access_key = row[1]

    client= boto3.client('rekognition', region_name = 'us-east-2', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')
   
def main():
    model_arn='arn:aws:rekognition:us-east-2:696327820520:project/AssemblyFinder4/version/AssemblyFinder4.2023-04-25T16.20.38/1682454037596'
    stop_model(model_arn)

if __name__ == "__main__":
    main()