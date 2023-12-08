import boto3

vpc_id = 'vpc-06b6ccae02b4b7436'
ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
