import boto3

internet_gateway_id = 'igw-04968295d922563cd'
vpc_id = 'vpc-06b6ccae02b4b7436'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)
