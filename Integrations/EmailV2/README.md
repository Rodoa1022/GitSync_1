
# EmailV2

Email integration over smtp and imap protocols

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sender's Address|None|True|String|user@mail.com|
|Sender's Display Name|None|True|String||
|SMTP Server Address|None|False|None|Not yet configured|
|SMTP Port|None|False|String|Not yet configured|
|IMAP Server Address|None|False|None|Not yet configured|
|IMAP Port|None|False|String|Not yet configured|
|Username|None|True|String|user@mail.com|
|Password|None|True|Password|None|
|SMTP - Use SSL|None|False|Boolean||
|IMAP - Use SSL|None|False|Boolean||
|SMTP - Use Authentication|None|False|Boolean||


#### Dependencies
| |
|-|
|cross/email-6.0.0a1.tar.gz|
|cross/olefile-0.46.zip|
|cross/TIPCommon-1.0.11-py2.py3-none-any.whl|
|cross/html2text-2018.1.9.tar.gz|
|cross/extract_msg-0.23.3-py2.py3-none-any.whl|
|cross/chardet-5.2.0-py3-none-any.whl|
|cross/urllib3-1.25.10-py2.py3-none-any.whl|
|cross/enum34-1.1.6-py3-none-any.whl|
|cross/PySocks-1.7.0-py3-none-any.whl|
|cross/six-1.11.0-py2.py3-none-any.whl|
|cross/six-1.13.0-py2.py3-none-any.whl|
|cross/backports.functools_lru_cache-1.5-py2.py3-none-any.whl|
|cross/soupsieve-1.9.2-py2.py3-none-any.whl|
|cross/pytz-2019.3-py2.py3-none-any.whl|
|cross/certifi-2024.2.2-py3-none-any.whl|
|cross/IMAPClient-2.1.0-py2.py3-none-any.whl|
|cross/icalendar-4.0.7-py2.py3-none-any.whl|
|cross/html2text-2019.8.11-py2.py3-none-any.whl|
|cross/charset_normalizer-3.3.2-py3-none-any.whl|
|cross/win_inet_pton-1.1.0-py2.py3-none-any.whl|
|cross/python_dateutil-2.7.0-py2.py3-none-any.whl|
|cross/emaildata-0.3.4-py3-none-any.whl|
|cross/beautifulsoup4-4.8.0-py3-none-any.whl|
|cross/idna-3.7-py3-none-any.whl|
|cross/bs4-0.0.1.tar.gz|
|cross/requests-2.31.0-py3-none-any.whl|
|cross/urllib3-2.0.7-py3-none-any.whl|
|cross/tzlocal-1.5.1.tar.gz|
|cross/EnvironmentCommon-1.0.1-py2.py3-none-any.whl|


## Actions
#### DownloadEmailAttachments
Download email attachments from email to specific file path on Siemplify server. Requires: IMAP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders|True|String|None|
|Download Path|File path on the server where to download the email attachments|True|String|None|
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated multiple message ids. If message id is provided, subject filter is ignored|False|String|None|
|Subject Filter|Filter condition to search emails by specific subject|False|String|None|



#### Move Email To Folder
Searches for emails in the source folder, then moves emails matching the search criteria to the target folder. Requires: IMAP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Source Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders.|True|String|None|
|Destination Folder Name|Destination folder to move emails to|True|String|None|
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated multiple message ids. If message id is provided, subject filter is ignored.|False|String|None|
|Subject Filter|Filter condition, specify what subject to search for emails|False|String|None|
|Only Unread|Filter condition, specify if search should look only for unread emails|False|Boolean|None|



#### Send Thread Reply
Send a message as a reply to the email thread.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message ID|Specify the ID of the message to which you want to send a reply.|True|String||
|Folder Name|Specify a comma-separated list of mailbox folders in which action should search for email. Note: you can set mail-specific folders, for example, "[Gmail]/All Mail" to search in all of the folders of Gmail mailbox. Additionally, folder name should match exactly the IMAP folder. If folder contains spaces, folder must be wrapped in double quotes.|True|String||
|Content|Specify the content of the reply.|True|Email Content||
|Attachment Paths|Specify a comma separated list of attachments file paths stored on the server for addition to the email.|False|String||
|Reply All|If enabled, action will send a reply to all recipients related to the original email. Note: this parameter has priority over "Reply To" parameter.|False|Boolean|true|
|Reply To|Specify a comma-separated list of emails to which you want to send this reply. If nothing is provided and "Reply All" is disabled, action will only send a reply to the sender of the email. If "Reply All" is enabled, action will ignore this parameter.|False|String||



##### JSON Results
```json
{"message_id":"<162556278608.14165.480701790xxxxxxxxxx@siemplify>","recipients":"test@example.com"}
```



#### Copy of Send Email
Send email message. Requires: SMTP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recipients|Arbitrary comma separated list of email addresses for the email recipients|True|String||
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email|False|String||
|BCC|BCC email address. Multiple addresses can be separated by commas|False|String||
|Subject|The email subject part|True|String||
|Content|The email body part, if Email HTML Template is set, action should support definition of body of the email with provided HTML template.|True|Email Content||
|Return message id for the sent email|If selected, action returns the message id for the sent email in JSON technical result. This message id when can be used for the 'Wait for Email from user' action to process user response|False|Boolean||
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email.|False|String||



##### JSON Results
```json
{"date": "2019-11-18 08:02:57.984000+00:00", "message_id": "<157406417676.181148.9624253160139989862@C3431448806>", "recipients": "aaa@aaa.com, bbb@bbb.com"}
```



#### Save Email Attachments To Case
Save email attachments from email stored in monitored mailbox to the Case Wall. Requires: IMAP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders.|True|String|None|
|Message ID|Message id to find an email to download attachments from.|False|String|None|
|Attachment To Save|If parameter is not specified - save all email attachments to the case wall. If parameter specified - save only matching attachment to the case wall.|False|String|None|



##### JSON Results
```json
{"emails":[{"name": "aaa@aaa.com_1574937477000", "message_id": "<CAHNaB8eum4Tc=fj4U-n42zJNf6hgN6jop+KqG+WC3eGret_ZmA@mail.gmail.com>", "email_uid": 14, "subject": "Test 35", "StartTime": 1574937477000, "EndTime": 1574937477000, "Environment": "Undefined", "body": "Test with attachment", "html_body": "<div>Test with attachment</div>", "text_body": "Test with attachment", "device_product": "Mail", "vendor": "Mail", "event_type": "Mailbox Alert", "from": "uuu@uuu.com", "to": "hhh@hhh.com", "managerReceiptTime": 1574937477000, "original_message": "", "reply_to": "", "answer": "", "url_1": "https://siemplify.co", "url_2": "github.com", "file_1_name": "Test email as MSG.zip", "file_1_md5": "fc0118857de51b68c6c38c71566d9a5c", "file_2_name": "small_jpg.jpg", "file_2_md5": "2c39ce6536da5891e3766005438d3b47", "extra_data_field": "ttt"}, {"name": "aaa@aaa.com_1574937477000", "message_id": "<CAHNaB8eum4Tc=fj4U-n42zJNf6hgN6jop+KqG+WC3eGret_ZmA@mail.gmail.com>", "email_uid": 14, "subject": "Test 35", "StartTime": 1574937477000, "EndTime": 1574937477000, "Environment": "Undefined", "body": "Test with attachment", "html_body": "<div>Test with attachment</div>", "text_body": "Test with attachment", "device_product": "Mail", "vendor": "Mail", "event_type": "Mailbox Alert", "from": "uuu@uuu.com", "to": "hhh@hhh.com", "managerReceiptTime": 1574937477000, "original_message": "", "reply_to": "", "answer": "", "url_1": "https://siemplify.co", "url_2": "github.com", "file_1_name": "Test email as MSG.zip", "file_1_md5": "fc0118857de51b68c6c38c71566d9a5c", "file_2_name": "small_jpg.jpg", "file_2_md5": "2c39ce6536da5891e3766005438d3b47", "extra_data_field": "ttt"}]}
```



#### Forward Email
Forward email including previous messages. Message_id of the email to forward needs to be provided as an action input parameter.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders. Note that you can set mail-specific folders, for example "[Gmail]/All Mail"  to search in all of the folders of Gmail mailbox. Additionally, folder name should match exactly the IMAP folder. If folder contains spaces, folder must be wrapped in double quotes.|True|String|None|
|Message ID of email to forward|message_id value of the email to forward.|True|String||
|Recipients|Arbitrary comma separated list of email addresses for the email recipients.|True|String|None|
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email.|False|String|None|
|BCC|BCC email address. Multiple addresses can be separated by commas.|False|String|None|
|Subject|The email subject part.|True|String|None|
|Content|The email body part, if Email HTML Template is set, action should support definition of body of the email with provided HTML template.|False|Email Content||
|Return message id for the forwarded email|If selected, action returns the message id for the sent email in JSON technical result.|False|Boolean|None|
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email.|False|String|None|



##### JSON Results
```json
{"date": "2019-11-18 08:02:57.984000+00:00", "message_id": "<157406417676.181148.9624253160139989862@C3431448806>", "recipients": "aaa@aaa.com, bbb@bbb.com"}
```



#### Delete Email
Delete one or multiple email from the mailbox that matches search criteria. Delete can be done for the first email that matched the search criteria, or it can be done for all matching emails. Requires: IMAP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders.|True|String|None|
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated list of message ids to search for. If message id is provided, subject, sender, recipient and time filters are ignored.|False|String|None|
|Subject Filter|Filter condition, specify subject to search for emails.|False|String|None|
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String|None|
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String|None|
|Days Back|Filter condition, specify in what time frame in days should action look for emails to delete. Note - Action works in days granularity only. 0 means it will search for mails from today.|False|String|None|
|Delete All Matching Emails|Filter condition, specify if action should delete all matched by criteria emails from the mailbox or delete only first match.|False|Boolean|None|



##### JSON Results
```json
{"emails":[{"name": "aaa@aaa.com_1574937477000", "message_id": "<CAHNaB8eum4Tc=fj4U-n42zJNf6hgN6jop+KqG+WC3eGret_ZmA@mail.gmail.com>", "email_uid": 14, "subject": "Test 35", "StartTime": 1574937477000, "EndTime": 1574937477000, "Environment": "Undefined", "body": "Test with attachment", "html_body": "<div>Test with attachment</div>", "text_body": "Test with attachment", "device_product": "Mail", "vendor": "Mail", "event_type": "Mailbox Alert", "from": "uuu@uuu.com", "to": "hhh@hhh.com", "managerReceiptTime": 1574937477000, "original_message": "", "reply_to": "", "answer": "", "url_1": "https://siemplify.co", "url_2": "github.com", "file_1_name": "Test email as MSG.zip", "file_1_md5": "fc0118857de51b68c6c38c71566d9a5c", "file_2_name": "small_jpg.jpg", "file_2_md5": "2c39ce6536da5891e3766005438d3b47", "extra_data_field": "ttt"}, {"name": "aaa@aaa.com_1574937477000", "message_id": "<CAHNaB8eum4Tc=fj4U-n42zJNf6hgN6jop+KqG+WC3eGret_ZmA@mail.gmail.com>", "email_uid": 14, "subject": "Test 35", "StartTime": 1574937477000, "EndTime": 1574937477000, "Environment": "Undefined", "body": "Test with attachment", "html_body": "<div>Test with attachment</div>", "text_body": "Test with attachment", "device_product": "Mail", "vendor": "Mail", "event_type": "Mailbox Alert", "from": "uuu@uuu.com", "to": "hhh@hhh.com", "managerReceiptTime": 1574937477000, "original_message": "", "reply_to": "", "answer": "", "url_1": "https://siemplify.co", "url_2": "github.com", "file_1_name": "Test email as MSG.zip", "file_1_md5": "fc0118857de51b68c6c38c71566d9a5c", "file_2_name": "small_jpg.jpg", "file_2_md5": "2c39ce6536da5891e3766005438d3b47", "extra_data_field": "ttt"}]}
```



#### Send Email StartTLS Test
Send email message. Requires: SMTP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recipients|Arbitrary comma separated list of email addresses for the email recipients|True|String||
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email|False|String||
|BCC|BCC email address. Multiple addresses can be separated by commas|False|String||
|Subject|The email subject part|True|String||
|Content|The email body part, if Email HTML Template is set, action should support definition of body of the email with provided HTML template.|True|Email Content||
|Return message id for the sent email|If selected, action returns the message id for the sent email in JSON technical result. This message id when can be used for the 'Wait for Email from user' action to process user response|False|Boolean||
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email.|False|String||



##### JSON Results
```json
{"date": "2019-11-18 08:02:57.984000+00:00", "message_id": "<157406417676.181148.9624253160139989862@C3431448806>", "recipients": "aaa@aaa.com, bbb@bbb.com"}
```



#### Ping
Test Connectivity. Requires: IMAP or SMTP configuration
Timeout - 600 Seconds



#### Search Email
Search email messages. Requires: IMAP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders.|True|String|None|
|Subject Filter|Filter condition, specify what subject to search for emails|False|String|None|
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String|None|
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String|None|
|Time frame (minutes)|Filter condition, specify in what time frame in minutes should search look for emails|True|String|None|
|Only Unread|Filter condition, specify if search should look only for unread emails|False|Boolean|None|
|Max Emails To Return|Return max X emails as an action result.|True|String|None|



##### JSON Results
```json
{"emails":[{"name": "aaa@aaa.com_1574937477000", "message_id": "<CAHNaB8eum4Tc=fj4U-n42zJNf6hgN6jop+KqG+WC3eGret_ZmA@mail.gmail.com>", "email_uid": 14, "subject": "Test 35", "StartTime": 1574937477000, "EndTime": 1574937477000, "Environment": "Undefined", "body": "Test with attachment", "html_body": "<div>Test with attachment</div>", "text_body": "Test with attachment", "device_product": "Mail", "vendor": "Mail", "event_type": "Mailbox Alert", "from": "uuu@uuu.com", "to": "hhh@hhh.com", "managerReceiptTime": 1574937477000, "original_message": "", "reply_to": "", "answer": "", "url_1": "https://siemplify.co", "url_2": "github.com", "file_1_name": "Test email as MSG.zip", "file_1_md5": "fc0118857de51b68c6c38c71566d9a5c", "file_2_name": "small_jpg.jpg", "file_2_md5": "2c39ce6536da5891e3766005438d3b47", "extra_data_field": "ttt"}, {"name": "aaa@aaa.com_1574937477000", "message_id": "<CAHNaB8eum4Tc=fj4U-n42zJNf6hgN6jop+KqG+WC3eGret_ZmA@mail.gmail.com>", "email_uid": 14, "subject": "Test 35", "StartTime": 1574937477000, "EndTime": 1574937477000, "Environment": "Undefined", "body": "Test with attachment", "html_body": "<div>Test with attachment</div>", "text_body": "Test with attachment", "device_product": "Mail", "vendor": "Mail", "event_type": "Mailbox Alert", "from": "uuu@uuu.com", "to": "hhh@hhh.com", "managerReceiptTime": 1574937477000, "original_message": "", "reply_to": "", "answer": "", "url_1": "https://siemplify.co", "url_2": "github.com", "file_1_name": "Test email as MSG.zip", "file_1_md5": "fc0118857de51b68c6c38c71566d9a5c", "file_2_name": "small_jpg.jpg", "file_2_md5": "2c39ce6536da5891e3766005438d3b47", "extra_data_field": "ttt"}]}
```



#### Send Email
Send email message. Requires: SMTP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recipients|Arbitrary comma separated list of email addresses for the email recipients|True|String|None|
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email|False|String|None|
|BCC|BCC email address. Multiple addresses can be separated by commas|False|String|None|
|Subject|The email subject part|True|String|None|
|Content|The email body part, if Email HTML Template is set, action should support definition of body of the email with provided HTML template.|True|Email Content||
|Return message id for the sent email|If selected, action returns the message id for the sent email in JSON technical result. This message id when can be used for the 'Wait for Email from user' action to process user response|False|Boolean|None|
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email.|False|String|None|



##### JSON Results
```json
{"date": "2019-11-18 08:02:57.984000+00:00", "message_id": "<157406417676.181148.9624253160139989862@C3431448806>", "recipients": "aaa@aaa.com, bbb@bbb.com"}
```



#### DEBUG - Wait for Email from User
Wait for user's response based on an email sent via Send Email action. Note: This is a Siemplify async action, if required, please adjust the async timeout for action (polling timeout) and global action timeout as needed. Action input parameter “Wait stage timeout (minutes)“ cant be larger than global timeout. Note: Please make sure to set IDE timeout as well, as the IDE timeout will override the action’s timeout if the IDE timeout will be shorter. Requires: IMAP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Email Recipients|Comma-separated list of recipient emails, response from which current action would be waiting for. If message has been sent using Send Email action, please select Select SendEmail.JSONResult.recipients field as a placeholder.|True|String||
|Wait stage timeout (minutes)|How long in minutes to wait for the user’s reply before marking it timed out.|True|String|1440|
|Wait for all recipients to reply?|Parameter can be used to define if there are multiple recipients - should the Action wait for responses from all of recipients until timeout, or Action should wait for first reply to proceed.|False|Boolean|True|
|Wait stage exclude pattern|Regular expression to exclude specific replies from the wait stage. Works with body part of email. Example is, to exclude automatic Out-Of-Office emails to be considered as recipient reply, and instead wait for actual user reply|False|String||
|Folder to check for reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|False|String|Inbox|
|Fetch Response Attachments|If selected, if recipient replies with attachment – fetch recipient response and add it as attachment for the action result.|False|Boolean|False|
|Email Message_id|Message_id of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult.message_id field as a placeholder.|True|String||
|Email Date|Send timestamp of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult.email_date field as a placeholder.|True|String||



##### JSON Results
```json
{"Responses": [{"recipient": "aaa@aaa.com", "content": "It's approved, John!"}, {"recipient": "xxx@xxx.com", "content": "I approve going forward on this"}]}
```



#### Wait for Email from User
Wait for user's response based on an email sent via Send Email action. Note: This is a Siemplify async action, if required, please adjust the async timeout for action (polling timeout) and global action timeout as needed. Action input parameter “Wait stage timeout (minutes)“ cant be larger than global timeout. Note: Please make sure to set IDE timeout as well, as the IDE timeout will override the action’s timeout if the IDE timeout will be shorter. Requires: IMAP configuration
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Email Message_id|Message_id of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult.message_id field as a placeholder.|True|String|None|
|Email Date|Send timestamp of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult.email_date field as a placeholder.|True|String|None|
|Email Recipients|Comma-separated list of recipient emails, response from which current action would be waiting for. If message has been sent using Send Email action, please select Select SendEmail.JSONResult.recipients field as a placeholder.|True|String|None|
|Wait stage timeout (minutes)|How long in minutes to wait for the user’s reply before marking it timed out.|True|String|None|
|Wait for all recipients to reply?|Parameter can be used to define if there are multiple recipients - should the Action wait for responses from all of recipients until timeout, or Action should wait for first reply to proceed.|False|Boolean|None|
|Wait stage exclude pattern|Regular expression to exclude specific replies from the wait stage. Works with body part of email. Example is, to exclude automatic Out-Of-Office emails to be considered as recipient reply, and instead wait for actual user reply|False|String|None|
|Folder to check for reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|False|String|None|
|Fetch Response Attachments|If selected, if recipient replies with attachment – fetch recipient response and add it as attachment for the action result.|False|Boolean|None|



##### JSON Results
```json
{"Responses": [{"recipient": "aaa@aaa.com", "content": "It's approved, John!"}, {"recipient": "xxx@xxx.com", "content": "I approve going forward on this"}]}
```









## Connectors
#### Copy of Generic IMAP Email Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Additional headers to extract from emails|Specify additional headers to search and extract from processed emails. Found headers will be added to the email’s Siemplify event. Parameter accepts multiple values as a comma separated string, provided values can be set as an exact match or as a regex, for example, Received:, (Test).*|False|String||
|Attached Mail File Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String||
|Attach Original EML|If checked, attach the original message as eml file.|False|Boolean|false|
|Create a Separate Siemplify Alert per Attached Mail File?|if enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|
|DeviceProductField|The value to use as the device product|True|String|Mail|
|Environment Field Name|If defined - connector will extract the environment from the specified event field. You can manipulate the field data using the Regex pattern field to extract specific string. In case the the extracted environment field and Siemplify environment name are not equal - you can map them in the map.json that is auto-generated on the first run, inside the <run-folder>.<run-folder> = C:\Siemplify_Server\Scripting\SiemplifyConnectorExecution<Connector_Folder>|False|Integer||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "envirnment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|String||
|EventClassId|The field name used to determine the event name (sub-type)|False|String|event_name_mail_type|
|Exclusion Body Regex|Exclude emails for which body matches specified regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Exclusion Subject Regex|Exclude emails for which subject matches specified. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|True|String|Inbox|
|IMAP Port|Imap port. e.g. 993|True|Integer|993|
|IMAP Server Address|e.g. imap.gmail.com|True|String|imap.gmail.com|
|IMAP USE SSL|Indicates whether to use ssl on connection or not.|False|Boolean|true|
|Mark Emails as Read|If checked, mark mails as read after pulling them|False|Boolean|true|
|Max Emails Per Cycle|Max count of mails to pull in one cycle|True|String|10|
|Offset Time In Days|Max number of days to fetch mails since. e.g. 3|True|String|5|
|Original Received Mail Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String||
|Password|IMAP Password|True|Password|India@123@|
|Proxy Password|The proxy password to authenticate with.|False|Password||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|Server Time Zone|The timezone configured in the server, examples (1. UTC, 2. Asia/Jerusalem)|False|String|UTC|
|Unread Emails Only|If checked, pull only unread mails|False|Boolean|true|
|Username|IMAP Username|True|String||


##### Whitelist
| |
|-|
|subject: (?<=Subject: ).*|
|to: (?m)(?<=^To: ).*|


#### Generic IMAP Email Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The value to use as the device product|True|String|Mail|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|event_name_mail_type|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|IMAP Server Address|e.g. imap.gmail.com|True|String||
|IMAP Port|Imap port. e.g. 993|True|Integer||
|Username|IMAP Username|True|String||
|Password|IMAP Password|True|Password||
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|True|String|Inbox|
|Server Time Zone|The timezone configured in the server, examples (1. UTC, 2. Asia/Jerusalem)|False|String|UTC|
|Environment Field Name|If defined - connector will extract the environment from the specified event field. You can manipulate the field data using the Regex pattern field to extract specific string. In case the the extracted environment field and Siemplify environment name are not equal - you can map them in the map.json that is auto-generated on the first run, inside the <run-folder>.<run-folder> = C:\Siemplify_Server\Scripting\SiemplifyConnectorExecution<Connector_Folder>|False|Integer||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "envirnment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|String||
|IMAP USE SSL|Indicates whether to use ssl on connection or not.|False|Boolean|true|
|Unread Emails Only|If checked, pull only unread mails|False|Boolean|true|
|Mark Emails as Read|If checked, mark mails as read after pulling them|False|Boolean|true|
|Attach Original EML|If checked, attach the original message as eml file.|False|Boolean|false|
|Offset Time In Days|Max number of days to fetch mails since. e.g. 3|True|String|5|
|Max Emails Per Cycle|Max count of mails to pull in one cycle|True|String|10|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||
|Additional headers to extract from emails|Specify additional headers to search and extract from processed emails. Found headers will be added to the email’s Siemplify event. Parameter accepts multiple values as a comma separated string, provided values can be set as an exact match or as a regex, for example, Received:, (Test).*|False|String||
|Exclusion Subject Regex|Exclude emails for which subject matches specified. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Exclusion Body Regex|Exclude emails for which body matches specified regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Original Received Mail Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String|orig|
|Attached Mail File Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String|attach|
|Create a Separate Siemplify Alert per Attached Mail File?|if enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|


##### Whitelist
| |
|-|
|subject: (?<=Subject: ).*|
|to: (?m)(?<=^To: ).*|


#### KM padding Generic IMAP Email Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Additional headers to extract from emails|Specify additional headers to search and extract from processed emails. Found headers will be added to the email’s Siemplify event. Parameter accepts multiple values as a comma separated string, provided values can be set as an exact match or as a regex, for example, Received:, (Test).*|False|String||
|Attached Mail File Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String|attach|
|Attach Original EML|If checked, attach the original message as eml file.|False|Boolean|false|
|Create a Separate Siemplify Alert per Attached Mail File?|if enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|
|DeviceProductField|The value to use as the device product|True|String|Mail|
|Environment Field Name|If defined - connector will extract the environment from the specified event field. You can manipulate the field data using the Regex pattern field to extract specific string. In case the the extracted environment field and Siemplify environment name are not equal - you can map them in the map.json that is auto-generated on the first run, inside the <run-folder>.<run-folder> = C:\Siemplify_Server\Scripting\SiemplifyConnectorExecution<Connector_Folder>|False|Integer||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "envirnment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|String||
|EventClassId|The field name used to determine the event name (sub-type)|False|String|event_name_mail_type|
|Exclusion Body Regex|Exclude emails for which body matches specified regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Exclusion Subject Regex|Exclude emails for which subject matches specified. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|True|String|Inbox|
|IMAP Port|Imap port. e.g. 993|True|Integer||
|IMAP Server Address|e.g. imap.gmail.com|True|String||
|IMAP USE SSL|Indicates whether to use ssl on connection or not.|False|Boolean|true|
|Mark Emails as Read|If checked, mark mails as read after pulling them|False|Boolean|true|
|Max Emails Per Cycle|Max count of mails to pull in one cycle|True|String|10|
|Offset Time In Days|Max number of days to fetch mails since. e.g. 3|True|String|5|
|Original Received Mail Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String|orig|
|Password|IMAP Password|True|Password||
|Proxy Password|The proxy password to authenticate with.|False|Password||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|Server Time Zone|The timezone configured in the server, examples (1. UTC, 2. Asia/Jerusalem)|False|String|UTC|
|Unread Emails Only|If checked, pull only unread mails|False|Boolean|true|
|Username|IMAP Username|True|String||


##### Whitelist
| |
|-|
|subject: (?<=Subject: ).*|
|to: (?m)(?<=^To: ).*|




