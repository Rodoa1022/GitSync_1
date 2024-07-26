<p align="center"><img src="./Resources/Cybereason.svg" 
     alt="Cybereason" width="200"/></p>

# Cybereason

Cybereason automatically detects malicious activity and presents it in an intuitive way. It deploys easily with minimal organizational impact and provides end-to-end context of an attack campaign.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String||
|Username|None|True|String||
|Password|None|True|Password|None|
|Verify SSL|None|False|Boolean|False|


#### Dependencies
| |
|-|
|cross/TIPCommon-1.0.10-py3-none-any.whl|
|cross/chardet-4.0.0-py2.py3-none-any.whl|
|cross/requests_file-1.5.1-py2.py3-none-any.whl|
|cross/filelock-3.0.12-py3-none-any.whl|
|cross/tldextract-3.1.0-py2.py3-none-any.whl|
|cross/urllib3-1.26.6-py2.py3-none-any.whl|
|cross/certifi-2021.5.30-py2.py3-none-any.whl|
|cross/EnvironmentCommon-1.0.0-py3-none-any.whl|
|cross/six-1.16.0-py2.py3-none-any.whl|
|cross/requests-2.25.1-py2.py3-none-any.whl|
|cross/idna-2.9-py2.py3-none-any.whl|


## Actions
#### List Malop Affected Machines
List machines affected by the Malop in Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Malop ID|Specify the ID of the malop for which you want to return affected machines.|True|String||
|Results Limit|Specify how many results to return. Default: 100|True|String|100|
|Create Hostname Entity|If enabled, action will create an entity based on machines name.|False|Boolean|false|



##### JSON Results
```json
[{"simpleValues":{"freeMemory":{"totalValues":1,"values":["610844672"]},"freeDiskSpace":{"totalValues":1,"values":["8435953664"]},"timeStampSinceLastConnectionTime":{"totalValues":1,"values":["4643703153"]},"isActiveProbeConnected":{"totalValues":1,"values":["false"]},"timezoneUTCOffsetMinutes":{"totalValues":1,"values":["0"]},"hasRemovableDevice":{"totalValues":1,"values":["false"]},"cpuCount":{"totalValues":1,"values":["2"]},"totalMemory":{"totalValues":1,"values":["2113499136"]},"lastSeenTimeStamp":{"totalValues":1,"values":["1622047044535"]},"platformArchitecture":{"totalValues":1,"values":["ARCH_AMD64"]},"domainFqdn":{"totalValues":1,"values":["pearson.net"]},"hasSuspicions":{"totalValues":1,"values":["false"]},"adCanonicalName":{"totalValues":1,"values":["pearson.net/Domain Controllers/DC01"]},"totalDiskSpace":{"totalValues":1,"values":["32210153472"]},"osType":{"totalValues":1,"values":["WINDOWS"]},"adOU":{"totalValues":1,"values":["Domain Controllers"]},"osVersionType":{"totalValues":1,"values":["Windows_Server_2016"]},"hasMalops":{"totalValues":1,"values":["false"]},"isIsolated":{"totalValues":1,"values":["true"]},"adSid":{"totalValues":1,"values":["S-1-5-21-1411487056-1755689160-1727733893-xxxx"]},"pylumId":{"totalValues":1,"values":["PYLUMCLIENT_INTEGRATION_DC01_0xxxx"]},"adDNSHostName":{"totalValues":1,"values":["dc01.pearson.net"]},"adDisplayName":{"totalValues":1,"values":["DC01$"]},"uptime":{"totalValues":1,"values":["454585"]},"elementDisplayName":{"totalValues":1,"values":["dc01"]},"isSuspiciousOrHasSuspiciousProcessOrFile":{"totalValues":1,"values":["true"]}},"elementValues":{"networkInterfaces":{"totalValues":2,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"removableDevices":{"totalValues":0,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"drivers":{"totalValues":141,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"mountPoints":{"totalValues":2,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"users":{"totalValues":9,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"autoruns":{"totalValues":928,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"suspiciousProcesses":{"totalValues":1113,"elementValues":null,"totalSuspicious":1113,"totalMalicious":1001,"guessedTotal":0},"processes":{"totalValues":53449,"elementValues":null,"totalSuspicious":14063,"totalMalicious":1017,"guessedTotal":0},"services":{"totalValues":241,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"logonSessions":{"totalValues":101,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"self":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"-1514448867.119877508955xxxx","name":"dc01","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{},"filterData":{"sortInGroupValue":"-1514448867.1198775089551518743","groupByValue":"MachineRuntime:-1514448867.11987750895xxxxadCanonicalName=pearson.net/Domain Controllers/DC01 , adCompany=null , adDNSHostName=dc01.pearson.net , adDepartment=null , adDescription=null , adDisplayName=DC01$ , adLocation=null , adMachineRole=null , adOU=Domain Controllers , adOrganization=null , adSid=S-1-5-21-1411487056-1755689160-1727733893-xxx , computerName=dc01 , "},"isMalicious":false,"suspicionCount":0,"guidString":"-1514448867.119877508955xxxx","labelsIds":null,"malopPriority":null,"malicious":false,"suspect":false}]
```



#### Get Malop
Retrieve detailed information about a malop in Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Malop ID|Specify the ID of the malop for which you want to return details.|True|String||



##### JSON Results
```json
{"simpleValues":{"hasRansomwareSuspendedProcesses":{"totalValues":1,"values":["false"]},"decisionFeatureSet":{"totalValues":1,"values":["Process.connectionToBlackListAddressByAddressRootCause(Malop decision)"]},"rootCauseElementCompanyProduct":{"totalValues":0,"values":null},"decisionFeature":{"totalValues":1,"values":["Process.connectionToBlackListAddressByAddressRootCause(Malop decision)"]},"detectionType":{"totalValues":1,"values":["BLACKLIST"]},"totalReceivedBytes":{"totalValues":1,"values":["1280975"]},"malopActivityTypes":{"totalValues":2,"values":["MALICIOUS_INFECTION","CNC_COMMUNICATION"]},"elementDisplayName":{"totalValues":1,"values":["CNC_COMMUNICATION"]},"creationTime":{"totalValues":1,"values":["1625577635462"]},"isBlocked":{"totalValues":1,"values":["false"]},"totalNumberOfOutgoingConnections":{"totalValues":1,"values":["2"]},"totalNumberOfIncomingConnections":{"totalValues":1,"values":["0"]},"rootCauseElementTypes":{"totalValues":1,"values":["IpAddress"]},"malopStartTime":{"totalValues":1,"values":["1621476953475"]},"rootCauseElementNames":{"totalValues":1,"values":["10.2.x.xx"]},"totalTransmittedBytes":{"totalValues":1,"values":["37707"]},"malopLastUpdateTime":{"totalValues":1,"values":["1625577635462"]},"allRansomwareProcessesSuspended":{"totalValues":1,"values":["false"]},"rootCauseElementHashes":{"totalValues":0,"values":null}},"elementValues":{"suspects":{"totalValues":1,"elementValues":[{"elementType":"Process","guid":"-1514448867.-24138770923xxxx","name":"powershell.exe","hasSuspicions":true,"hasMalops":true}],"totalSuspicious":1,"totalMalicious":1,"guessedTotal":0},"filesToRemediate":{"totalValues":0,"elementValues":null,"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"primaryRootCauseElements":{"totalValues":1,"elementValues":[{"elementType":"IpAddress","guid":"0.-88015870624xxxxx","name":"10.2.101.39","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"affectedUsers":{"totalValues":1,"elementValues":[{"elementType":"User","guid":"0.-2528084736xxxxx","name":"pearson\\devin","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"rootCauseElements":{"totalValues":1,"elementValues":[{"elementType":"IpAddress","guid":"0.-88015870624xxxxx","name":"10.2.101.39","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"affectedMachines":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"-1514448867.1198775xxxxx","name":"dc01","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{},"filterData":{"sortInGroupValue":"11.-4838364314188xxxx","groupByValue":"MalopProcessRuntime:11.-4838364314188xxxx "},"isMalicious":false,"suspicionCount":0,"guidString":"11.-4838364314188xxxx","labelsIds":null,"malopPriority":null,"malicious":false,"suspect":false,"@class":".DetectionMalopDetailsModel","guid":"11.1440956455257300628","status":"Active","displayName":"powershell.exe","rootCauseElementType":"Process","rootCauseElementNamesCount":1,"detectionEngines":["Script"],"detectionTypes":["Malicious floating module"],"malopDetectionType":"MALICIOUS_PROCESS","machines":[{"@class":".MachineDetailsModel","guid":"-1514448867.1198775089551xxxx","displayName":"dc01","osType":"WINDOWS","connected":false,"isolated":true,"lastConnected":1622047044535,"adOU":"Domain Controllers","adOrganization":null,"adDisplayName":"DC01$","adDNSHostName":"dc01.pearson.net","adDepartment":null,"adCompany":null,"adLocation":null,"adMachineRole":null,"pylumId":"PYLUMCLIENT_INTEGRATION_DC01_xxxx"}],"users":[{"guid":"0.-252808473653xxxx","displayName":"pearson\\devin","admin":true,"localSystem":false,"domainUser":false,"adSid":null,"adDisplayName":"Devin M.","adLogonName":"devin@pearson.net","adDepartment":null,"adSamAccountName":"devin","adMemberOf":"CN=Domain Admins,CN=Users,DC=pearson,DC=net, CN=Administrators,CN=Builtin,DC=pearson,DC=net","adCompany":null,"adAssociatedDomain":null,"adMail":null,"adOU":"SPECTER","adPrimaryGroupID":"5xx","adCountry":null}],"creationTime":1620890240130,"lastUpdateTime":1625267485993,"labels":null,"iconBase64":"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQjSURBVFhH7ZZZT1NREMf5CHwUHkw0PrCDskmVYPRNTcBEBYoioIgWrKzWLSbqE4iiCSEKJiaIEMBdRJCiggsUZassVgTZdZw5S++9PZdFn/knk1to7/nNmTPzv9dvXesyU2BK056wzA6IOuXyiT7YiiGva46T+msvXnshOn8A4grGLAJpVGhGmyfh4h+QsePCEuw4vwDbHXNgOTsDltJpiC/5CduKf0Bc0QQtBLFnvkGMfQRiTg+xxaNsX1jSBNuS+wm2nPgAkTndEHHsHURkd+HnHogrHLcJpCbcfQDdqMDPzUF6BSagg28r+k6LIHwUYu1uhA9zeN4y8OMcHp7Vyf7G+60Cq4nKTwuzBC789sL7Rv8AqbFrwQgv0MMHITrvK+6+3xx+jMP58fbhOp4AgdWECZQRlMMXET4PFscMg0s1OudXhtN5535G+EdTeNjR1+yoBNIo/NKlh293zOK5/4J7bQsCz9XgnMXSLwM/KeE9EHn8PcLfQni2E8Iz3yC8HUIzXlEFmwRSU2Bqsz9l7AuPL52C+OJJLP+8wHOVVlPDmcBzTeBZEt7GqoBrqg0YlNpiodIo8JJJzNiDZZ9gO9frXM3EP8FDj7SyvsBmVkcwKO2xDRtDheP/CC7HraHT2BOOu2Oi6RB+wgSeqcFDDr9gVcNx9hdYTSFHXjbJWV8OLmfd2T8n8Fxn77i1jke4HDcGP6rBg9OfUQO7BNIoynitRpNYNAC9I8aeSDpPO9dmXXZ8aIYGpyuOdZlAagpJfx5A57i60Qx6jaa+Y0qgua5Ut5nAXwFWFnB9CLY+YUeCY64aEGZmpV0qcJNZP3h1WNn9z+k5iEq7bQ4/TPCngD3GmhWnTDUgPKMyBl4F7qgZh+nZ3wLL1djaC4HJN7HET1eE45SxfhJIo7B0LgWuM5rE4kF41m3sftp1UVkLbEy6oxiNF45JSTi6LJ2/akA4Iv5knXLWOZw3HcEPXXOD27MosFzdrlFIzKqCIOtj01n3wvF7CafE8BmjGhCWzELlVcYtfwgqmycFUtON+x2wYe8tCEOoOZx3==","priority":null,"decisionStatuses":["Detected"],"severity":"High","malopCloseTime":null,"group":null,"signer":null,"fileClassificationType":null,"filePaths":[],"commandLines":[],"decodedCommandLines":[],"detectionValues":["boo.lang.parser","boo.lang.extensions"],"detectionValueTypes":["DVT_MODULE"],"fileHash":"21d5224e20a4be7f303ab6c4b9f219d0d70904ee","scriptDetectionTypes":["SDT_PS_MALICIOUS_FLOATING_MODULE"],"exploitDetectionTypes":[],"descriptions":["39 malicious floating modules were loaded to a .NET application"],"hasAnyScanEvent":false,"activeProcessesCount":41,"totalProcessesCount":165,"fileSuspects":null,"processSuspects":[{"@class":".ProcessSuspectDetailsModel","firstSeen":1621638682415,"lastSeen":1621638682415,"counter":1,"wasEverDetectedInScan":false,"wasEverDetectedByAccess":false,"detectionDecisionStatus":"DDS_DETECTED","processGuid":"-1514448867.34111033995xxxx","elementDisplayName":"powershell.exe","pid":null,"ownerMachine":"dc01","calculatedUser":"pearson\\devin","commandLine":"powershell -Command \"$File=\\\"C:\\Users\\DEVIN~1.PEA\\AppData\\Local\\Temp\\2\\bbotstage.png\\\";$Content=get-content $File;$Contento=[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($Content));Set-ExecutionPolicy Bypass -Scope Process -Force;IEX($Contento)\"","creationTime":1621638669788,"endTime":null}],"processes":[{"@class":".ProcessDetailsModel","lastDetectionDecisionStatus":"DDS_DETECTED","guid":"-1187140749.-41580595400xxxx","elementDisplayName":"powershell.exe","pid":636,"ownerMachine":"dc02","calculatedUser":"pearson\\devin","commandLine":"powershell -command Invoke-Expression","creationTime":1623346351305,"endTime":1623365448375}],"files":[],"connections":[{"@class":".ConnectionDetailsModel","lastDetectionDecisionStatus":null,"direction":"OUTGOING","serverAddress":"104.26.8.77","serverPort":"443","portType":"SERVICE_HTTP","receivedBytesCount":802277,"transmittedBytesCount":418,"remoteAddressCountryName":null,"ownerMachine":"dc02","ownerProcess":"powershell.exe","creationTime":1624295799841,"endTime":1624295899685,"elementDisplayName":"10.2.101.150:57682 > 104.26.8.77:443","guid":"-1187140749.739369188209xxxx"}],"timelineEvents":[{"@class":".MalopStartTimelineEventModel","timestamp":1620890112125,"data":{"detectionTypes":["Malicious floating module"],"detectionEngines":["Script"]},"type":"malopStart"}],"payloads":[],"edr":false,"escalated":false}
```



#### Isolate Machine
Isolate a machine in Cybereason. Supported entities: Hostname.
Timeout - 600 Seconds



#### Enrich Entities
Enrich entities using information from Cybereason. Supported entities: Hostname, IP Address, File Hash, URL (action will strip domain part from URL entity). Note: IP Address for this action refers to external IP addresses. Only MD5 and SHA-1 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insights|If enabled, action will create an insight for each enriched entity.|False|Boolean|true|
|Only Malicious Entity Insight|If enabled, action will create an insight only for entities that have type: ransomware, maltool, unwanted, malware, blacklist. Note: this affects only IP Address, File Hash and URL entities, for Hostname entity action will still create an insight.|False|Boolean|true|



##### JSON Results
```json
[{"Entity":"ef742XXXXXXXXXX334d3964082361a460bfdb975", "EntityResult": {"requestKey":{"sha1":"ef7420141bb15ac334d3964082361a460bfdb975","md5":null},"ttl":81198007,"allowFurtherClassification":true,"cpId":2,"cpType":"VIRUS_TOTAL","aggregatedResult":{"maliciousClassification":{"type":"indifferent","classificationScore":-1,"typeScore":-1},"productClassification":{"productType":"NONE","type":"NONE","manufacturer":"Microsoft Corporation","signatureVerified":true,"externalSignatureVerificationStatus":"SIGNATURE_VERIFICATION_STATUS_SUCCESS","signed":true},"link":"https://www.virustotal.com/gui/file/334e69ac9367f708ce601a6f490ff227d6c20636da5222f148b25831d22e13d4/detection/f-334e69ac9367f708ce601a6f490ff227d6c20636da5222f148b25831d22e13d4-1626675202"},"simpleValues":{"totalMemory":{"totalValues":1,"values":["4244205568"]},"hasSuspicions":{"totalValues":1,"values":["false"]},"adCanonicalName":{"totalValues":1,"values":["cyberrange.attackiq.com/Computers/BCYBDW8888W10E1"]},"platformArchitecture":{"totalValues":1,"values":["ARCH_AMD64"]},"lastSeenTimeStamp":{"totalValues":1,"values":["1624949056021"]},"adSid":{"totalValues":1,"values":["S-1-5-21-925260173-1387230621-1164276501-2761"]},"freeDiskSpace":{"totalValues":1,"values":["35619577856"]},"osVersionType":{"totalValues":1,"values":["Windows_20H2"]},"isIsolated":{"totalValues":1,"values":["true"]},"freeMemory":{"totalValues":1,"values":["495063040"]},"elementDisplayName":{"totalValues":1,"values":["bcybdw8888w10e1"]},"totalDiskSpace":{"totalValues":1,"values":["84827230208"]},"hasRemovableDevice":{"totalValues":1,"values":["false"]},"cpuCount":{"totalValues":1,"values":["2"]},"pylumId":{"totalValues":1,"values":["PYLUMCLIENT_INTEGRATION_BCYBDW8888W10E1_02004C4F4F50"]},"isActiveProbeConnected":{"totalValues":1,"values":["false"]},"domainFqdn":{"totalValues":1,"values":["cyberrange.attackiq.com"]},"hasMalops":{"totalValues":1,"values":["false"]},"timeStampSinceLastConnectionTime":{"totalValues":1,"values":["1840046194"]},"adDNSHostName":{"totalValues":1,"values":["bcybdw8888w10e1.cyberrange.attackiq.com"]},"uptime":{"totalValues":1,"values":["4679861514"]},"osType":{"totalValues":1,"values":["WINDOWS"]}},"elementValues":{"networkInterfaces":{"totalValues":4,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"removableDevices":{"totalValues":0,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"mountPoints":{"totalValues":1,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"users":{"totalValues":7,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"autoruns":{"totalValues":1059,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"drivers":{"totalValues":171,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"processes":{"totalValues":91249,"elementValues":"None","totalSuspicious":18,"totalMalicious":18,"guessedTotal":0},"services":{"totalValues":249,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"logonSessions":{"totalValues":50,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"self":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"1848597613.1198775089551518743","name":"bcybdw8888w10e1","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{},"filterData":{"sortInGroupValue":"1848597613.1198775089551518743","groupByValue":"MachineRuntime:1848597613.1198775089551518743 adCanonicalName=cyberrange.attackiq.com/Computers/BCYBDW8888W10E1 , adCompany=null , adDNSHostName=bcybdw8888w10e1.cyberrange.attackiq.com , adDepartment=null , adDescription=null , adDisplayName=null , adLocation=null , adMachineRole=null , adOU=null , adOrganization=null , adSid=S-1-5-21-925260173-1387230621-1164276501-2761 , computerName=bcybdw8888w10e1 , "},"isMalicious":false,"suspicionCount":0,"guidString":"1848597613.1198775089551518743","labelsIds":"None","malopPriority":"None","malicious":false,"suspect":false,"additional_data":[{"simpleValues":{"sha1String":{"totalValues":1,"values":["3fb552a575713181856b208aff35545d4f22141e"]},"correctedPath":{"totalValues":1,"values":["c:\\windows\\temp\\ip2hh7fdnurmj\\files\\e7f9f801-5e87-47db-9001-a0c678d6b8fe\\x64\\mimikatz.exe"]},"maliciousClassificationType":{"totalValues":1,"values":["av_detected"]},"md5String":{"totalValues":1,"values":["8d0a0f482090df08b986c7389c1401c2"]},"elementDisplayName":{"totalValues":1,"values":["mimikatz.exe"]}},"elementValues":{"ownerMachine":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"-829873668.1198775089551518743","name":"acybdw8888w10a0","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{"reportedByAntiMalwareSuspicion":1626429338897},"filterData":{"sortInGroupValue":"-829873668.2242825736719868666","groupByValue":"FileHashRuntime:0.-1163446445045776925 "},"isMalicious":false,"suspicionCount":1,"guidString":"-829873668.2242825736719868666","labelsIds":null,"malopPriority":null,"malicious":false,"suspect":true},{"simpleValues":{"sha1String":{"totalValues":1,"values":["3fb552a575713181856b208aff35545d4f22141e"]},"correctedPath":{"totalValues":1,"values":["c:\\windows\\temp\\ewdvuuwzufu1e\\files\\e7f9f801-5e87-47db-9001-a0c678d6b8fe\\x64\\mimikatz.exe"]},"maliciousClassificationType":{"totalValues":1,"values":["av_detected"]},"md5String":{"totalValues":1,"values":["8d0a0f482090df08b986c7389c1401c2"]},"elementDisplayName":{"totalValues":1,"values":["mimikatz.exe"]}},"elementValues":{"ownerMachine":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"607055315.1198775089551518743","name":"acybdw8888w10a2","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{"reportedByAntiMalwareSuspicion":1626427273694},"filterData":{"sortInGroupValue":"607055315.-608333059050771302","groupByValue":"FileHashRuntime:0.-1163446445045776925 "},"isMalicious":false,"suspicionCount":1,"guidString":"607055315.-608333059050771302","labelsIds":null,"malopPriority":null,"malicious":false,"suspect":true}]}}]
```



#### List Processes
List processes based on provided criteria in Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Process Name|Specify a comma-separated list of process names for which you want to return data.|False|String||
|Machine Name|Specify a comma-separated list of machine names on which you want to search for processes.|False|String||
|Has Suspicions|If enabled, action will only return processes that are labeled as suspicious.|False|Boolean||
|Has Incoming Connection|If enabled, action will only return processes that have incoming connections.|False|Boolean||
|Has Outgoing Connection|If enabled, action will only return processes that have outgoing connections.|False|Boolean||
|Has External Connection|If enabled, action will only return processes that have external connections.|False|Boolean||
|Unsigned process with unknown reputation|If enabled, action will only return unsigned processes with unknown reputation.|False|Boolean||
|Running from temporary folder|If enabled, action will only return processes running from a temporary folder.|False|Boolean||
|Privilege Escalation|If enabled, action will only return processes with escalated privileges.|False|Boolean||
|Malicious use of PsExec|If enabled, action will only return processes related to malicious use of PsExec.|False|Boolean||
|Results Limit|Specify how many processes to return.|True|String||



##### JSON Results
```json
[{"simpleValues":{"imageFile.companyName":{"totalValues":1,"values":["value"]},"elementDisplayName":{"totalValues":1,"values":["value"]},"endTime":{"totalValues":1,"values":["value"]},"imageFile.md5String":{"totalValues":1,"values":["value"]},"imageFile.productName":{"totalValues":1,"values":["value"]},"isWhiteListClassification":{"totalValues":1,"values":["true"]},"productType":{"totalValues":1,"values":["value"]},"commandLine":{"totalValues":1,"values":["string"]},"creationTime":{"totalValues":1,"values":["string"]},"pid":{"totalValues":1,"values":["string"]},"executionPrevented":{"totalValues":1,"values":["false"]},"imageFile.maliciousClassificationType":{"totalValues":1,"values":["whitelist"]},"iconBase64":{"totalValues":1,"values":["string"]},"imageFile.sha1String":{"totalValues":1,"values":["value"]},"isImageFileSignedAndVerified":{"totalValues":1,"values":["true"]}},"elementValues":{"calculatedUser":{"totalValues":1,"elementValues":[{"elementType":"User","guid":"guid","name":"name","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"ownerMachine":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"guid","name":"name","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"parentProcess":{"totalValues":1,"elementValues":[{"elementType":"Process","guid":"guid","name":"name","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"imageFile":{"totalValues":1,"elementValues":[{"elementType":"File","guid":"guid","name":"name","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{"lsassEncryptionKeysReadSuspicion":1602000000000,"lsassMainAuthenticationPackageReadSuspicion":1602000000000,"maliciousNGAVDetectionOfPowershellSuspicion":1602000000000,"lsassSensitiveReadSuspicion":1602000000000,"powerShellDownloaderSuspcion":1602000000000,"unexpectedAuditObjectAccessLsassSuspicion":1602000000000,"maliciousUseOfPowershellSuspicion":1602000000000,"lsassSupplementalAuthenticationPackageReadSuspicion":1602000000000,"suspiciousUseOfPowershellSuspicion":1602000000000},"filterData":{"sortInGroupValue":"value","groupByValue":"powershell.exe"},"isMalicious":true,"suspicionCount":9,"guidString":"guid","labelsIds":"None","malopPriority":"None","malicious":true,"suspect":true}]
```



#### Is Probe Connected
Check the connectivity of the endpoint to Cybereason. Supported entities: Hostname.
Timeout - 600 Seconds



##### JSON Results
```json
{"Entity":"bxxxdw0000w10e1","EntityResult":{"is_connected":"false"}}
```



#### Prevent File
Add hash to a blacklist in Cybereason. Supported entities: File Hash. Note: only MD5 hashes are supported.
Timeout - 600 Seconds



#### List Reputation Items
List information about items with reputation in Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Logic|Specify what filter logic should be applied.|False|List|None|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied.|False|String||
|Max Results To Return|Specify how many results to return. Default: 50|False|String||



##### JSON Results
```json
{"key":"8cc79ae4XXXXXXXXXXXXd50a60ec99f4","reputation":"blacklist","prevent_execution":"false","comment":"null","remove":"false"}
```



#### Unisolate Machine
Unisolate a machine in Cybereason. Supported entities: Hostname.
Timeout - 600 Seconds



#### List files
Get information about files from Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Hash|Specify a comma-separated list of file hashes for which you want to return data. Note: action only supports SHA-1 and MD5 hashes. If you provide values for this parameter, then parameter “Results Limit“ is ignored. Action will try to find information about all provided hashes. |False|String||
|Results Limit|Specify how many files to return.|True|String||
|Fields To Return|Specify a comma-separated list of fields that you want to return. If nothing is provided, action will work with predefined fields. Possible values: md5String,ownerMachine,avRemediationStatus,isSigned,signatureVerified,sha1String,maliciousClassificationType,createdTime,modifiedTime,size,correctedPath,productName,productVersion,companyName,internalName,elementDisplayName.|False|String||



##### JSON Results
```json
[{"simpleValues":{"size":{"totalValues":1,"values":["28160"]},"sha1String":{"totalValues":1,"values":["3de58e6c504a9daXXXXXXXd20a5c9576d280065d"]},"isSigned":{"totalValues":1,"values":["false"]},"modifiedTime":{"totalValues":1,"values":["1585124888222"]},"maliciousClassificationType":{"totalValues":1,"values":["indifferent"]},"md5String":{"totalValues":1,"values":["21f73cd5562XXXXXXXbce53eafbef128"]},"signatureVerified":{"totalValues":1,"values":["false"]},"createdTime":{"totalValues":1,"values":["1585124888221"]},"elementDisplayName":{"totalValues":1,"values":["python_sb_609645112_bs_1718922.exe"]},"correctedPath":{"totalValues":1,"values":["c:\\program files\\safebreach\\safebreach endpoint simulator\\app\\20.1.10\\simvenv\\scripts\\python_sb_609645112_bs_1718922.exe"]}},"elementValues":{"ownerMachine":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"1589170329.1198000000051518743","name":"dasdfp-sb01","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{"blackListedFileSuspicion":1601020416198},"filterData":{"sortInGroupValue":"1589170329.999000000000785885","groupByValue":"FileHashRuntime:0.-8076888620413037613 "},"isMalicious":false,"suspicionCount":1,"guidString":"1589170329.999000000000785885","labelsIds":"None","malopPriority":"None","malicious":false,"suspect":true}]
```



#### Set Reputation
Set a reputation for entity in Cybereason. Supported entities: File Hash, IP Address, URL (action will extract domain part). Note: only MD5 and SHA1 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reputation List Type|Specify the reputation that needs to be applied to an entity.|True|List|None|



#### Ping
Test connectivity to the Cybereason with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Update Malop Status
Update status for the Malop in Cybereason. Note: detection malops support only "Remediated", "Not Relevant" or "Open" statuses.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Malop ID|Specify the ID of the malop that needs to be updated.|True|String||
|Status|Specify the new status for the malop.|True|List|None|



#### List Malop Processes
List processes related to the Malop in Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Malop ID|Specify the ID of the malop for which you want to return related processes.|True|String||
|Results Limit|Specify how many results to return.|True|String||



##### JSON Results
```json
{"simpleValues":{"imageFile.companyName":{"totalValues":1,"values":["Microsoft Corporation"]},"elementDisplayName":{"totalValues":1,"values":["msbuild.exe"]},"endTime":{"totalValues":1,"values":["1616000008438"]},"imageFile.md5String":{"totalValues":1,"values":["e10ce76b0000000853cf8d183fc7f60"]},"imageFile.productName":{"totalValues":1,"values":["Microsoft® .NET Framework"]},"isWhiteListClassification":{"totalValues":1,"values":["false"]},"productType":{"totalValues":1,"values":["NONE"]},"commandLine":{"totalValues":1,"values":["C:\\Windows\\Microsoft.Net\\Framework\\v4.0.30319\\MSBuild.exe trusted_developer_utilities.csproj"]},"creationTime":{"totalValues":1,"values":["1616632385801"]},"pid":{"totalValues":1,"values":["11160"]},"executionPrevented":{"totalValues":1,"values":["false"]},"imageFile.maliciousClassificationType":{"totalValues":1,"values":["indifferent"]},"iconBase64":{"totalValues":1,"values":["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"]},"imageFile.sha1String":{"totalValues":1,"values":["1d81004900000000000073d540a09171b1b9899c"]},"isImageFileSignedAndVerified":{"totalValues":1,"values":["true"]}},"elementValues":{"children":{"totalValues":2,"elementValues":"None","totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"calculatedUser":{"totalValues":1,"elementValues":[{"elementType":"User","guid":"0.-9151230000000005773","name":"d3test4\\system","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"ownerMachine":{"totalValues":1,"elementValues":[{"elementType":"Machine","guid":"280830967.1198000000001518743","name":"d3test4","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"parentProcess":{"totalValues":1,"elementValues":[{"elementType":"Process","guid":"280830967.-547400000000680005","name":"cmd.exe","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0},"imageFile":{"totalValues":1,"elementValues":[{"elementType":"File","guid":"280830967.-3976000000065521329","name":"msbuild.exe","hasSuspicions":false,"hasMalops":false}],"totalSuspicious":0,"totalMalicious":0,"guessedTotal":0}},"suspicions":{"maliciousNGAVDetectionOfPowershellSuspicion":1616612345687},"filterData":{"sortInGroupValue":"280830967.1638000000456730051","groupByValue":"msbuild.exe"},"isMalicious":true,"suspicionCount":1,"guidString":"280830967.1638000000456730051","labelsIds":"None","malopPriority":"None","malicious":true,"suspect":true,"@class":".ProcessSuspectDetailsModel","firstSeen":1621600002415,"lastSeen":1621600002415,"counter":1,"wasEverDetectedInScan":false,"wasEverDetectedByAccess":false,"detectionDecisionStatus":"DDS_DETECTED","processGuid":"-1514448867.3411000000009435213","elementDisplayName":"powershell.exe","pid":"None","ownerMachine":"XX01","calculatedUser":"XXXXson\\XXXin","commandLine":"powershell -Command ","creationTime":162160000088,"endTime":"None"}
```



#### Remediate Malop
Perform remediation action on the malop in Cybereason. Note: Action is running as async, please adjust script timeout value in Chronicle SOAR IDE for action as needed. To get a list of remediation unique ids, please run the action "List Malop Remediations".
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Malop ID|Specify the ID of the malop which you want to remediate.|True|String||
|Remediation Unique IDs|Specify a comma-separated list of the remediation actions that need to be executed. This value can be retrieved from the action "List Malop Remediations".|True|String||



##### JSON Results
```json
[{"malopId":"NOMALOP","remediationId":"75e6e05c-99be-4c64-92c5-a237f1c1177a","start":1684176792584,"end":null,"initiatingUser":"string","final_status":"SUCCESS","target_name":"abcd-efgh","statusLog":[{"machineId":"ClfZtxCi55eyTiwX","targetId":"ClfZt5Hmhmiu6g-U","status":"PENDING","actionType":"KILL_PROCESS","error":null,"timestamp":1684176793876,"empty":false},{"machineId":"ClfZtxCi55eyTiwX","targetId":"ClfZt5Hmhmiu6g-U","status":"IN_PROGRESS","actionType":"KILL_PROCESS","error":null,"timestamp":1684176793981,"empty":false},{"machineId":"ClfZtxCi55eyTiwX","targetId":"ClfZt5Hmhmiu6g-U","status":"SUCCESS","actionType":"KILL_PROCESS","error":null,"timestamp":1684176794006,"empty":false}],"empty":false}]
```



#### Get Sensor Details
Get sensor details of entities in Cybereason. Supported entities: Hostname, IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insight|If enabled, action will create an insight containing information about the sensor.|False|Boolean|true|



##### JSON Results
```json
[{"Entity":"10.0.xxx.xxx","EntityResult":{"sensorId":"5e77883de4b0575xxxxxxxxxx:PylumClient_integration_720500371520xxxxxxx","pylumId":"PylumClient_integration_720500371520xxxxxx","guid":"1301212619.11987750895xxxxxxx","fqdn":"macbookpro-909e","machineName":"Adi’s MacBook Pro","internalIpAddress":"10.0.xxx.xxx","externalIpAddress":"24.23.xxx.xxx","siteName":"Default","siteId":0,"ransomwareStatus":"DISABLED","preventionStatus":"NOT_INSTALLED","isolated":false,"disconnectionTime":1636598475639,"lastPylumInfoMsgUpdateTime":1636592697045,"status":"Offline","serviceStatus":"Down","onlineTimeMS":0,"offlineTimeMS":0,"staleTimeMS":0,"archiveTimeMs":null,"statusTimeMS":0,"lastStatusAction":"None","archivedOrUnarchiveComment":"","sensorArchivedByUser":"","serverName":"integration-1-t","serverId":"5e77883de4b057xxxxxx","serverIp":"10.203.xxx.xxx","privateServerIp":"10.203.xxx.xxx","collectiveUuid":null,"osType":"OSX","osVersionType":"12.0.1","collectionStatus":"SUSPENDED","version":"20.2.244.0","consoleVersion":null,"firstSeenTime":1636398294435,"upTime":2612,"cpuUsage":0,"memoryUsage":0,"outdated":false,"amStatus":"AM_FIRST_TIME_INITIALIZATION","amModeOrigin":null,"avDbVersion":"","avDbLastUpdateTime":0,"powerShellStatus":"PS_DISABLED","remoteShellStatus":"AC_DISABLED","usbStatus":"DISABLED","fwStatus":"DISABLED","antiExploitStatus":"AE_UNKNOWN","documentProtectionStatus":"DS_UNKNOWN","documentProtectionMode":"DM_UNKNOWN","organizationalUnit":"","antiMalwareStatus":"AM_ENABLED","antiMalwareModeOrigin":null,"organization":"integration","proxyAddress":"","preventionError":"","exitReason":"STOP_REQUEST_FROM_PYLUM","actionsInProgress":0,"pendingActions":[],"lastUpgradeResult":"None","department":null,"location":null,"criticalAsset":null,"deviceType":null,"customTags":null,"lastUpgradeSteps":[],"disconnected":true,"staticAnalysisDetectMode":"DISABLED","staticAnalysisDetectModeOrigin":null,"staticAnalysisPreventMode":"DISABLED","staticAnalysisPreventModeOrigin":null,"collectionComponents":[],"sensorLastUpdate":0,"fullScanStatus":"UNKNOWN","quickScanStatus":"UNKNOWN","lastFullScheduleScanSuccessTime":0,"lastQuickScheduleScanSuccessTime":0,"policyName":"Default","deliveryTime":1636398435235,"policyId":"be944da9-89e9-48e0-8c84-xxxxxxx","compliance":false,"groupId":null,"groupName":"Unassigned"}}]
```



#### Allow File
Remove hash from a blacklist in Cybereason. Supported entities: File Hash. Note: only MD5 hashes are supported.
Timeout - 600 Seconds



#### Add Comment To Malop
Add a comment to an existing malop in Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Malop ID|Specify the ID of the malop to which you want to add a comment.|True|String||
|Comment|Specify the comment for the malop.|True|String||



#### Clear Reputation
Clear the reputation of the entity in Cybereason. Supported entities: File Hash, IP Address, URL (action will strip domain part from URL entity). Note: only MD5 and SHA1 hashes are supported.
Timeout - 600 Seconds



#### List Malop Remediations
List available remediations for a malop in Cybereason.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Malop ID|Specify the ID of the malop for which you want to list available remediations.|True|String||



##### JSON Results
```json
[{"uniqueId":"QUARANTINE_FILE::Q127xR36N9FSGZlV","remediationType":"QUARANTINE_FILE","targetName":"lockless.exe","targetId":"Q127xR36N9FSGZlV","machineName":"desktop-v22rbe5","machineId":"Q127xRCi55eyTiwX","machinesCount":1,"malopId":"AAAA1qdkdM5jUoWK","metaData":null,"malopType":"MalopDetectionEvents","machineConnected":false}]
```



#### Execute Custom Investigation Search
Execute investigation search based on parameters in Cybereason. This action supports nested queries for different item types.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query Filters JSON|Specify the query that needs to be executed. Note: the query should follow a strict pattern of "{API field } {Operator} {Value}". For multiple values you need to provide an "OR" key. Each new filter needs to be a separate item in the list. Each key represents the request type, for example, machine or user. Please refer to the documentation portal to understand what an API field name is. Possible operators: Equals NotEquals ContainsIgnoreCase NotContainsIgnoreCase LessThan LessOrEqualsTo GreaterThan GreaterOrEqualsTo Between Includes NotIncludes|True|String|[{"request_type": "{request type 1}","queries": ["Query 1","Query 2"],"connection": "{connection feature}"},{"request_type": "{request type 2}","queries": ["Query 3"]}]|
|Fields To Return|Specify a comma-separated list of fields that need to be returned. Note: you need to provide API field names.|True|String|osVersionType,platformArchitecture,uptime,isActiveProbeConnected,lastSeenTimeStamp,timeStampSinceLastConnectionTime,mountPoints,processes,services,logonSessions,domainFqdn,timezoneUTCOffsetMinutes,domain,ownerMachine,ownerOrganization.name,isLocalSystem,emailAddress,avRemediationStatus,isSigned,signatureVerified,sha1String,maliciousClassificationType,createdTime,modifiedTime,size,correctedPath,productName,productVersion,companyName,internalName,elementDisplayName|
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{  "simpleValues": {  "isActiveProbeConnected": {  "totalValues": 1,  "values": [  "false"  ]  },  "uptime": {  "totalValues": 1,  "values": [  "334268"  ]  },  "timezoneUTCOffsetMinutes": {  "totalValues": 1,  "values": [  "330"  ]  },  "timeStampSinceLastConnectionTime": {  "totalValues": 1,  "values": [  "5637862539"  ]  },  "domainFqdn": {  "totalValues": 1,  "values": [  ""  ]  },  "lastSeenTimeStamp": {  "totalValues": 1,  "values": [  "1681878151155"  ]  },  "platformArchitecture": {  "totalValues": 1,  "values": [  "ARCH_AMD64"  ]  },  "elementDisplayName": {  "totalValues": 1,  "values": [  "desktop-bjgt1cr"  ]  },  "osVersionType": {  "totalValues": 1,  "values": [  "Windows_10"  ]  }  },  "elementValues": {  "ownerOrganization": [  {  "elementType": "Organization",  "guid": "AAAAEo0vR-BSveB6",  "name": null,  "hasSuspicions": false,  "hasMalops": false,  "elementValues": {},  "simpleValues": {}  }  ]  } }]
```



#### Execute Simple Investigation Search
Execute investigation search based on parameters in Cybereason. Note: this action doesn't support nested queries. Only one type of data, for example, machines or users can be queried at once. For nested queries refer to action "Execute Custom Investigation Search". Please refer to the documentation portal for more details.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Request Type|Specify what should be queried.|False|List|Machine|
|Query Filters|Specify the query that needs to be executed. Note: this query should follow a strict pattern of "{API field} {Operator} {Value}". For multiple values you need to provide an "OR" key. Each new filter needs to start from a new line. Please refer to the documentation portal to understand what an API field name is. Possible operators: Equals NotEquals ContainsIgnoreCase NotContainsIgnoreCase LessThan LessOrEqualsTo GreaterThan GreaterOrEqualsTo Between Includes NotIncludes|False|String|{API field name} {Operator} {Value} OR {Value}|
|Fields To Return|Specify a comma-separated list of fields that need to be returned. Note: you need to provide API field names.|True|String|osVersionType,platformArchitecture,uptime,isActiveProbeConnected,lastSeenTimeStamp,timeStampSinceLastConnectionTime,mountPoints,processes,services,logonSessions,domainFqdn,timezoneUTCOffsetMinutes,domain,ownerMachine,ownerOrganization.name,isLocalSystem,emailAddress,avRemediationStatus,isSigned,signatureVerified,sha1String,maliciousClassificationType,createdTime,modifiedTime,size,correctedPath,productName,productVersion,companyName,internalName,elementDisplayName|
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{  "simpleValues": {  "isActiveProbeConnected": {  "totalValues": 1,  "values": [  "false"  ]  },  "uptime": {  "totalValues": 1,  "values": [  "334268"  ]  },  "timezoneUTCOffsetMinutes": {  "totalValues": 1,  "values": [  "330"  ]  },  "timeStampSinceLastConnectionTime": {  "totalValues": 1,  "values": [  "5637862539"  ]  },  "domainFqdn": {  "totalValues": 1,  "values": [  ""  ]  },  "lastSeenTimeStamp": {  "totalValues": 1,  "values": [  "1681878151155"  ]  },  "platformArchitecture": {  "totalValues": 1,  "values": [  "ARCH_AMD64"  ]  },  "elementDisplayName": {  "totalValues": 1,  "values": [  "desktop-bjgt1cr"  ]  },  "osVersionType": {  "totalValues": 1,  "values": [  "Windows_10"  ]  }  },  "elementValues": {  "ownerOrganization": [  {  "elementType": "Organization",  "guid": "AAAAEo0vR-BSveB6",  "name": null,  "hasSuspicions": false,  "hasMalops": false,  "elementValues": {},  "simpleValues": {}  }  ]  } }]
```






## Jobs



## Connectors
#### Cybereason - Malops Inbox Connector
Pull alerts from Malops Inbox in Cybereason.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|@class|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Cybereason instance.|True|String|https:/{{api root}}|
|Username|Cybereason account username.|True|String||
|Password|Cybereason account password.|True|Password||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Cybereason server is valid.|False|Boolean|true|
|Severity Filter|Severity that will be used to fetch model breaches. If nothing is specified, action will ingest all alerts. Possible values: N/A, Low, Medium, High. If malop doesn’t have a severity, connector will apply Informational severity to Siemplify alert.|False|String||
|Status Filter|Status filter for the alerts. Possible values: Active, Remediated, Closed, Excluded.|False|String|Active|
|Max Hours Backwards|Amount of hours from where to fetch alerts.|False|Integer|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration.|False|Integer|10|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||




