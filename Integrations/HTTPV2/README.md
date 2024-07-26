
# HTTPV2

HTTP V2 integration was designed for you to build your own integrations, actions without the need of writing any code.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Test URL|Test URL that can be used to valid the "Basic Auth" authentication or "API Key" authentication.|False|String||
|Basic Auth Username|If you provide "Basic Auth Username" and "Basic Auth Password" parameters then these parameters will be added as Basic Authentication headers to every action run. Note: you need to provide both "Basic Auth Password" and "Basic Auth Username".|False|String||
|Basic Auth Password|If you provide "Basic Auth Username" and "Basic Auth Password" parameters then these parameters will be added as Basic Authentication headers to every action run. Note: you need to provide both "Basic Auth Password”" and "Basic Auth Username".|False|Password|None|
|API Key Field Name|Name of the header that will contain the API key. If you provide "API Key Field Name" and "API Key Secret" parameters then these parameters will be added to every action run. Note: you need to provide both "API Key Field Name" and "API Key Secret".|False|String||
|API Key Secret|API key secret. If you provide "API Key Field Name" and "API Key Secret" parameters then these parameters will be added to every action run. Note: you need to provide both "API Key Field Name" and "API Key Secret".|False|Password|None|
|Dedicated Auth API Request Method|Method that will be used in the Dedicated Auth API flow to generate the access token.|False|String|Post|
|Dedicated Auth API Request URL|API request that will be used in the Dedicated Auth API flow to generate the access token.|False|String||
|Dedicated Auth API Request Headers|Headers that will be used in the Dedicated Auth API flow to generate the access token.|False|Password|None|
|Dedicated Auth API Request Body|Request Body that will be used in the Dedicated Auth API flow to generate the access token.|False|Password|None|
|Dedicated Auth API Request Token Field Name|Name of the field that contains the generated access token. This access token can be used inside the actions with {{integration.token}} placeholder. Note: that the response for token generation will be flattened with "_" as delimiter.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for all of the connections done by integration.|False|Boolean|true|
|CA Certificate|CA certificate to use to validate the secure connection. Parameter accepts the CA certificate in a form of base64 encoded string.|False|String||


#### Dependencies
| |
|-|
|cross/pyzipper-0.3.6-py2.py3-none-any.whl|
|cross/idna-3.3-py3-none-any.whl|
|cross/google_auth-2.5.0-py2.py3-none-any.whl|
|cross/pycryptodomex-3.20.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cross/chardet-3.0.4-py2.py3-none-any.whl|
|cross/pyparsing-3.0.7-py3-none-any.whl|
|cross/google_api_core-2.4.0-py2.py3-none-any.whl|
|cross/cachetools-5.0.0-py3-none-any.whl|
|cross/pyasn1-0.4.8-py2.py3-none-any.whl|
|cross/setuptools-60.6.0-py3-none-any.whl|
|cross/httplib2-0.20.2-py3-none-any.whl|
|cross/beautifulsoup4-4.9.1-py3-none-any.whl|
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
|cross/certifi-2023.11.17-py3-none-any.whl|
|cross/EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|cross/six-1.16.0-py2.py3-none-any.whl|
|cross/charset_normalizer-2.0.11-py3-none-any.whl|
|cross/TIPCommon-1.1.7.2-py2.py3-none-any.whl|


## Actions
#### Ping
Test connectivity.
Timeout - 600 Seconds



##### JSON Results
```json
{"endpoint": "https://testendpoint.com"}
```



#### Execute HTTP Request
Execute HTTP request.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Method|Specify the method for the request.|True|List|GET|
|URL Path|Specify the URL that needs to be executed.|True|String|https://|
|URL Params|Specify the parameters for the URL. Any value provided in this parameter will be used alongside the values that are directly provided in the URL path parameters.|False|String|{"URL Field Name": "URL Field Value"}|
|Headers|Specify headers for the HTTP request.|False|String|{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json", "User-Agent" : "GoogleSecOps"}|
|Cookie|Specify the parameters that should be constructed into the "Cookie" header. This parameter will overwrite the cookie provided in the "Headers" parameter.|False|String|{"Cookie_1": "value_1"}|
|Body Payload|Specify body for the HTTP request.|False|String|{"Body Field Name": "Body Field Value"}|
|Expected Response Values|Specify the expected response values. If this parameter is not empty, then action will work in ASYNC mode and action will execute until the expected values will be seen or until timeout.|False|String||
|Follow Redirects|If enabled, action will follow the redirects.|False|Boolean|true|
|Fail on 4xx/5xx|If enabled, action will fail, if the status code of the response is 4xx or 5xx.|False|Boolean|true|
|Base64 Output|If enabled, action will convert the response to base64. This is useful when downloading files. Note: JSON result can't be bigger than 15 mb.|False|Boolean|false|
|Fields To Return|Specify what fields to return. Possible values: response_data, redirects, response_code,response_cookies,response_headers,apparent_encoding|True|String|response_data, redirects, response_code,response_cookies,response_headers,apparent_encoding|
|Request Timeout|How long to wait for the server to send data before giving up|True|String|120|
|Save To Case Wall|If enabled, action will save the file and attach it to the case wall. Note: the file will be archived with ".zip" extension. This zip will not be password protected.|False|Boolean|false|
|Password Protect Zip|If enabled, action will add an "infected" password to the zip created with "Save To Case Wall" parameter. Use this, when you are dealing with suspicious files.|False|Boolean|true|



##### JSON Results
```json
{"response_data": null, "redirects": ["http://testurl.com/"], "response_code": 200, "response_cookies": {}, "response_headers": {}, "apparent_encoding": "ascii"}
```






## Jobs



## Connectors


