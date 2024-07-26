
# GoogleCloudAssetInventory

Cloud Asset Inventory is a fully-managed service that helps you discover, monitor, and analyze your Google Cloud and Anthos assets across projects and services. Cloud Asset Inventory provides a comprehensive view of your assets, including their configuration, relationships, and usage. This information can be used to improve your security posture, optimize your costs, and make better decisions about your cloud resources.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Google Cloud Asset Inventory instance.|True|String|https://cloudasset.googleapis.com|
|Organization ID|ID of the organization that should be used in Google Cloud Asset Inventory integration.|False|String||
|Project ID|ID of the Project that should be used in Google Cloud Asset Inventory integration. Takes precedence over "Organization ID".|False|String||
|User's Service Account|Service account of the Google Cloud Asset Inventory instance. A full content of the service account JSON file should be provided. This or "Workload Identity Email" must be provided.|False|Password|None|
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the "Service Usage Consumer" IAM role to your Google Cloud service account.|False|String||
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Cloud Asset Inventory server is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|linux64/regex-2022.9.13-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl|
|linux64/aiohttp-3.6.2-cp37-cp37m-manylinux1_x86_64.whl|
|linux64/yarl-1.6.0-cp37-cp37m-manylinux1_x86_64.whl|
|linux64/multidict-4.7.6-cp37-cp37m-manylinux1_x86_64.whl|
|cross/idna-3.3-py3-none-any.whl|
|cross/google_auth-2.5.0-py2.py3-none-any.whl|
|cross/tldextract-2.2.3-py2.py3-none-any.whl|
|cross/certifi-2021.10.8-py2.py3-none-any.whl|
|cross/chardet-3.0.4-py2.py3-none-any.whl|
|cross/attrs-20.2.0-py2.py3-none-any.whl|
|cross/pyparsing-3.0.7-py3-none-any.whl|
|cross/google_api_core-2.4.0-py2.py3-none-any.whl|
|cross/cachetools-5.0.0-py3-none-any.whl|
|cross/pyasn1-0.4.8-py2.py3-none-any.whl|
|cross/requests_file-1.5.1-py2.py3-none-any.whl|
|cross/setuptools-60.6.0-py3-none-any.whl|
|cross/httplib2-0.20.2-py3-none-any.whl|
|cross/beautifulsoup4-4.9.1-py3-none-any.whl|
|cross/async_timeout-3.0.1-py3-none-any.whl|
|cross/typing_extensions-3.7.4.3-py3-none-any.whl|
|cross/protobuf-3.19.4-py2.py3-none-any.whl|
|cross/google_api_python_client-2.36.0-py2.py3-none-any.whl|
|cross/google_auth_httplib2-0.1.0-py2.py3-none-any.whl|
|cross/requests-2.27.1-py2.py3-none-any.whl|
|cross/pyasn1_modules-0.2.8-py2.py3-none-any.whl|
|cross/rsa-4.8-py3-none-any.whl|
|cross/soupsieve-1.9.6-py2.py3-none-any.whl|
|cross/googleapis_common_protos-1.54.0-py2.py3-none-any.whl|
|cross/uritemplate-4.1.1-py2.py3-none-any.whl|
|cross/urllib3-1.26.8-py2.py3-none-any.whl|
|cross/six-1.16.0-py2.py3-none-any.whl|
|cross/charset_normalizer-2.0.11-py3-none-any.whl|
|cross/EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|cross/TIPCommon-1.1.6.1-py2.py3-none-any.whl|


## Actions
#### Get Resource Snapshot
Get information about the resource using Google Cloud Asset Inventory.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Names|Specify a comma-separated list of resources for which you want to fetch details.|True|String||
|Fields To Return|Specify a comma-separated list of fields to return. Note: every field should be in format with "assets.{field}" Example of values:assets.asset.name, assets.asset.assetType,assets.asset.resource.data.Note: assets.asset.name will always be returned.|False|String|*|



##### JSON Results
```json
[{"Entity": "//compute.googleapis.com/projects/project-id/zones/us-central1-a/instances/test-instance-2", "EntityResult": {"window": {"startTime": "2023-08-14T19:43:41.805828Z", "endTime": "2262-04-11T23:47:16.854775807Z"}, "asset": {"name": "//compute.googleapis.com/projects/project-id/zones/us-central1-a/instances/test-instance-2", "assetType": "compute.googleapis.com/Instance", "resource": {"version": "v1", "discoveryDocumentUri": "https://www.googleapis.com/discovery/v1/apis/compute/v1/rest", "discoveryName": "Instance", "parent": "//cloudresourcemanager.googleapis.com/projects/1111", "data": {"description": "", "serviceAccounts": [{"email": "1111-compute@developer.gserviceaccount.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "lastStartTimestamp": "2022-05-26T01:44:52.756-07:00", "deletionProtection": false, "name": "test-instance-2", "keyRevocationActionType": "NONE_ON_KEY_REVOCATION", "canIpForward": false, "shieldedInstanceIntegrityPolicy": {"updateAutoLearnPolicy": true}, "zone": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a", "resourceStatus": {}, "scheduling": {"onHostMaintenance": "MIGRATE", "preemptible": false, "provisioningModel": "STANDARD", "automaticRestart": true}, "machineType": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/machineTypes/e2-micro", "confidentialInstanceConfig": {"enableConfidentialCompute": false}, "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/instances/test-instance-2", "id": "8490693105130046232", "fingerprint": "MbrVGpwz9YU=", "startRestricted": false, "networkInterfaces": [{"network": "https://www.googleapis.com/compute/v1/projects/project-id/global/networks/test-vpc-network", "stackType": "IPV4_ONLY", "name": "nic0", "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/subnetworks/test-vpc-network-subnet", "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT", "natIP": "34.123.197.84", "networkTier": "PREMIUM"}], "fingerprint": "sMekMexYaNI=", "networkIP": "10.0.0.2"}], "allocationAffinity": {"consumeAllocationType": "ANY_ALLOCATION"}, "labelFingerprint": "42WmSpB8rSM=", "shieldedInstanceConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "cpuPlatform": "Intel Broadwell", "creationTimestamp": "2022-05-26T01:44:40.323-07:00", "status": "RUNNING", "disks": [{"guestOsFeatures": [{"type": "VIRTIO_SCSI_MULTIQUEUE"}, {"type": "SEV_CAPABLE"}, {"type": "UEFI_COMPATIBLE"}, {"type": "GVNIC"}], "interface": "SCSI", "shieldedInstanceInitialState": {"dbxs": []}, "diskSizeGb": "10", "deviceName": "test-instance-2", "type": "PERSISTENT", "source": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/disks/test-instance-2", "boot": true, "licenses": ["https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-1804-lts"], "index": 0, "autoDelete": true, "mode": "READ_WRITE"}], "tags": {"items": ["http-server"], "fingerprint": "FYLDgkTKlA4="}, "displayDevice": {"enableDisplay": false}, "reservationAffinity": {"consumeReservationType": "ANY_ALLOCATION"}}, "location": "us-central1-a"}, "ancestors": ["projects/1111", "organizations/2222"], "updateTime": "2023-08-14T19:43:41.805828Z"}}}, {"Entity": "//iam.googleapis.com/projects/project-id/serviceAccounts/109539808120564529093", "EntityResult": {"window": {"startTime": "2023-12-22T13:37:50Z", "endTime": "2262-04-11T23:47:16.854775807Z"}, "asset": {"name": "//iam.googleapis.com/projects/project-id/serviceAccounts/109539808120564529093", "assetType": "iam.googleapis.com/ServiceAccount", "resource": {"version": "v1", "discoveryDocumentUri": "https://iam.googleapis.com/$discovery/rest", "discoveryName": "ServiceAccount", "parent": "//cloudresourcemanager.googleapis.com/projects/1111", "data": {"name": "projects/project-id/serviceAccounts/cloud-asset-inventory@project-id.iam.gserviceaccount.com", "projectId": "project-id", "email": "cloud-asset-inventory@project-id.iam.gserviceaccount.com", "uniqueId": "109539808120564529093", "displayName": "Cloud Asset Inventory Automation", "oauth2ClientId": "109539808120564529093"}}, "ancestors": ["projects/1111", "organizations/2222"], "updateTime": "2023-12-22T13:37:50Z"}}}]
```



#### Enrich Resource
Enrich information about a Google Cloud resource using Google Cloud Asset Inventory.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Names|Specify a comma-separated list of resources for which you want to fetch details.|True|String||
|Fields To Return|Specify a comma-separated list of fields to return. Example of values:assetType,project,folders,organization,displayName,description,location,labels,networkTags,kmsKeys,createTime,updateTime,state,additionalAttributes, parentFullResourceName, parentAssetType. Note: name will always be returned. There is also an option to provide more advanced filters. For example, if you want to return a specific key from the "additionalAttributes" you can provide "additionalAttributes.{key}". Also, if you want to exclude a specific key from "additionalAttributes",then you can provide "-additionalAttributes.{key}".|False|String|*|



##### JSON Results
```json
[{"Entity": "//iam.googleapis.com/projects/test-project/serviceAccounts/123456789/keys/1d0b9d0d4641b4a1c09ce1ccc8b070454f2gfrd843","EntityResult": {"additionalAttributes": {"email": "test-2@test-project.iam.gserviceaccount.com","uniqueId": 123456789},"name": "//iam.googleapis.com/projects/test-project/serviceAccounts/123456789/keys/1d0b9d0d4641b4a1c09ce1ccc8b070454f2gfrd843","assetType": "iam.googleapis.com/ServiceAccountKey","project": "projects/123456789","displayName": "projects/test-project/serviceAccounts/test-service-account@test-project.iam.gserviceaccount.com/keys/1d0b9d0d4641b4a1c09ce1ccc8b070454f2gfrd843","createTime": "2022-05-26T17:35:07Z","versionedResources": [{"version": "v1","resource": {"keyAlgorithm": "KEY_ALG_RSA_2048","keyOrigin": "GOOGLE_PROVIDED","keyType": "USER_MANAGED","name": "projects/test-project/serviceAccounts/test-service-account@test-project.iam.gserviceaccount.com/keys/1d0b9d0d4641b4a1c09ce1ccc8b070454f2gfrd843","validAfterTime": "2022-05-26T17:35:07Z","validBeforeTime": "9999-12-31T23:59:59Z"}}],"organization": "organizations/123456789","parentFullResourceName": "//iam.googleapis.com/projects/test-project/serviceAccounts/test-service-account@test-project.iam.gserviceaccount.com","parentAssetType": "iam.googleapis.com/ServiceAccount"}}]
```



#### Ping
Test connectivity to the Google Cloud Asset Inventory with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### List Service Account Roles
List roles related to the Google Cloud service account using Google Cloud Asset Inventory.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Service Accounts|Specify a comma-separated list of service accounts for which you want to fetch details.|True|String||
|Check Roles|Specify a comma-separated list of roles that you want to check in relation to the service account. Example: roles/cloudasset.owner|False|String||
|Check Permissions|Specify a comma-separated list of permission that you want to check in relation to the service account. Example: cloudasset.assets.listResource.|False|String||
|Expand Permissions|If enabled, action will return information about all of the unique permissions related to the resource.|False|Boolean|false|
|Max Roles To Return|Specify how many roles related to the service account to return.|True|String|100|
|Max Permissions To Return|Specify how many permissions related to the service account to return.|True|String|100|



##### JSON Results
```json
[{"Entity": "xxx@project.iam.gserviceaccount.com", "EntityResult": {"roles": ["roles/storage.admin"], "unique_permissions": ["storage.buckets.getIamPolicy"]}}]
```






## Jobs



## Connectors


