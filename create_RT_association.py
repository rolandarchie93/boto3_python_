import boto3

route_table_id = 'rtb-08301781474178b66'
subnet_id = 'subnet-0b7b3602d2e29aa02'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association['AssociationId'])
