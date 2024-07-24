<p align="center"><img src="./Resources/SSH.svg" 
     alt="SSH" width="200"/></p>

# SSH

Connect to endpoints vis SSH and perform various operations.

Python Version - 3


#### Dependencies
| |
|-|
|asn1crypto-1.5.1-py2.py3-none-any.whl|
|cryptography-42.0.5-cp39-abi3-manylinux_2_28_x86_64.whl|
|PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl|
|paramiko-3.4.0-py3-none-any.whl|
|bcrypt-4.1.2-cp39-abi3-manylinux_2_28_x86_64.whl|
|pycparser-2.22-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|cffi-1.16.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Copy of Execute Program
Run script on a remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Program Path|The path to the program in the remote host.|True|String||
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port||False|String||



##### JSON Results
```json
None
```



#### Shutdown Machine
Shutdown remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x)|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port|The default port will be 22.|False|String||
|Wait Time|Time to wait before shutdown in minutes(e.g: now).|True|String||



#### List Processes
List running processes on a remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port|The default port will be 22.|False|String||



##### JSON Results
```json
{"Processes": ["USER,PID,%CPU,%MEM,VSZ,RSS,TTY,STAT,START,TIME,COMMAND", "root,1,0.0,0.0,193656,6656,?,Ss,Jan16,0:24,/usr/lib/systemd/systemd --system --deserialize 24", "root,32142,0.0,0.0,0,0,?,S,Jan22,0:32,[kworker/3:1]"]}
```



#### Run Command
Run command on a remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port||False|String||
|Command|Command content(e.g: ifconfig).|True|String||



##### JSON Results
```json
{"ifconfig": "ens32: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>mtu1500\ninet1.1.1.1netmask1.1.1.1broadcast1.1.1.1\ninet6fe80: : 2156: 9c37: 7a0d: 87eprefixlen64scopeid0x20<link>\nether00: 50: 56: b5: 70: e3txqueuelen1000(Ethernet)\nRXpackets7448423bytes1077754116(1.0GiB)\nRXerrors0dropped0overruns0frame0\nTXpackets370155bytes44300304(42.2MiB)\nTXerrors0dropped0overruns0carrier0collisions0\n\nlo: flags=73<UP,LOOPBACK,RUNNING>mtu65536\ninet1.1.1.1netmask1.1.1.1\ninet6: : 1prefixlen128scopeid0x10<host>\nlooptxqueuelen1000(LocalLoopback)\nRXpackets86bytes4780(4.6KiB)\nRXerrors0dropped0overruns0frame0\nTXpackets86bytes4780(4.6KiB)\nTXerrors0dropped0overruns0carrier0collisions0\n\n", "output": "ens32: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>mtu1500\ninet1.1.1.1netmask1.1.1.1broadcast1.1.1.1\ninet6fe80: : 2156: 9c37: 7a0d: 87eprefixlen64scopeid0x20<link>\nether00: 50: 56: b5: 70: e3txqueuelen1000(Ethernet)\nRXpackets7448423bytes1077754116(1.0GiB)\nRXerrors0dropped0overruns0frame0\nTXpackets370155bytes44300304(42.2MiB)\nTXerrors0dropped0overruns0carrier0collisions0\n\nlo: flags=73<UP,LOOPBACK,RUNNING>mtu65536\ninet1.1.1.1netmask1.1.1.1\ninet6: : 1prefixlen128scopeid0x10<host>\nlooptxqueuelen1000(LocalLoopback)\nRXpackets86bytes4780(4.6KiB)\nRXerrors0dropped0overruns0frame0\nTXpackets86bytes4780(4.6KiB)\nTXerrors0dropped0overruns0carrier0collisions0\n\n"}
```



#### List Connections
List all  connections on a remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port||False|String||



##### JSON Results
```json
{"Results": ["Proto,Recv-Q,Send-Q,Local,Address,Foreign,Address,State,PID/Program,name", "tcp,0,0,0.0.0.0:111,0.0.0.0:*,LISTEN,1/systemd", "tcp,0,0,0.0.0.0:22,0.0.0.0:*,LISTEN,10624/sshd"]}
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Execute Program
Run script on a remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port||False|String||
|Remote Program Path|The path to the program in the remote host.|True|String||



#### Delete Firewall Rule
Delete iptables Firewall rule (Example: INPUT -s 10.0.0.10 -j DROP)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port||False|String||
|IPtables Rule|Rule value(e.g: INPUT -s 10.0.0.10 -j DROP)|True|String||



#### Logoff User
Log off remote user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x)|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port|The default port will be 22.|False|String||
|Logoff Username|The username to log off.|True|String||



#### Reboot Machine
 Reboot remote server
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port|The default port will be 22.|False|String||



#### Terminate Process
Terminate process on a remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x)|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port||False|String||
|PROCESS|Process to terminate.|True|String||



#### Block IP Address in iptables
Add rule to iptables to block IP address
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x).|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port||False|String||
|Block IP Address|IP address to block(e.g: x.x.x.x).|True|String||



#### List iptables Rules
List iptables rules on a remote machine
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Remote Server|Remote server address(e.g: x.x.x.x)|True|String||
|Remote Username||True|String||
|Remote Password||True|Password||
|Remote Port|The default port will be 22.|False|String||
|Chain|The iptables chain that you wish to see (e.g: INPUT, OUTPUT, etc.)|False|String||



##### JSON Results
```json
{"-,Chain,Rule": ["-P,INPUT,ACCEPT", "-P,FORWARD,ACCEPT", "-P,OUTPUT,ACCEPT"]}
```









