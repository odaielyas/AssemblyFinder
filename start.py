import boto3
import csv

def start_model(project_arn, model_arn, version_name, min_inference_units):

    with open ('mkal_accessKeys.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        
        for row in reader:
            access_key_id = row[0]
            secret_access_key = row[1]

    client= boto3.client('rekognition', region_name = 'us-east-2', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        #Get the running status
        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage'])
    except Exception as e:
        print(e)
       
    print('Done...')
   
def main():
    
    #project_arn='arn:aws:rekognition:us-east-2:696327820520:project/AssemblyFinder3/1681313954711'
    #model_arn='arn:aws:rekognition:us-east-2:696327820520:project/AssemblyFinder3/version/AssemblyFinder3.2023-04-12T11.59.22/1681315162247'
    #version_name='AssemblyFinder3.2023-04-12T11.59.22'
    
    min_inference_units=1

    project_arn='arn:aws:rekognition:us-east-2:696327820520:project/AssemblyFinder4/1682438202957'
    model_arn='arn:aws:rekognition:us-east-2:696327820520:project/AssemblyFinder4/version/AssemblyFinder4.2023-04-25T16.20.38/1682454037596'
    version_name='AssemblyFinder4.2023-04-25T16.20.38'

    start_model(project_arn, model_arn, version_name, min_inference_units)


if __name__ == "__main__":
    main()