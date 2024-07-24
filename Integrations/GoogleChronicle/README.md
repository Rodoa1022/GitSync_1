
# GoogleChronicle

Google SecOps enables you to examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed from within your enterprise. To enable the Google API client to communicate with the Backstory API you will need Google Developer Service Account Credential, https://developers.google.com/identity/protocols/OAuth2#serviceaccount.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|UI Root|UI root of the Chronicle instance. It will be used to create a link that points back to Chronicle across multiple actions.|True|String|https://{instance}.chronicle.security|
|API Root|API root of the Chronicle instance.|True|String|https://backstory.googleapis.com|
|User's Service Account|Service Account that is used for authentication. If not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password|None|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Chronicle server is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|linux64/regex-2022.9.13-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl|
|linux64/aiohttp-3.6.2-cp37-cp37m-manylinux1_x86_64.whl|
|linux64/yarl-1.6.0-cp37-cp37m-manylinux1_x86_64.whl|
|linux64/multidict-4.7.6-cp37-cp37m-manylinux1_x86_64.whl|
|cross/tldextract-2.2.3-py2.py3-none-any.whl|
|cross/chardet-3.0.4-py2.py3-none-any.whl|
|cross/attrs-20.2.0-py2.py3-none-any.whl|
|cross/idna-2.10-py2.py3-none-any.whl|
|cross/google_auth-1.22.0-py2.py3-none-any.whl|
|cross/pyasn1-0.4.8-py2.py3-none-any.whl|
|cross/requests_file-1.5.1-py2.py3-none-any.whl|
|cross/urllib3-1.25.10-py2.py3-none-any.whl|
|cross/async_timeout-3.0.1-py3-none-any.whl|
|cross/EnvironmentCommonOld-1.0.0-py2.py3-none-any.whl|
|cross/typing_extensions-3.7.4.3-py3-none-any.whl|
|cross/setuptools-50.3.0-py3-none-any.whl|
|cross/pyasn1_modules-0.2.8-py2.py3-none-any.whl|
|cross/certifi-2020.6.20-py2.py3-none-any.whl|
|cross/TIPCommon-1.1.3.2-py2.py3-none-any.whl|
|cross/requests-2.24.0-py2.py3-none-any.whl|
|cross/six-1.15.0-py2.py3-none-any.whl|
|cross/rsa-4.6-py3-none-any.whl|
|cross/EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|cross/cachetools-4.1.1-py3-none-any.whl|


## Actions
#### List Assets
List assets in Google Chronicle based on the related entities in the specified time frame. Supported entities: URL, IP Address, File hash. Only MD5, SHA-1 or SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Hours Backwards|Specify how many hours backwards to fetch the assets. Default: 1 hour.|False|String|1|
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time". If the "Max Hours Backwards" parameter is provided then action will use the "Max Hours Backwards" parameter to provide a time filter. This is done for backwards compatibility.|False|List|Max Hours Backwards|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Assets To Return|Specify how many assets to return in the response.|False|String|50|



##### JSON Results
```json
[{"Entity":"1.1.1.1","EntityResult":{"assets":[{"asset":{"assetIpAddress":"1.1.1.1"},"firstSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2020-10-03T00:22:00.944Z"},"lastSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2020-10-04T08:27:17.971Z"}},{"asset":{"hostname":"test1"},"firstSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2020-10-02T22:59:43.903Z"},"lastSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2020-10-04T05:44:33.464Z"}},{"asset":{"hostname":"test3"},"firstSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2020-07-27T18:22:42.861Z"},"lastSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2020-10-04T04:38:35.344Z"}},{"asset":{"hostname":"exampledomain"},"firstSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2019-12-04T13:46:34Z"},"lastSeenArtifactInfo":{"artifactIndicator":{"destinationIpAddress":"1.1.1.1"},"seenTime":"2020-10-04T08:27:17.971Z"}}],"uri":["https://ironmountain.backstory.chronicle.security/domainResults?domain=www.google.com&selectedList=DomainViewDistinctAssets&whoIsTimestamp=2020-09-27T12%3A07%3A34.166830443Z"]}}]
```



#### Execute Retrohunt
Execute a rule retrohunt in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule ID|Specify the ID of the rule for which you want to run retrohunt.|True|String||
|Time Frame|Specify a time frame for the results. If “Alert Time Till Now” is selected, action will use start time of the alert as start time for the search and end time will be current time. If “30 Minutes Around Alert Time” is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to “1 Hour Around Alert Time” and “5 Minutes Around Alert Time”. If “Custom” is selected, you also need to provide “Start Time”.|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if “Custom” is selected for the “Time Frame” parameter. Format: ISO 8601.|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and “Custom” is selected for the “Time Frame” parameter then this parameter will use current time.|False|String||



##### JSON Results
```json
{"retrohuntId": "xxxxxxxxx-xxxxx-xxxxx-89e8-xxxxxxxxx", "ruleId": "xxxxxxxxx-xxf66d-xx4cec-xx-xxxxxxxxx", "versionId": "xxxxxxxxx-f66d-xx-b682-xxxxxxxxx@xxxxxxxxx", "eventStartTime": "2023-10-14T02:02:49.943Z", "eventEndTime": "2023-10-14T07:02:49.943Z", "retrohuntStartTime": "2023-10-16T12:28:09.042884Z", "state": "RUNNING"}
```



#### Get Detection Details
Fetch information about a detection in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule ID|Specify the ID of the rule, which is related to the detection.|True|String||
|Detection ID|Specify the ID of the detection for which you want to fetch details.|True|String||



##### JSON Results
```json
{"type": "RULE_DETECTION", "detection": [{"ruleName": "dns_not_google", "urlBackToProduct": "https://unotest2.backstory-dev.chronicle.xxxx/alert?xxxx=xxxx-e380-xxxx-d29c-xxxx", "ruleId": "xxxx-f66d-xxxx-xxxx-xxxx", "ruleVersion": "xxxx-xxxx-xxxx-b682-xxxx@xxxx", "alertState": "ALERTING", "ruleType": "SINGLE_EVENT", "ruleLabels": [{"key": "priority", "value": "Medium"}, {"key": "severity", "value": "Medium"}], "riskScore": 40}], "createdTime": "2023-10-04T22:16:22.145254Z", "id": "xxxx-e380-xxxx-xxxx-xxxx", "timeWindow": {"startTime": "2023-10-04T21:18:44Z", "endTime": "2023-10-04T21:18:44Z"}, "collectionElements": [{"references": [{"event": {"metadata": {"productLogId": "xxxx-xxxx-xxxx45fc-xxxx-xxxx", "eventTimestamp": "2023-10-04T21:18:44Z", "eventType": "NETWORK_CONNECTION", "vendorName": "Palo Alto Networks", "productName": "NGFW", "productEventType": "Traffic - start", "ingestedTimestamp": "2023-10-04T21:31:03.790969Z", "id": "xxxx=", "logType": "UDM"}, "principal": {"hostname": "test3", "ip": ["x.x.0.x"], "port": 18985, "mac": ["00:00:00:0b:c9:11"], "asset": {"hostname": "test3", "ip": ["00.0.0.00"], "mac": ["00:00:00:0b:c9:11"]}}, "target": {"hostname": "youtube.com", "port": 4548, "asset": {"hostname": "youtube.com"}}, "securityResult": [{"action": ["ALLOW"]}], "network": {"sentBytes": "xxxxxxxxxxx", "receivedBytes": "xxxxxxxxxxx", "ipProtocol": "TCP", "sessionId": "xxxxxxxxxxx"}}}], "label": "e"}], "detectionTime": "2023-10-04T21:18:44Z"}
```



#### Ping
Test connectivity to the Google Chronicle with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Add Values To Reference List
Add values to a reference list in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference List Name|Specify the name of the reference list that needs to be updated|True|String||
|Values|Specify a comma-separated list of values that need to be added to a reference list|True|String||



##### JSON Results
```json
{"name": "xxxx", "description": "xxxx", "createTime": "xxx-11-xxxx:20:52.xxx", "lines": ["0.0.0.0/24"], "contentType": "AABB"}
```



#### Get Reference Lists
Get available reference lists in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter reference lists.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied.|False|List|Equal|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. “Equal” works with “title” parameter, while “Contains” works with all values in response. If nothing is provided in this parameter, the filter will not be applied.|False|String||
|Expanded Details|If enabled, action will return detailed information about the reference lists.|False|Boolean||
|Max Reference Lists To Return|Specify how many reference lists to return. Default: 100.|False|String|100|



##### JSON Results
```json
[{"name": "list_name_sXXXX", "description": "XXXX", "createTime": "XXXXX", "lines": ["XXXX"], "contentType": "XXXX"}]
```



#### Execute UDM Query
Execute custom UDM query in Google Chronicle. Note: 120 action executions are allowed per hour.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Specify the query that needs to be executed in Chronicle.|True|String||
|Time Frame|Specify a time frame for the results. If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time". If "Custom" is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601. Note: The maximum time window (start time to end time) is 90 days.|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Note: The maximum time window (start time to end time) is 90 days.|False|String||
|Max Results To Return|Specify how many results to return for the query. Default: 50. Maximum: 10000.|False|String|50|



##### JSON Results
```json
{"events":[{"name":"02c2c701c5bb7e7042701axxxxxxxxxx,4,16496990275xxxxx,EMAIL,","udm":{"metadata":{"eventTimestamp":"2022-04-11T17:43:47.586Z","eventType":"EMAIL_TRANSACTION","productName":"Chronicle Internal","ingestedTimestamp":"2022-04-11T15:50:21.912562Z","enrichmentState":"ENRICHED"},"principal":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","user":{"userid":"test","userDisplayName":"test test","windowsSid":"S-1-5-21-2623356xxx-8883713xxx-9684409xxx-xxxxx","emailAddresses":["test@example.com"],"productObjectId":"test","attribute":{"labels":[{"key":"2FA Enabled","value":"false"}]},"groupIdentifiers":["Contractors"],"title":"IT Support Agent","department":["Cymbal Investments IT Contractors"]},"ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"],"location":{"city":"San Francisco","state":"California","countryOrRegion":"US"},"asset":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"]}},"securityResult":[{"action":["ALLOW"]}],"network":{"email":{"from":"test@example.com","to":["test@example.com"],"subject":["I did not create this service account"]}}}},{"name":"02c2c701c5bb7e7042701axxxxxxxxxx,3,16496987245xxxxx,EMAIL,","udm":{"metadata":{"eventTimestamp":"2022-04-11T17:38:44.586Z","eventType":"EMAIL_TRANSACTION","productName":"Chronicle Internal","ingestedTimestamp":"2022-04-11T15:50:21.912562Z","enrichmentState":"ENRICHED"},"principal":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","user":{"userid":"test","userDisplayName":"test test","windowsSid":"S-1-5-21-2623356xxx-8883713xxx-9684409xxx-xxxxx","emailAddresses":["test@example.com"],"productObjectId":"test","attribute":{"labels":[{"key":"2FA Enabled","value":"false"}]},"groupIdentifiers":["Contractors"],"title":"IT Support Agent","department":["Cymbal Investments IT Contractors"]},"ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"],"location":{"city":"San Francisco","state":"California","countryOrRegion":"US"},"asset":{"hostname":"test-pc","assetId":"CS:8973060bcf1d441a8cf10exxxxxxxxxx","ip":["10.2.xx.xxx"],"mac":["b5:1c:8b:xx:xx:xx"]}},"securityResult":[{"action":["ALLOW"]}],"network":{"email":{"from":"test@example.com","to":["test@example.com"],"subject":["Did you create this service account"]}}}}]}
```



#### List Events
List events on the particular asset in the specified time frame. Supported entities: IP Address, Mac Address, Hostname. Note: action can only fetch 10000 events. Make sure to narrow down the timeframe for better results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event Types|Specify a comma-separated list of the event types that need to be returned. If nothing is provided, action will fetch all event types. Possible values: EVENTTYPE_UNSPECIFIED, PROCESS_UNCATEGORIZED, PROCESS_LAUNCH, PROCESS_INJECTION, PROCESS_PRIVILEGE_ESCALATION, PROCESS_TERMINATION, PROCESS_OPEN, PROCESS_MODULE_LOAD, REGISTRY_UNCATEGORIZED, REGISTRY_CREATION, REGISTRY_MODIFICATION, REGISTRY_DELETION, SETTING_UNCATEGORIZED, SETTING_CREATION, SETTING_MODIFICATION, SETTING_DELETION, MUTEX_UNCATEGORIZED, MUTEX_CREATION, FILE_UNCATEGORIZED, FILE_CREATION, FILE_DELETION, FILE_MODIFICATION, FILE_READ, FILE_COPY, FILE_OPEN, FILE_MOVE, FILE_SYNC, USER_UNCATEGORIZED, USER_LOGIN, USER_LOGOUT, USER_CREATION, USER_CHANGE_PASSWORD, USER_CHANGE_PERMISSIONS, USER_STATS, USER_BADGE_IN, USER_DELETION, USER_RESOURCE_CREATION, USER_RESOURCE_UPDATE_CONTENT, USER_RESOURCE_UPDATE_PERMISSIONS, USER_COMMUNICATION, USER_RESOURCE_ACCESS, USER_RESOURCE_DELETION, GROUP_UNCATEGORIZED, GROUP_CREATION, GROUP_DELETION, GROUP_MODIFICATION, EMAIL_UNCATEGORIZED, EMAIL_TRANSACTION, EMAIL_URL_CLICK, NETWORK_UNCATEGORIZED, NETWORK_FLOW, NETWORK_CONNECTION, NETWORK_FTP, NETWORK_DHCP, NETWORK_DNS, NETWORK_HTTP, NETWORK_SMTP, STATUS_UNCATEGORIZED, STATUS_HEARTBEAT, STATUS_STARTUP, STATUS_SHUTDOWN, STATUS_UPDATE, SCAN_UNCATEGORIZED, SCAN_FILE, SCAN_PROCESS_BEHAVIORS, SCAN_PROCESS, SCAN_HOST, SCAN_VULN_HOST, SCAN_VULN_NETWORK, SCAN_NETWORK, SCHEDULED_TASK_UNCATEGORIZED, SCHEDULED_TASK_CREATION, SCHEDULED_TASK_DELETION, SCHEDULED_TASK_ENABLE, SCHEDULED_TASK_DISABLE, SCHEDULED_TASK_MODIFICATION, SYSTEM_AUDIT_LOG_UNCATEGORIZED, SYSTEM_AUDIT_LOG_WIPE, SERVICE_UNSPECIFIED, SERVICE_CREATION, SERVICE_DELETION, SERVICE_START, SERVICE_STOP, SERVICE_MODIFICATION, GENERIC_EVENT, RESOURCE_CREATION, RESOURCE_DELETION, RESOURCE_PERMISSIONS_CHANGE, RESOURCE_READ, RESOURCE_WRITTEN, ANALYST_UPDATE_VERDICT, ANALYST_UPDATE_REPUTATION, ANALYST_UPDATE_SEVERITY_SCORE, ANALYST_UPDATE_STATUS, ANALYST_ADD_COMMENT|False|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|List|Custom|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Note: value "now" can also be used.|False|String||
|Reference Time|Specify the reference time for the event search. Format: YYYY-MM-DDThh:mmTZD. Note: if nothing is provided, action will use end time as reference time.|False|String||
|Output|Specify what should be the output for this action.|True|List|Events + Statistics|
|Max Events To Return|Specify how many events to process per entity type. Default: 100.|False|String|100|



##### JSON Results
```json
[{"Entity":"alan-centeno-pc","EntityResult":{"statistics":{"NETWORK_CONNECTION":10},"events":[{"metadata":{"eventTimestamp":"2020-09-28T17:20:00Z","eventType":"NETWORK_CONNECTION","productName":"Tanium Stream","productEventType":"NETWORK_DNS","ingestedTimestamp":"2020-09-28T16:28:11.615578Z"},"principal":{"hostname":"alan-centeno-pc","assetId":"TANIUM:alan-centeno-pc","process":{"pid":"1101","productSpecificProcessId":"TANIUM:32323"}},"target":{"hostname":"micrgsoft.com","user":{"userid":"alan"},"process":{"pid":"8172","file":{"md5":"a219fc7fcc93890a842183388f80369e","fullPath":"C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe"},"commandLine":"\"C:\\Program Files(x86)\\adobe\\acrobat reader dc\\reader\\acrord32.exe\" ...","productSpecificProcessId":"TANIUM:82315"}}}],"uri":["https://demodev.backstory.chronicle.security/"]}}]
```



#### Remove Values From Reference List
Remove values from a reference list in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference List Name|Specify the name of the reference list that needs to be updated.|True|String||
|Values|Specify a comma-separated list of values that need to be removed from a reference list.|True|String||



##### JSON Results
```json
{"name": "xxxx", "description": "xxxx", "createTime": "xxx-11-xxxx:20:52.xxx", "lines": ["0.0.0.0/24"], "contentType": "AABB"}
```



#### Is Value In Reference List
Check, if provided values are found in reference lists in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference List Names|Specify a comma-separated list of names of the reference list that needs to be searched.|True|String||
|Values|Specify a comma-separated list of values that need to be searched in reference lists.|True|String||
|Case Insensitive Search|If enabled, action will perform case insensitive matching.|False|Boolean|true|



##### JSON Results
```json
[{"Entity": "xxxx", "EntityResult": {"found_in": "xxxx", "not_found_in": [], "overall_status": "xxxx"}}]
```



#### Enrich Domain
Enrich domains using information from IOCs in Google Chronicle. Supported entities: Hostname, URL (action extracts domain part).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insight|If enabled, action will create an insight containing information about the entities.|False|Boolean|true|
|Only Suspicious Insight|If enabled, action will only create an insight for entities that are marked as suspicious. Note: "Create Insight" parameter needs to be enabled.|False|Boolean|false|
|Lowest Suspicious Severity|Specify the lowest severity that should be associated with domain in order to mark it suspicious.|True|List|Medium|
|Mark Suspicious N/A Severity|If enabled, action will mark the entity as suspicious, if information about severity is not available.|False|Boolean|True|



##### JSON Results
```json
[{"Entity": "https://professionallogistics.in", "EntityResult": {"sources": [{"sourceUrl": "https://tools.emergingthreats.net/docs/ET%20Intelligence%20Rep%20List%20Tech%20Description.pdf", "confidenceScore": {"strRawConfidenceScore": "77"}, "rawSeverity": "Medium", "category": "Drop site for logs or stolen credentials", "addresses": [{"port": [80], "domain": "professionallogistics.in"}], "firstActiveTime": "2020-03-20T00:00:00Z", "lastActiveTime": "2020-03-21T00:00:00Z"}], "uri": ["https://ironmountain.backstory.chronicle.security/domainResults?domain=professionallogistics.in&selectedList=DomainViewDistinctAssets&whoIsTimestamp=2020-10-04T07%3A39%3A29.770408493Z"]}}]
```



#### Get Rule Details
Fetch information about a rule in Google Chronicle.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule ID|Specify the ID of the rule for which you want to fetch details.|True|String||



##### JSON Results
```json
{"ruleId": "xxxx-b682-xxxx", "versionId": "xxxx-f-xxxx-xxxx@xxxx", "ruleName": "dns_not_google", "metadata": {"severity": "Medium", "priority": "Medium"}, "ruleText": "rule dns_not_google {\n meta:\n   severity = \"Medium\"\n   priority = \"Medium\"\n events:\n   $e.principal.ip != \"0.0.0.0\"\n   $e.network.dns.questions.name != /google/\n   $e.network.dns.questions.name != /gstatic.com/\n   $e.network.dns.questions.name != /gvt1.com/\n   $e.network.dns.questions.name != /gvt2.com/\n   $e.network.dns.questions.name != /youtube.com/\n \n condition:\n   $e\n}\n", "alertingEnabled": true, "liveRuleEnabled": true, "versionCreateTime": "2022-10-24T10:39:24.809839Z", "compilationState": "SUCCEEDED", "ruleType": "SINGLE_EVENT"}
```



#### Enrich IP
Enrich IP entities using information from IOCs in Google Chronicle. Supported entities: IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insight|If enabled, action will create an insight containing information about the entities.|False|Boolean|true|
|Only Suspicious Insight|If enabled, action will only create an insight for entities that are marked as suspicious. Note: "Create Insight" parameter needs to be enabled.|False|Boolean|false|
|Lowest Suspicious Severity|Specify the lowest severity that should be associated with IP in order to mark it suspicious.|True|List|Medium|
|Mark Suspicious N/A Severity|If enabled, action will mark the entity as suspicious, if information about severity is not available.|False|Boolean|True|



##### JSON Results
```json
[{"Entity": "213.227.145.147", "EntityResult": {"sources": [{"confidenceScore": {"strRawConfidenceScore": "High"}, "rawSeverity": "High", "category": "Blocked", "description": "Application.JS/Adware.Sculinst.I", "addresses": [{"domain": "special-offers.online"}, {"ipAddress": "213.227.145.147"}], "firstActiveTime": "1970-01-01T00:00:00Z", "lastActiveTime": "2020-10-06T00:26:12Z"}], "uri": ["https://ironmountain.backstory.chronicle.security/destinationIpResults?ip=213.227.145.147&referenceTime=2020-10-04T07%3A45%3A51.723475776Z&selectedList=IpViewDistinctAssets"]}}]
```



#### List IOCs
List all of the IoCs discovered within your enterprise within the specified time range.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Start Time|Fetches IOC Domain from the specified time. Value should be in RFC 3339 format (e.g. 2018-11-05T12:00:00Z). If not supplied, the default is the UTC time corresponding to 3 days earlier than current time.|False|String||
|Max IoCs to Fetch|Specify the maximum number of IoCs to return. You can specify between 1 and 10,000. The default is 50.|False|String|50|



##### JSON Results
```json
[{"artifact": {"domainName": "st.dynamicyield.com"}, "sources": [{"source": "ESET Threat Intelligence", "confidenceScore": {"normalizedConfidenceScore": "Low", "intRawConfidenceScore": 0}, "rawSeverity": "n/a", "category": "BlockedObject"}], "iocIngestTime": "2019-07-31T07:41:32.365Z", "firstSeenTime": "2018-10-03T00:11:17Z", "lastSeenTime": "2020-07-06T12:59:41Z", "uri": ["https://demodev.backstory.chronicle.security/domainResults?domain=st.dynamicyield.com&selectedList=DomainViewDistinctAssets&whoIsTimestamp=2020-10-07T12%3A39%3A56.925673179Z"]}]
```



#### Lookup Similar Alerts
Lookup similar alerts in Google Chronicle. Supported Chronicle alert types: RULE, EXTERNAL, IOC. Note: this action can only work with alerts that come from the "Chronicle Alerts Connector". Note: action can only fetch 10000 alerts. Make sure to narrow down the timeframe for better results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Specify a time frame for the results. If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened.  Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time".|False|List|Last Hour|
|IOCs / Assets|Specify a comma-separated list of IOCs or assets that you want to find in the alerts. Note: action will perform a different search for each item provided.|True|String||
|Similarity By|Specify what attributes need to be used, when the action is to search for similar alerts. If "Alert Name and Alert Type" is selected, action will try to find all of the alerts that have the same alert name and IOCs/Assets for the underlying alert type. If "Product" is selected, then action will try to find all of the alerts that originate from the same product and have the same IOCs/Assets, action will search among both "EXTERNAL" and "Rule" alerts. If "Only IOCs/Assets" is enabled, action will match the similarity only based upon the items provided in the parameter "IOCs/Assets", action will search among both "EXTERNAL" and "Rule" alerts.|False|List|Alert Name and Product|



##### JSON Results
```json
{"count":4,"distinct":[{"first_seen":"2021-12-01T20:47:02Z","last_seen":"2021-12-02T00:47:02Z","product_name":"Office 365","used_ioc_asset":"10.169.xxx.xxx","name":"Threat Model Positive Score:74","hostnames":"host-name","urls":"www.test.com","ips":"10.169.xxx.xxx","subjects":"Invoice for Goods","users":"test-user1, test-user2","email_addresses":"stanlee4@acme.com, tony@starkindustries.com","hashes":"xxxxxxxxxxxxxxxx","processes":"pr1, pr2","rule_urls":["www.rule-url.com"]},{"first_seen":"2021-12-01T20:47:02Z","last_seen":"2021-12-02T00:47:02Z","product_name":"Office 365","used_ioc_asset":"stanlee4@acme.com","name":"Threat Model Positive Score:74","hostnames":"host-name","urls":"www.test.com","ips":"10.169.xxx.xxx","subjects":"Invoice for Goods","users":"test-user1, test-user2","email_addresses":"stanlee4@acme.com, tony@starkindustries.com","hashes":"xxxxxxxxxxxxxxxx","processes":"pr1, pr2","rule_urls":["www.rule-url.com"]}],"processed_alerts":210,"run_time":0.640103,"external_url":"www.external-url.com"}
```






## Jobs

#### Google Chronicle Sync Job
This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM.
 Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|API Root|True|String|https://backstory.googleapis.com|
|User's Service Account|False|Password||
|Max Hours Backwards|False|String|24|
|Verify SSL|False|Boolean|true|

#### Google Chronicle Alerts Creator Job
This job will sync new SOAR alerts with Chronicle SIEM.
Note: This job is only supported from Chronicle SOAR version 6.2.30 and higher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|API Root|True|String|https://backstory.googleapis.com|
|User's Service Account|False|Password||
|Verify SSL|False|Boolean|true|



## Connectors
#### Google Chronicle - Chronicle Alerts Connector
Pull information about Rule based alerts from Google Chronicle. Note: dynamic list is used for filtering purposes. For all of the details please visit the documentation portal.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|alert_type|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|event_type|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Chronicle instance.|True|String|https://backstory.googleapis.com|
|User's Service Account|Service Account that is used for authentication. If not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password||
|Max Hours Backwards|Amount of hours from where to fetch alerts. Maximum: 167 hours.|False|Integer|1|
|Disable Event Splitting|If enabled, the connector will not split original events into multiple. If this parameter is enabled, you would see a matching count of events between Chronicle SIEM and SOAR.|False|Boolean|false|
|Max Alerts To Fetch|How many alerts per type to process per one connector iteration. Default: 100.|False|Integer|100|
|Fallback Severity|Specify the fallback severity for the detection. This parameter is going to be used, if Chronicle detection doesn't include any information related to the severity. Possible values: Critical, High, Medium, Low, Info.|True|String|Medium|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Chronicle server is valid.|False|Boolean|true|
|Proxy Server Address|The address of the proxy server to use.|False|String||
| Proxy Username| The proxy username to authenticate with.|False|String||
| Proxy Password| The proxy password to authenticate with.|False|Password||
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|Boolean|false|




