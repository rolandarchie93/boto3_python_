import boto3

internet_gateway_id = 'igw-04968295d922563cd'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
