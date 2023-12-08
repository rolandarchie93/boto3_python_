import boto3

subnet_id = 'subnet-0b7b3602d2e29aa02'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

