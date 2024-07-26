
# Functions

A set of math and data manipulation actions created for Google SecOps Community to power up playbook capabilities.

Python Version - 2


#### Dependencies
| |
|-|
|tldextract-2.2.3-py2.py3-none-any.whl|
|chardet-3.0.4-py2.py3-none-any.whl|
|idna-2.10-py2.py3-none-any.whl|
|pytz-2021.1-py2.py3-none-any.whl|
|idna-3.4-py3-none-any.whl|
|requests_file-1.5.1-py2.py3-none-any.whl|
|packaging-21.0-py3-none-any.whl|
|typing_extensions-4.7.1-py3-none-any.whl|
|webencodings-0.5.1-py2.py3-none-any.whl|
|urllib3-1.25.10-py2.py3-none-any.whl|
|tld-0.13-py2.py3-none-any.whl|
|urlextract-1.8.0-py3-none-any.whl|
|decorator-4.4.2-py2.py3-none-any.whl|
|jsonpath_ng-1.5.2-py3-none-any.whl|
|hashID-3.1.4-py2.py3-none-any.whl|
|platformdirs-3.10.0-py3-none-any.whl|
|setuptools-50.3.0-py3-none-any.whl|
|certifi-2020.6.20-py2.py3-none-any.whl|
|bleach-3.3.0-py2.py3-none-any.whl|
|ply-3.11-py2.py3-none-any.whl|
|pyparsing-2.4.7-py2.py3-none-any.whl|
|Pillow-8.2.0-cp37-cp37m-manylinux1_x86_64.whl|
|requests-2.24.0-py2.py3-none-any.whl|
|six-1.15.0-py2.py3-none-any.whl|
|uritools-4.0.2-py3-none-any.whl|
|filelock-3.12.2-py3-none-any.whl|
|xmltodict-0.13.0-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|


## Actions
#### Time Duration Calculator
The Time Duration Calculator will calculate the time that has elapsed/difference between two dates with time.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input DateTime 1|The first input datetime value.  Supports either strftime format or "now" for the current time.|True|String||
|Input DateTime 1 Format|The strftime format of the DateTime string.https://strftime.org/|True|String|%Y-%m-%dT%H:%M:%S%z|
|Input DateTime 2|The second input datetime value.  Supports either strftime format or "now" for the current time.|True|String|now|
|Input DateTime 2 Format|The strftime format of Input DateTime 2.|True|String|%Y-%m-%dT%H:%M:%S%z|



##### JSON Results
```json
{}
```



#### SanitizeHTML
Given a fragment of HTML, SantizeHTML will parse it according to the HTML5 parsing algorithm and sanitize any disallowed tags or attributes. This algorithm also takes care of things like unclosed and (some) misnested tags.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Tags|Tags is the allowed set of HTML tags. Comma separated list. HTML tags not in this list will be escaped or stripped. |False|String|a,abbr,acronym,b,blockquote,code,em,i,li,ol,strong,ul,table,tr,td,th,h1,h2,h3,body,tbody,thead,div,footer,head,header,html,img,option,p,section,span,strong,svg|
|Attributes|Attributes lets you specify which attributes are allowed. Value should be a comma separated list.Default  {'a': ['href', 'title'], 'abbr': ['title'],|False|String|None|
|Styles|If you allow the style attribute, specify the allowed styles set, for example color and background-color. Value should be comma separated list.|False|String|None|
|Allow All Attributes|Set to True to allow all attributes.|False|Boolean|false|
|Input HTML|The HTML fragment that will be sanitized.|True|String||



##### JSON Results
```json
{}
```



#### Run JSONPath Query
The action runs an JSONPath Query on a given json and extracts values according to the expression.
View https://github.com/h2non/jsonpath-ng for more information on JSONPath
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Json|Json input|True|Code|None|
|JSONPath Expression|JSONPath expressions always refers to a JSON structure in the same way as XPath expressions are used in combination with an XML document.|True|String|None|



##### JSON Results
```json
{}
```



#### Ping
Check connectivity
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Convert Time Format
Convert a datetime value from one format to another format.  
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input|The input datetime value that will be converted.|True|String|<input val>|
|From Format|The datetime format the input string is in.  https://strftime.org/|True|String|X|
|To Format|The desired time format of the output.  Use Arrow time format.  https://arrow.readthedocs.io/en/stable/#supported-tokens|True|String|YYYY/MM/DD|
|Time Delta In Seconds|Shift parameter that allows to change the output actual time to either the future (positive) or past (negative). This shift is measured in seconds|True|String|0|
|Timezone|Output timezone|False|String||



##### JSON Results
```json
{}
```



#### Detect IP Type
This action checks if an IP is an IPv4 address or IPv6 address.  IP Address entities will be enriched with IPType field.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Addresses|Comma-separated|False|String||



##### JSON Results
```json
[{"Address": "2.2.2.2", "IPType": "IPV4"}, {"Address": "2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF", "IPType": "IPV6"}, {"IPType": "IPV4", "Address": "1.1.1.1"}]
```



#### XMLtoJson
Convert XML formatted data to JSON.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|xml|Convert XML to JSON|True|String|<e> <a>text</a> <a>text</a> </e>|



##### JSON Results
```json
{}
```



#### Math Functions
A set of built-in Python functions - 
Abs - returns the absolute value of a number
Float - returns a floating point number
Display - converts the number to include commas where needed
Hex - converts a number into a hexadecimal value
Int - returns an integer number
Max - returns the largest item in an iterable 
Min - returns the smallest item in an iterable
Round - rounds a number
Sort - returns a sorted number
Sum - sums the items of an iterator
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Function|Select the Math Function you would like to run on the number|True|List|Max|
|Numbers|The numbers you would like to run the Math function on.|True|String|13.5,-90,566,11.32|



##### JSON Results
```json
{}
```



#### Extract IOCs
Extract domains, IP addresses, URLs and Emails from a string.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input String|The string to extract the IP addresses from.|True|String|<input string>|



##### JSON Results
```json
{"domains":["google.com"],"ips":["10.10.1.1"],"urls":["www.google.com"],"emails":["user@user.com"]}
```



#### String Functions
This action includes basic Pythonic string functions as mentioned below - 
Lower: Converts the input string to lowercase.
Upper: Converts the input string to uppercase (duplicated case in the script).
Strip: Removes leading and trailing whitespaces from the input string.
Title: Converts the first character of each word in the input string to uppercase.
Count: Counts the occurrences of `param_1` in the input string.
Replace: Replaces occurrences of `param_1` with `param_2` in the input string.
Find: Finds the first occurrence of `param_1` in the input string and returns its index.
IsAlpha: Checks if all characters in the input string are alphanumeric.
IsDigit: Checks if all characters in the input string are digits.
Regex Replace: Performs a regex-based replacement of `param_1` with `param_2` in the input string.
JSON Serialize: Converts the input string to a JSON formatted string.
Regex: Finds all occurrences of the pattern `param_1` in the input string, joins them using `param_2` (defaulting to ", "), and returns the result.
DecodeBase64: Decodes the input string from base64 using `param_1` as the encoding type. Default to utf-8
EncodeBase64: Encodes the input string in base64 using `param_1` as the encoding type. Default to utf-8
RemoveNewLines: Removes new lines from the input string, replacing them with spaces.
Split: Splits the input string using `param_1` (or "," if not provided) and adds the result to the Siemplify result.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Param 2|The second parameter (this is an optional parameter as some functions require only 1 param)|False|String| |
|Param 1|The first parameter (this is an optional parameter as some functions require only 1 param)|False|String|None|
|Input|The input for the current fuction|True|String|Example|
|Function|Select the function you would like to run from the list|True|List|Lower|



##### JSON Results
```json
{}
```



#### Detect Hash Type
This action detects the most likely hash type of entities. Supported types are SHA256, MD5, SHA1, SHA-512.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hashes|One or more hashes that are comma separated. |False|String||



##### JSON Results
```json
[  
  {  
    "Hash": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F",  
    "HashType": "SHA-256"  
  },  
  {  
    "Hash": "202cb962ac59075b964b07152d234b70",  
    "HashType": "MD5"  
  }  
]
```



#### Math Arithmetic
A set of built in math operators:
Plus - returns a result for the sum of 2 arguments
Sub - returns a result for 1 argument minus the other
Multi - returns a result for 1 argument multiplied by the other
Div - returns a result for 1 argument divided by the other
Mod - returns the result of the percentage between 2 arguments
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Function|The function you would like to run on 2 given arguments |True|List|Plus|
|Arg 2|The second argument |True|String|{}|
|Arg 1|The first argument|True|String|{}|



##### JSON Results
```json
{}
```



#### IP to Integer
Converts an IP address or list of IP addresses to integers or longs.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Addresses|Comma separated list of IP addresses to be converted into integers.|True|String||



##### JSON Results
```json
{}
```



#### Create Thumbnail
Creates a Base64 Thumbnail of an image.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 Image|The Base64 string of the image.|False|String||
|Thumbnail Size|Comma separated.  Pixels.   X , Y|True|String|250,250|
|Input JSON|Input JSON|False|String||
|Image Key Path|If using Input JSON, the keypath for the image field.|False|String||



##### JSON Results
```json
{}
```






## Jobs



## Connectors


