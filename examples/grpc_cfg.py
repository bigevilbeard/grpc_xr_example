""" Basic gRPC getcall configuration. Shows how to set up the vairables
for tls and how to put into the class and get information from the box.
Need Cisco GRPC python library
https://github.com/bigevilbeard/grpc_xr_example
Credit: https://github.com/cisco-grpc-connection-libs/ios-xr-grpc-python/blob/master/examples/grpc_example.py
"""

import sys
sys.path.insert(0, '../')
from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient
from grpc.framework.interfaces.face.face import AbortionError
import json
from time import sleep
import click


class Example:
    def __init__(self):
        self.client = CiscoGRPCClient('sbx-iosxr-mgmt.cisco.com', 19399, 10, 'admin', 'C1sco12345')

    def get(self):
        path = '{"Cisco-IOS-XR-ipv4-bgp-cfg:bgp": [null]}'
        result = self.client.getconfig(path)
        print(result)


    def replace(self):
        path = open('snips/bgp_start.json').read()
        result = self.client.replaceconfig(path)
        print(result) # If this is sucessful, then there should be no errors.


    def merge(self):
        path = open('snips/bgp_merge.json').read()
        result = self.client.mergeconfig(path)
        print(result) # If this is sucessful, then there should be no errors.

    def config_delete(self):
        path = open('snips/bgp_start.json').read()
        result = self.client.deleteconfig(path)
        print(result) # If this is sucessful, then there should be no errors.


example = Example()

@click.group()
def cli():
    pass

@click.command()
def get():
    try:
        fact = example.client.getconfig(path='{"Cisco-IOS-XR-ipv4-bgp-cfg:bgp": [null]}')
        new_fact = json.loads(fact[1])
        print(json.dumps(new_fact, indent=4))
    except Exception as e:
        print ("BGP instance 'default' not active")


@click.command()
def replace():
    new_path = open('snips/bgp_start.json').read()
    add_replace = example.client.replaceconfig(yangjson= new_path)
    print("Replace Completed")

@click.command()
def merge():
    new_path = open('snips/bgp_merge.json').read()
    add_merge = example.client.mergeconfig(yangjson= new_path)
    print("Merge Completed")

@click.command()
def delete():
    new_path = open('snips/bgp_delete.json').read()
    add_delete = example.client.deleteconfig(yangjson= new_path)
    print("Delete Completed")


cli.add_command(get)
cli.add_command(replace)
cli.add_command(merge)
cli.add_command(delete)

if __name__ == "__main__":
    cli()