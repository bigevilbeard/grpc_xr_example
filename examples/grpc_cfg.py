""" Basic gRPC getcall configuration. Shows how to set up the vairables
for tls and how to put into the class and get information from the box.
Need Cisco GRPC python library
https://github.com/bigevilbeard/grpc_xr_example
Credit: https://github.com/cisco-grpc-connection-libs/ios-xr-grpc-python/blob/master/examples/grpc_example.py
"""

import sys
sys.path.insert(0, '../')
from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient
import json
from time import sleep
import click

class Example:
    def __init__(self):
        self.client = CiscoGRPCClient('sbx-iosxr-mgmt.cisco.com', 19399, 10, 'admin', 'C1sco12345')
    
    def get_facts(self):
        path = '{"Cisco-IOS-XR-ipv4-bgp-cfg:bgp": [null]}'
        result = self.client.getconfig(path)
        print(result)

    def config_replace(self):
        path = open('snips/bgp_start.json').read()
        result = self.client.replaceconfig(path)
        print(result) # If this is sucessful, then there should be no errors.

    def config_merge(self):
        path = open('snips/bgp_merge.json').read()
        result = self.client.mergeconfig(path)
        print(result) # If this is sucessful, then there should be no errors.

    def config_delete(self):
        path = open('snips/bgp_start.json').read()
        result = self.client.deleteconfig(path)
        print(result) # If this is sucessful, then there should be no errors.



@click.group()
def cli():
    pass

@click.command()
def get():
    click.secho("Retrieving Information")
    get = json.dumps((Example.get_facts), sort_keys=True, indent=4)
    click.echo(get)

@click.command()
def replace():
    click.secho("Retrieving Information")
    replace = json.dumps((Example.config_replace), sort_keys=True, indent=4)
    click.echo(replace)

cli.add_command(get)
cli.add_command(replace)

if __name__ == "__main__":
    cli()