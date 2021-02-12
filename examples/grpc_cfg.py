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
    def __init__(self, host, port, timeout, user, password, creds=None, options=None):
        # self.client = CiscoGRPCClient('sbx-iosxr-mgmt.cisco.com', 19399, 10, 'admin', 'C1sco12345')
        self.client = CiscoGRPCClient(host=host, port=port, timeout=timeout, user=user, password=password)
    
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

    
device = CiscoGRPCClient('sbx-iosxr-mgmt.cisco.com', 19399, 10, 'admin', 'C1sco12345')


@click.group()
def cli():
    pass

@click.command()
def fact():
    click.secho("Retrieving Information")
    # get = json.loads((Example.get), sort_keys=True, indent=4)
    # cisco_sucks_at_keeping_up_with_stuff = Example.get
    # fact = json.loads(str(device.getconfig('path')(), sort_keys=True, indent=4))
    print(device.getconfig('path'))
    click.echo(fact)


@click.command()
def replace():
    click.secho("Replacing Configuration")
    # cisco_sucks_at_keeping_up_with_stuffs = Example.replace

    # get = json.loads((str(cisco_sucks_at_keeping_up_with_stuffs)))
    # print(Example.replace)
    click.echo(replace)

cli.add_command(fact)
cli.add_command(replace)
# cli.add_command(merge)
# cli.add_command(delete)

if __name__ == "__main__":
    cli()