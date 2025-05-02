import boto3
import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Get current date
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Get all volumes with a specific tag (example: Backup:True)
    volumes = ec2.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Backup',
                'Values': ['True']
            }
        ]
    )

    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        description = f"Automated snapshot of {volume_id} on {today}"

        print(f"Creating snapshot for volume {volume_id}")
        ec2.create_snapshot(
            VolumeId=volume_id,
            Description=description,
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {'Key': 'CreatedBy', 'Value': 'Lambda'},
                        {'Key': 'VolumeId', 'Value': volume_id}
                    ]
                }
            ]
        )

