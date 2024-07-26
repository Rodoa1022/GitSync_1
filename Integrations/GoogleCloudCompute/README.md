
# GoogleCloudCompute

Google Cloud Compute is the Infrastructure as a Service (IaaS) component of Google Cloud Platform which is built on the global infrastructure that runs Google's search engine, Gmail, YouTube and other services. Google Cloud Compute enables users to launch virtual machines (VMs) on demand. VMs can be launched from the standard images or custom images created by users. Google Cloud Compute users must authenticate based on OAuth 2.0 before launching the VMs.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Account Type|Type of the Google Cloud account. Located at the “type” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|service_account|
|Project ID|Project ID of the Google Cloud account. Located at the “project_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Private Key ID|Private Key ID of the Google Cloud account. Located at the “private_key_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|Password|None|
|Private Key|Private Key of the Google Cloud account. Located at the “private_key” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|Password|None|
|Client Email|Client Email of the Google Cloud account. Located at the “client_email” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Client ID|Client ID of the Google Cloud account. Located at the “client_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Auth URI|Auth URI of the Google Cloud account. Located at the “auth_uri” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://accounts.google.com/o/oauth2/auth|
|Token URI|Token URI of the Google Cloud account. Located at the “token_uri” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://oauth2.googleapis.com/token|
|Auth Provider X509 URL|Auth Provider X509 URL of the Google Cloud account. Located at the “auth_provider_x509_cert_url” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://www.googleapis.com/oauth2/v1/certs|
|Client X509 URL|Client X509 URL of the Google Cloud account. Located at the “client_x509_cert_url” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Service Account Json File Content|Optional: Instead of specifying private key id, private key and other parameters, specify here the full JSON content of the service account file. Other connection parameters will be ignored if this parameter is provided.|False|Password|None|
|Workload Identity Email|A Service Account Client Email to replace the usage of "Service Account Json File Content", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Cloud Compute service is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|soupsieve-2.2.1-py3-none-any.whl|
|chardet-3.0.4-py2.py3-none-any.whl|
|rsa-4.7.2-py3-none-any.whl|
|idna-2.10-py2.py3-none-any.whl|
|pyparsing-3.1.1-py3-none-any.whl|
|pyasn1-0.4.8-py2.py3-none-any.whl|
|setuptools-57.0.0-py3-none-any.whl|
|google_api_core-2.17.1-py3-none-any.whl|
|httplib2-0.20.2-py3-none-any.whl|
|google_cloud-0.34.0-py2.py3-none-any.whl|
|urllib3-1.25.11-py2.py3-none-any.whl|
|google_api_python_client-2.119.0-py2.py3-none-any.whl|
|beautifulsoup4-4.9.3-py3-none-any.whl|
|protobuf-4.24.1-py3-none-any.whl|
|pyasn1_modules-0.2.8-py2.py3-none-any.whl|
|cachetools-4.2.2-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|google_auth-2.28.1-py2.py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|requests-2.24.0-py2.py3-none-any.whl|
|TIPCommon-1.1.5.2-py2.py3-none-any.whl|
|google-3.0.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.62.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|certifi-2020.11.8-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|


## Actions
#### Start Instance
Start a previously stopped Google Cloud Compute Instance. Note that it can take a few minutes for the instance to enter the running status.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /project/{project_id}/zone/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to start. Instance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
{"id": "123456667", "name": "operation-1234-1234-1234-1234", "zone": "us-central1-a", "operationType": "start", "targetLink": "https://www.googleapis.com/compute/v1/projects/project111/zones/us-central1-a/instances/123456667", "targetId": "123456667", "status": "RUNNING", "user": "google-cloud-compute-spec@project111.iam.gserviceaccount.com", "progress": 0, "insertTime": "2021-06-07T05:44:01.508-07:00", "startTime": "2021-06-07T05:44:01.548-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/project111/zones/us-central1-a/operations/operation-1234-1234-1234-1234", "kind": "compute#operation"}
```



#### Get Instance IAM Policy
Gets the access control policy for the resource. Note that policy may be empty if no policy is assigned to the resource.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /project/{project_id}/zone/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to get policy for. Intsance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
[{"version": 1,"etag": "XXXXXXXX","bindings": [{"role": "roles/compute.XXXXXXX","members": ["user:XXXXXX@XXXXXX.XX"]}]}]
```



#### Update Firewall Rule
Update a firewall rule with given parameters in Google Cloud Compute. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project ID|Specify the name of the project of your firewall rule. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Firewall Rule|Specify firewall rule name to update.|False|String||
|Source IP ranges|Specify a comma-separated list of source IP ranges. Parameter supports 'none' value. If "none" value is provided, then the action will delete existing values for the firewall rule. If nothing is provided for the parameter, action will not update the existing value.|False|String||
|Source Tags|Specify a comma-separated list of source tags. Parameter supports 'none' value. If "none" value is provided, then the action will delete existing values for the firewall rule. If nothing is provided for the parameter, action will not update the existing value.|False|String||
|Resource Name|Specify the full resource name for the firewall rule. Format: projects/{project_id}/global/firewalls/{firewall}. This parameter has higher priority over the combination of "Project ID", and "Firewall Rule".|False|String||
|Source Service Accounts|Specify a comma-separated list of source service accounts. Parameter supports 'none' value. If "none" value is provided, then the action will delete existing values for the firewall rule. If nothing is provided for the parameter, action will not update the existing value.|False|String||
|TCP Ports|Specify a comma-separated list of TCP ports. If specified, action will use it to update determine allow / deny lists. Parameter supports 'all' and 'none' values.|False|String||
|UDP Ports|Specify a comma-separated list of UDP ports. If specified, action will use it to update determine allow / deny lists. Parameter supports 'all' and 'none' values.|False|String||
|Other Protocols|Specify a comma-separated list of other protocols. Parameter supports 'none' value. If 'all' specified, the action will allow all protocols including tcp and udp.|False|String||



##### JSON Results
```json
{"kind": "compute#operation", "id": "9160761312385876914", "name": "operation-1716223324528-618e5619d1f93-174eac81-6b38200d", "operationType": "patch", "targetLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/global/firewalls/yyyy", "targetId": "7886634413370691799", "status": "DONE", "user": "compute-admin@xxxxx.iam.gserviceaccount.com", "progress": 100, "insertTime": "2024-05-20T09:42:05.150-07:00", "startTime": "2024-05-20T09:42:05.164-07:00", "endTime": "2024-05-20T09:42:09.381-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/global/operations/operation-1716223324528-618e5619d1f93-174eac81-6b38200d"}
```



#### Add Labels To Instance
Add labels to the Google Cloud Compute Instance.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /project/{project_id}/zone/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to add labels to. Instance id can be found with the "List Instances" action.|False|String||
|Instance Labels|Specify instance lables to add to instance. Lables should be provided in the following format - label_key_name:label_value, for example: vm_label_key:label1. Parameter accepts multiple values as a comma separated string.|True|String||



##### JSON Results
```json
[{"id": "XXXXXXXXX", "name": "operation-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX", "zone": "XXX-XXXXXXXXX", "operationType": "setLabels", "targetLink": "https://www.googleapis.com/compute/v1/projects/XXXXXX-XXXXXXXXX-XXXXXXXXX/XXXXX/XX-XXXXX-XX/instances/XXXXXXXXX", "targetId": "XXXXXXXXX", "status": "RUNNING", "user": "XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX@XXXXXXXXX-XXXXXXXXX-XXXXXXXXX.XXXXXXXXX.XXXXXXXXX.XXXXXXXXX", "progress": 0, "insertTime": "2021-06-03T09:43:56.015-07:00", "startTime": "2021-06-03T09:43:56.023-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/XXXXXXXXX-XXXXXXXXX-XXXXXXXXX/zones/XX-XXXXXX-XXXX/operations/operation-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX", "kind": "compute#operation"}]
```



#### Enrich Entities
Enrich Siemplify IP entities with instance information from Google Cloud Compute.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||



##### JSON Results
```json
[{"Entity": "1.1.1.1", "EntityResult": {"id": "1234", "creationTimestamp": "2021-04-28T21:34:57.369-07:00", "name": "instance-1", "description": "", "tags": {"fingerprint": "42WmSpB8rSM="}, "machineType": "f1-micro", "status": "RUNNING", "zone": "us-central1-a", "canIpForward": false, "networkInterfaces": [{"network": "default", "subnetwork": "default", "networkIP": "1.1.1.1", "name": "nic0", "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT", "natIP": "1.1.1.1", "networkTier": "PREMIUM", "kind": "compute#accessConfig"}], "fingerprint": "12345=", "kind": "compute#networkInterface"}], "disks": [{"type": "PERSISTENT", "mode": "READ_WRITE", "source": "instance-1", "deviceName": "instance-1", "index": 0, "boot": true, "autoDelete": true, "licenses": ["debian-10-buster"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "VIRTIO_SCSI_MULTIQUEUE"}], "diskSizeGb": "10", "kind": "compute#attachedDisk"}], "metadata": {"fingerprint": "12345=", "kind": "compute#metadata"}, "serviceAccounts": [{"email": "123456-compute@developer.gserviceaccount.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/12345/zones/us-central1-a/instances/instance-1", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false}, "cpuPlatform": "Intel Haswell", "labels": {"vm_test_tag": "tag1", "vm_new_label": "label1", "vm_test_tag2": "gabrieltag"}, "labelFingerprint": "12345=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedInstanceConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedInstanceIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialInstanceConfig": {"enableConfidentialCompute": false}, "fingerprint": "12345=", "lastStartTimestamp": "2021-05-11T01:01:28.994-07:00", "lastStopTimestamp": "2021-05-11T00:59:53.844-07:00", "kind": "compute#instance"}}, {"Entity": "1.1.1.1 ", "EntityResult": {"id": "720750400845139023", "creationTimestamp": "2021-06-01T01:41:05.363-07:00", "name": "instance-2", "description": "", "tags": {"fingerprint": "12345="}, "machineType": "e2-medium", "status": "TERMINATED", "zone": "us-central1-a", "canIpForward": false, "networkInterfaces": [{"network": "default", "subnetwork": "default", "networkIP": "1.1.1.1", "name": "nic0", "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT", "networkTier": "PREMIUM", "kind": "compute#accessConfig"}], "fingerprint": "12345=", "kind": "compute#networkInterface"}], "disks": [{"type": "PERSISTENT", "mode": "READ_WRITE", "source": "instance-2", "deviceName": "instance-2", "index": 0, "boot": true, "autoDelete": true, "licenses": ["debian-10-buster"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "VIRTIO_SCSI_MULTIQUEUE"}], "diskSizeGb": "10", "kind": "compute#attachedDisk"}], "metadata": {"fingerprint": "12345=", "kind": "compute#metadata"}, "serviceAccounts": [{"email": "123456-compute@developer.gserviceaccount.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/12345/zones/us-central1-a/instances/instance-2", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false}, "cpuPlatform": "Unknown CPU Platform", "labels": {"amit": "23", "kok": "2"}, "labelFingerprint": "123435=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedInstanceConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedInstanceIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialInstanceConfig": {"enableConfidentialCompute": false}, "fingerprint": "x-123123=", "lastStartTimestamp": "2021-06-01T01:41:21.651-07:00", "lastStopTimestamp": "2021-06-03T08:15:37.366-07:00", "kind": "compute#instance"}}]
```



#### Delete Instance
Delete the specified Google Cloud Compute instance.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /project/{project_id}/zone/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to delete. Instance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
{"id": "123465", "name": "operation-123456-123456-123456-123456", "zone": "us-central1-a", "operationType": "delete", "targetLink": "https://www.googleapis.com/compute/v1/projects/some-project/zones/us-central1-a/instances/123456", "targetId": "123456", "status": "RUNNING", "user": "google-cloud-compute-spec@some-project.iam.gserviceaccount.com", "progress": 0, "insertTime": "2021-06-07T07:36:22.400-07:00", "startTime": "2021-06-07T07:36:22.439-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/some-project/zones/us-central1-a/operations/operation-123456-123456-123456-123456", "kind": "compute#operation"}
```



#### Ping
Test connectivity to the Google Cloud Compute service with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Remove External IP Addresses
Remove external IP addresses on a Google Cloud Compute instance. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: projects/{project_id}/zones/{zone_id}/instances/{instance_id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to modify. Instance id can be found in "List Instances" action.|False|String||
|Network Interfaces|Specify a comma-separated list of network interfaces to modify. If this parameter is left empty or  “*” is provided then all of the network interfaces will be updated.|False|String|*|



##### JSON Results
```json
[{"kind": "compute#operation", "id": "1673537252688477099", "name": "operation-1716290883723-618f51c749f5b-876cd70d-3602a8a3", "zone": "us-west1-a", "operationType": "updateNetworkInterface", "targetLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/instances/yyyy", "targetId": "3905740668247239013", "status": "DONE", "user": "compute-admin@xxxxx.iam.gserviceaccount.com", "progress": 100, "insertTime": "2024-05-21T04:28:04.176-07:00", "startTime": "2024-05-21T04:28:04.190-07:00", "endTime": "2024-05-21T04:28:05.371-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/operations/operation-1716290883723-618f51c749f5b-876cd70d-3602a8a3"}, {"kind": "compute#operation", "id": "2531200345768541098", "name": "operation-1716290885077-618f51c894918-b3dbc881-cf094d9d", "zone": "us-west1-a", "operationType": "deleteAccessConfig", "targetLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/instances/yyyy", "targetId": "3905740668247239013", "status": "DONE", "user": "compute-admin@xxxxx.iam.gserviceaccount.com", "progress": 100, "insertTime": "2024-05-21T04:28:05.419-07:00", "startTime": "2024-05-21T04:28:05.430-07:00", "endTime": "2024-05-21T04:28:06.549-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/operations/operation-1716290885077-618f51c894918-b3dbc881-cf094d9d"}]
```



#### Set Instance IAM Policy
Sets the access control policy on the specified resource. Note that policy provided in action replaces any existing policy.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /project/{project_id}/zone/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to set policy for. Intsance id can be found in "List Instances" action.|False|String||
|Policy|Specify JSON policy document to set for instance.|True|String||



##### JSON Results
```json
[{"version": 1,"etag": "XXXXXXXX","bindings": [{"role": "roles/compute.XXXXXXX","members": ["user:XXXXXX@XXXXXX.XX"]}]}]
```



#### List Instances
List Google Cloud Compute instances based on the specified search criteria. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance Name|Specify instance name to search for. Parameter accepts multiple values as a comma separated string.|False|String||
|Instance Status|Specify instance status to search for. Parameter accepts multiple values as a comma separated string.|False|String||
|Instance Labels|Specify instance labels to search for in the format label_key_name:label_value, for example vm_label_key:label1. Parameter accepts multiple values as a comma separated string.|False|String||
|Max Rows to Return|Specify how many instances action should return.|False|String|50|



##### JSON Results
```json
[{"id": "12345", "creationTimestamp": "2021-04-28T21:34:57.369-07:00", "name": "xxxxxx-1", "description": "", "tags": {"fingerprint": "12345="}, "machineType": "f1-micro", "status": "RUNNING", "zone": "xxxxx-a", "canIpForward": false, "networkInterfaces": [{"network": "default", "subnetwork": "default", "networkIP": "1.1.1.1", "name": "xxx", "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT", "natIP": "1.1.1.1", "networkTier": "PREMIUM", "kind": "compute#accessConfig"}], "fingerprint": "1234=", "kind": "compute#networkInterface"}], "disks": [{"type": "PERSISTENT", "mode": "READ_WRITE", "source": "xxxxx-1", "deviceName": "xxxxx-1", "index": 0, "boot": true, "autoDelete": true, "licenses": ["debian-10-buster"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "VIRTIO_SCSI_MULTIQUEUE"}], "diskSizeGb": "10", "kind": "compute#attachedDisk"}], "metadata": {"fingerprint": "12345=", "kind": "compute#metadata"}, "serviceAccounts": [{"email": "1234-1234@1234.1234.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/1111111/zones/xxxxx-a/xxxxxs/xxxxx-1", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false}, "cpuPlatform": "Intel Haswell", "labels": {"vm_test_tag": "tag1", "vm_new_label": "label1", "vm_test_tag2": "tag2"}, "labelFingerprint": "12345=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedxxxxxConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedxxxxxIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialxxxxxConfig": {"enableConfidentialCompute": false}, "fingerprint": "123123=", "lastStartTimestamp": "2021-05-11T01:01:28.994-07:00", "lastStopTimestamp": "2021-05-11T00:59:53.844-07:00", "kind": "compute#xxxxx"}]
```



#### Stop Instance
Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /project/{project_id}/zone/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to stop. Instance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
{"id": "123456789", "name": "operation-123456-123456-123456-123456", "zone": "us-central1-a", "operationType": "stop", "targetLink": "https://www.googleapis.com/compute/v1/projects/some-zone/zones/us-central1-a/instances/123456789", "targetId": "123456789", "status": "RUNNING", "user": "google-cloud-compute-spec@some-zone.iam.gserviceaccount.com", "progress": 0, "insertTime": "2021-06-07T06:59:49.897-07:00", "startTime": "2021-06-07T06:59:49.936-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/some-zone/zones/us-central1-a/operations/operation-123456-123456-123456-123456", "kind": "compute#operation"}
```






## Jobs



## Connectors


