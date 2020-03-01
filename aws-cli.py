import boto3
from tabulate import tabulate

ec2 = boto3.client('ec2')
response = ec2.describe_instances()['Reservations']
table = [['Id', 'State', 'DNS']]
for i in range (len(response)):
    instance = response[i]['Instances'][0]
    Id = instance['InstanceId']
    State = instance['State']['Name']
    try:
        DNS = instance['PublicDnsName']
    except:
        DNS = None
    table.append([Id, State, DNS])
print(tabulate(table))