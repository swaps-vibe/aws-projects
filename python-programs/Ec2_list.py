import boto3

def check_ec2_status():
    ec2 = boto3.client('ec2' , region_name='ap-south-1')

    response = ec2.describe_instances()

    reservations = response['Reservations']

    if len(reservations) == 0:
        print("No Ec2 instance found in account")
    else:
   

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID :{instance['InstanceID']}")
                print(f"Type :{instance['InstanceType']}")
                
check_ec2_status()
                