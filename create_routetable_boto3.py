import boto3

vpc_id = 'vpc-06b6ccae02b4b7436'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable['RouteTable']['RouteTableId'])
