
# GoogleBigQuery

BigQuery is a fully-managed, serverless data warehouse that enables scalable analysis over petabytes of data. It is a Software as a Service that supports querying using ANSI SQL. It also has built-in machine learning capabilities.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Account Type|Type of the Google BigQuery account. Located at the “type” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|service_account|
|Project ID|Project ID of the Google BigQuery account. Located at the “project_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Private Key ID|Private Key ID of the Google BigQuery account. Located at the “private_key_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|Password|None|
|Private Key|Private Key of the Google BigQuery account. Located at the “private_key” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|Password|None|
|Client Email|Client Email of the Google BigQuery account. Located at the “client_email” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Client ID|Client ID of the Google BigQuery account. Located at the “client_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Auth URI|Auth URI of the Google BigQuery account. Located at the “auth_uri” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://accounts.google.com/o/oauth2/auth|
|Token URI|Token URI of the Google BigQuery account. Located at the “token_uri” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://oauth2.googleapis.com/token|
|Auth Provider X509 URL|Auth Provider X509 URL of the Google BigQuery account. Located at the “auth_provider_x509_cert_url” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://www.googleapis.com/oauth2/v1/certs|
|Client X509 URL|Client X509 URL of the Google BigQuery account. Located at the “client_x509_cert_url” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Service Account Json File Content|Optional: Instead of specifying private key id, private key and other parameters, specify here the full JSON content of the service account file. Other connection parameters will be ignored if this parameter is provided.|False|Password|None|
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|String||
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the “Service Usage Consumer” IAM role to your Google Cloud service account.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Big Query service is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|cross/protobuf-4.24.4-cp37-abi3-manylinux2014_x86_64.whl|
|cross/pytz-2024.1-py2.py3-none-any.whl|
|cross/googleapis_common_protos-1.63.0-py2.py3-none-any.whl|
|cross/packaging-24.0-py3-none-any.whl|
|cross/pycparser-2.21-py2.py3-none-any.whl|
|cross/pandas-1.3.5-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cross/typing_extensions-4.7.1-py3-none-any.whl|
|cross/numpy-1.21.6-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl|
|cross/rsa-4.9-py3-none-any.whl|
|cross/grpcio-1.62.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cross/pyasn1-0.5.1-py2.py3-none-any.whl|
|cross/cachetools-5.3.3-py3-none-any.whl|
|cross/pyparsing-3.1.2-py3-none-any.whl|
|cross/grpcio_status-1.62.2-py3-none-any.whl|
|cross/python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cross/google_auth-2.29.0-py2.py3-none-any.whl|
|cross/importlib_metadata-6.7.0-py3-none-any.whl|
|cross/TIPCommon-1.1.8.4-py2.py3-none-any.whl|
|cross/cffi-1.15.0.tar.gz|
|cross/google_api_core-2.19.0-py3-none-any.whl|
|cross/proto_plus-1.23.0-py3-none-any.whl|
|cross/google_cloud_bigquery-3.21.0-py2.py3-none-any.whl|
|cross/db_dtypes-1.2.0-py2.py3-none-any.whl|
|cross/zipp-3.15.0-py3-none-any.whl|
|cross/certifi-2024.2.2-py3-none-any.whl|
|cross/google_resumable_media-2.7.0-py2.py3-none-any.whl|
|cross/pyarrow-12.0.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cross/uritemplate-4.1.1-py2.py3-none-any.whl|
|cross/google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|cross/charset_normalizer-3.3.2-py3-none-any.whl|
|cross/google_cloud_core-2.4.1-py2.py3-none-any.whl|
|cross/idna-3.7-py3-none-any.whl|
|cross/six-1.16.0-py2.py3-none-any.whl|
|cross/requests-2.31.0-py3-none-any.whl|
|cross/urllib3-2.0.7-py3-none-any.whl|
|cross/pyasn1_modules-0.3.0-py2.py3-none-any.whl|
|cross/google_crc32c-1.5.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cross/google_api_python_client-2.127.0-py2.py3-none-any.whl|
|cross/httplib2-0.22.0-py3-none-any.whl|
|cross/pycryptodome-3.20.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Ping
Test connectivity to the Google BigQuery with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Run SQL Query
Execute queries in Google BigQuery.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Dataset Name|Specify the name of the dataset, which will be used, when executing queries.|True|String||
|Query|Specify the SQL query that needs to be executed.|True|String||
|Max Results To Return|Specify how many results to return in the response.|False|String|50|



##### JSON Results
```json
[{"Airport_Code": "MDW", "Airport_Name": "Chicago, IL: Chicago Midway International", "Time_Label": "2015/05", "Time_Month": 5, "Time_Month_Name": "May", "Time_Year": 2015, "Statistics___of_Delays_Carrier": 351, "Statistics___of_Delays_Late_Aircraft": 546, "Statistics___of_Delays_National_Aviation_System": 292, "Statistics___of_Delays_Security": 2, "Statistics___of_Delays_Weather": 100, "Statistics_Carriers_Names": "Delta Air Lines Inc.,ExpressJet Airlines Inc.,Southwest Airlines Co.", "Statistics_Carriers_Total": 3, "Statistics_Flights_Cancelled": 88, "Statistics_Flights_Delayed": 1289, "Statistics_Flights_Diverted": 32, "Statistics_Flights_On_Time": 6182, "Statistics_Flights_Total": 7591, "Statistics_Minutes_Delayed_Carrier": 19332, "Statistics_Minutes_Delayed_Late_Aircraft": 34376, "Statistics_Minutes_Delayed_National_Aviation_System": 12346, "Statistics_Minutes_Delayed_Security": 48, "Statistics_Minutes_Delayed_Total": 76163, "Statistics_Minutes_Delayed_Weather": 10061}]
```






## Jobs



## Connectors


