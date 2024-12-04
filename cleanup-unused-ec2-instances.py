import boto3


def terminate_unused_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"Terminated instance: {instance_id}")


terminate_unused_instances()
