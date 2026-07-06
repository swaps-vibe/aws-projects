import boto3

def check_ec2_ststus():

    ec2 = boto3.client('ec2',region_name='us-east-1')
    response = ec2.describe_instances()
    reservations = response['Reservations']
    
    if len(reservations) == 0:
        print("No Ec2 instance found!")
    else:
	
        for reservation in reservations:
            for instance in reservation['Instances']:
                print(f"ID  :{instance['InstanceId']}") 
                print(f"Type  :{instance['InstanceType']}")
                print(f"Status :{instance['State']['Name']}")

check_ec2_ststus()              