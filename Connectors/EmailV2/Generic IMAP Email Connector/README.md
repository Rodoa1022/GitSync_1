# Generic IMAP Email Connector



Integration: EmailV2

Integration Version: 32.0

Device Product Field: Mail

Event Name Field: event_name_mail_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|True|Inbox|
|Server Time Zone|The timezone configured in the server, examples (1. UTC, 2. Asia/Jerusalem)|False|UTC|
|Environment Field Name|If defined - connector will extract the environment from the specified event field. You can manipulate the field data using the Regex pattern field to extract specific string. In case the the extracted environment field and Siemplify environment name are not equal - you can map them in the map.json that is auto-generated on the first run, inside the <run-folder>.<run-folder> = C:\Siemplify_Server\Scripting\SiemplifyConnectorExecution<Connector_Folder>|False||
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|60|
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "envirnment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False||
|IMAP USE SSL|Indicates whether to use ssl on connection or not.|False|true|
|Unread Emails Only|If checked, pull only unread mails|False|true|
|Mark Emails as Read|If checked, mark mails as read after pulling them|False|false|
|Attach Original EML|If checked, attach the original message as eml file.|False|true|
|Offset Time In Days|Max number of days to fetch mails since. e.g. 3|True|1|
|Max Emails Per Cycle|Max count of mails to pull in one cycle|True|10|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Exclusion Body Regex|Exclude emails for which body matches specified regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False||
|Original Received Mail Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|orig|
|Attached Mail File Prefix|Prefix to add to the extracted keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|attach|
|Create a Separate Siemplify Alert per Attached Mail File?|if enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|true|
|IMAP Server Address|e.g. imap.gmail.com|True|imap.gmail.com|
|IMAP Port|Imap port. e.g. 993|True|993|
|Username|IMAP Username|True|siemplifytesting.rodgonzalez@gmail.com|
|Password|IMAP Password|True|***************|
|Proxy Password|The proxy password to authenticate with.|False||
|Additional headers to extract from emails|Specify additional headers to search and extract from processed emails. Found headers will be added to the email’s Siemplify event. Parameter accepts multiple values as a comma separated string, provided values can be set as an exact match or as a regex, for example, Received:, (Test).*|False||
|Exclusion Subject Regex|Exclude emails for which subject matches specified. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False||

