# IOS-XR over GRPC


This public repo contains python code that can be used to interact with the Cisco IOS XR devices.The environment is pre-configured to access the [Cisco DevNet Always-On Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/e83cfd31-ade3-4e15-91d6-3118b867a0dd?diagramType=Topology). You can edit the variables in the environment to point to your own IOS-XR device.


This package contains a library with the methods that are available to use over gRPC with IOS-XR boxes after 6.0.0. The API has several methods which allows a user to send simple RPC commands such as get and push using YANG and JSON.

The repo consists of two main components:

The compiled pb2 file from the proto definition.
A Python module accessing the pb2 file with the library bindings.

## Information

XR devices ship with the YANG files that define the data models they support. Using a management protocol such as NETCONF or gRPC, you can programmatically query a device for the list of models it supports and retrieve the model files.

gRPC is an open-source RPC framework. It is based on Protocol Buffers (Protobuf), which is an open source binary serialization protocol. gRPC provides a flexible, efficient, automated mechanism for serializing structured data, like XML, but is smaller and simpler to use. You define the structure using protocol buffer message types in .proto files. Each protocol buffer message is a small logical record of information, containing a series of name-value pairs.

## Getting Started


### Python Environment Setup
It is recommended that this code be used with Python 3.6. It is highly recommended to leverage Python Virtual Environments (venv).

Follow these steps to create and activate a venv.

### OS X or Linux
```
virtualenv venv --python=python3.6
source venv/bin/activate
```
Install the code requirements
```
Either download this repository or install with `pip install iosxr_grpc`
pip install click
```

### Enable gRPC

SSH in to the router and turn on gRPC and disable tls, below is an example configuration

```
grpc
 port 57777
 no-tls 
```

## Code Examples

Change to into the `examples` diretory and run the following code, this uses the yang model https://github.com/YangModels/yang/blob/master/vendor/cisco/xr/653/openconfig-interfaces.yang and will print all the interface from the Always-On Sandbox IOS-XR device in a `json` format.

```
(venv)python grpc_example.py 
{
    "openconfig-interfaces:interfaces": {
        "interface": [
            {
                "name": "Loopback100",
                "config": {
                    "name": "Loopback100",
                    "type": "iana-if-type:softwareLoopback",
                    "enabled": true,
                    "description": "***MERGE LOOPBACK 100****"
                },
                "subinterfaces": {
                    "subinterface": [
                        {
                            "index": 0,
                            "openconfig-if-ip:ipv4": {
                                "addresses": {
                                    "address": [
                                        {
                                            "ip": "1.1.1.100",
                                            "config": {
                                                "ip": "1.1.1.100",
                                                "prefix-length": 32
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            },
[/snip]
```


This code uses the JSON below is based off the YANG model provided by Cisco: https://github.com/YangModels/yang/blob/master/vendor/cisco/xr/653/Cisco-IOS-XR-ipv4-bgp-cfg.yang

You can walk through the hierachy using pyang, and create a JSON model similar to the example below. https://github.com/mbj4668/pyang/wiki/TreeOutput

This JSON model is for a BGP configuration. We can see that it is defining a BGP instance and a single neighbor.

```
{
 "Cisco-IOS-XR-ipv4-bgp-cfg:bgp": {
  "instance": [
   {
    "instance-name": "default",
    "instance-as": [
     {
      "as": 0,
      "four-byte-as": [
       {
        "as": 65400,
        "bgp-running": [
         null
        ],
        "default-vrf": {
         "global": {
          "router-id": "11.1.1.10",
          "global-afs": {
           "global-af": [
            {
             "af-name": "ipv4-unicast",
             "enable": [
              null
             ],
             "sourced-networks": {
              "sourced-network": [
               {
                "network-addr": "11.1.1.0",
                "network-prefix": 24
               }
              ]
             }
            }
           ]
          }
         },
         "bgp-entity": {
          "neighbors": {
           "neighbor": [
            {
             "neighbor-address": "11.1.1.20",
             "remote-as": {
              "as-xx": 0,
              "as-yy": 65450
             },
             "neighbor-afs": {
              "neighbor-af": [
               {
                "af-name": "ipv4-unicast",
                "activate": [
                 null
                ],
                "next-hop-self": true
               }
              ]
             }
            }
           ]
          }
         }
        }
       }
      ]
     }
    ]
   }
  ]
 }
}
```