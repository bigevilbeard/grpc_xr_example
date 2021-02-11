import sys
sys.path.insert(0, '../')
from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient
import json
from time import sleep

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

    def delete(self):
        path = open('snips/bgp_start.json').read()
        result = self.client.deleteconfig(path)
        print(result) # If this is sucessful, then there should be no errors.