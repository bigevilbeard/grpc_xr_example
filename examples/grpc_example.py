""" Basic gRPC getcall configuration. Shows how to set up the vairables
for tls and how to put into the class and get information from the box.
Need Cisco GRPC python library
https://github.com/bigevilbeard/grpc_xr_example
Credit: https://github.com/cisco-grpc-connection-libs/ios-xr-grpc-python/blob/master/examples/grpc_example.py
"""
import json
from grpc.framework.interfaces.face.face import AbortionError
import sys
sys.path.insert(0, '../')
from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient

def main():
    client = CiscoGRPCClient('sbx-iosxr-mgmt.cisco.com', 19399, 10, 'admin', 'C1sco12345')
    # path = '{"Cisco-IOS-XR-ipv4-bgp-cfg:bgp": [null]}'
    path = '{"openconfig-interfaces:interfaces": [null]}'
    try:
        err, result = client.getconfig(path)
        if err:
            print(err)
        print(json.dumps(json.loads(result), indent=4))
    except AbortionError:
        print(
            'Unable to connect to Sandbox, check your gRPC destination and configuration.'
            )

if __name__ == '__main__':
    main()