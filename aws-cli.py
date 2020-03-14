import click
import boto3
from tabulate import tabulate

@click.group()
@click.option('-t', '--tags')
@click.option('-c', '--cloud', type=click.Choice(['aws', 'gcp', 'azure']))
def cli(tags, cloud):
    """ Cloud Manager cli """

@cli.group()
def get():
    """ get action """

@get.command()
def instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()['Reservations']
    table = [['Id', 'State', 'DNS']]
    for i in range(len(response)):
        instance = response[i]['Instances'][0]
        Id = instance['InstanceId']
        State = instance['State']['Name']
        try:
            DNS = instance['PublicDnsName']
        except:
            DNS = None
        table.append([Id, State, DNS])
    print(tabulate(table))

@cli.command()
def stop():
    """ stop action """
    click.echo('Stop')
if __name__ == '__main__':
    cli()