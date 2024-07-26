
# GoogleChat

From direct messages to group conversations, Google Chat and Spaces help teams collaborate fluidly and efficiently from anywhere. Securely connect with anyone you work with, and take group work to the next level with shared chat, files and tasks.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root URL|API Root URL integration should use to connect to Google Chat service.|True|String|https://chat.googleapis.com/|
|Service Account|Service account JSON file content that chat bot should use to work with Google Chat service.|True|Password|None|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Chat service is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|linux64/aiohttp-3.6.2-cp37-cp37m-manylinux1_x86_64.whl|
|linux64/yarl-1.6.0-cp37-cp37m-manylinux1_x86_64.whl|
|linux64/multidict-4.7.6-cp37-cp37m-manylinux1_x86_64.whl|
|cross/tldextract-2.2.3-py2.py3-none-any.whl|
|cross/chardet-3.0.4-py2.py3-none-any.whl|
|cross/attrs-20.2.0-py2.py3-none-any.whl|
|cross/TIPCommon-1.0.11-py2.py3-none-any.whl|
|cross/idna-2.10-py2.py3-none-any.whl|
|cross/google_auth-1.22.0-py2.py3-none-any.whl|
|cross/pyasn1-0.4.8-py2.py3-none-any.whl|
|cross/requests_file-1.5.1-py2.py3-none-any.whl|
|cross/urllib3-1.25.10-py2.py3-none-any.whl|
|cross/async_timeout-3.0.1-py3-none-any.whl|
|cross/typing_extensions-3.7.4.3-py3-none-any.whl|
|cross/setuptools-50.3.0-py3-none-any.whl|
|cross/pyasn1_modules-0.2.8-py2.py3-none-any.whl|
|cross/certifi-2020.6.20-py2.py3-none-any.whl|
|cross/requests-2.24.0-py2.py3-none-any.whl|
|cross/six-1.15.0-py2.py3-none-any.whl|
|cross/rsa-4.6-py3-none-any.whl|
|cross/EnvironmentCommon-1.0.0-py3-none-any.whl|
|cross/cachetools-4.1.1-py3-none-any.whl|


## Actions
#### Send Message
Send a message to a Google Chat space that the Siemplify app was added to. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Space Name|Specify a space name to send message to. Example space name: AAAAdaTsel0|True|String||
|Message Text|Specify a message text to send.|True|String||



##### JSON Results
```json
{"name":"spaces/sPPxxxxxx/messages/vcm8Cxxxxxxxxxxx","sender":{"name":"users/1013903xxxxxxxx","displayName":"Quickstart app","domainId":"","type":"BOT","isAnonymous":false},"text":"Test Message","cards":[],"annotations":[],"thread":{"name":"spaces/sPPxxxxxxx/threads/vcm8Cxxxx"},"space":{"name":"spaces/sPPxxxxxxx","type":"DM","singleUserBotDm":true,"threaded":false,"displayName":""},"fallbackText":"","argumentText":"Test Message","attachment":[],"createTime":"2022-06-16T13:30:41.907695Z","lastUpdateTime":"2022-06-16T13:30:41.907695Z"}
```



#### Send Advanced Message
Send an advanced message to a Google Chat space based on provided message JSON payload. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Space Name|Specify a space name to send message to. Example space name: AAAAdaTsel0|True|String||
|Message JSON Payload|Specify a JSON payload to send with message. See article https://developers.google.com/chat/api/guides/message-formats/cards for the examples of messages payload.|True|String|{"cards":[{"sections":[{"widgets":[{"image":{"imageUrl":"https://..."}},{"buttons":[{"textButton":{"text":"OPEN IN GOOGLE MAPS","onClick":{"openLink":{"url":"https://..."}}}}]}]}]}]}|



##### JSON Results
```json
{"name":"spaces/sPPxxxxxx/messages/vcm8Cxxxxxxxxxxx","sender":{"name":"users/1013903xxxxxxxx","displayName":"Quickstart app","domainId":"","type":"BOT","isAnonymous":false},"text":"Test Message","cards":[],"annotations":[],"thread":{"name":"spaces/sPPxxxxxxx/threads/vcm8Cxxxx"},"space":{"name":"spaces/sPPxxxxxxx","type":"DM","singleUserBotDm":true,"threaded":false,"displayName":""},"fallbackText":"","argumentText":"Test Message","attachment":[],"createTime":"2022-06-16T13:30:41.907695Z","lastUpdateTime":"2022-06-16T13:30:41.907695Z"}
```



#### Ping
Test connectivity to the Google Chat service with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### List Spaces
List spaces that currently configured Google Chat bot was added to. Note: Action is not running on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter Google Chat spaces.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|String|50|
|Include User Memberships|If enabled, user memberships information will be added to the action Case Wall table and JSON result.|False|Boolean|false|



##### JSON Results
```json
[{"name": "spaces/sPPxO4xxxxx", "type": "DM", "singleUserBotDm": true, "threaded": false, "displayName": "", "memberships": [{"name": "spaces/sPPxO4xxxxx/members/114197761xxxxxx", "state": "JOINED", "member": {"name": "users/11419776166xxxxxx", "displayName": "Siemplify LAB Siemplify LAB", "domainId": "38jxxxxxx", "type": "HUMAN", "isAnonymous": false}, "createTime": "2022-04-26T04:47:18.031005Z"}]}]
```






## Jobs



## Connectors


