
# Lists

A set of tools to facilitate managing custom lists within Google SecOps.

Python Version - 2


#### Dependencies
| |
|-|
|tldextract-2.2.3-py2.py3-none-any.whl|
|chardet-3.0.4-py2.py3-none-any.whl|
|idna-2.10-py2.py3-none-any.whl|
|requests_file-1.5.1-py2.py3-none-any.whl|
|urllib3-1.25.10-py2.py3-none-any.whl|
|setuptools-50.3.0-py3-none-any.whl|
|requests-2.24.0-py2.py3-none-any.whl|
|six-1.15.0-py2.py3-none-any.whl|
|certifi-2023.11.17-py3-none-any.whl|


## Actions
#### Is String In Custom List
The action checks if a specific string exists in a custom list
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IdentifierList|A list of "strings" to compare against the custom list (for the current environment) in a specific category |True|String|1.2.3.4,google.com,yahoo.co.uk|
|Category|Custom list Category|True|String|WhiteList|



##### JSON Results
```json
[  
    {  
        "Entity": "1.2.3.4",  
        "EntityResult": false  
    },  
    {  
        "Entity": "google.com",  
        "EntityResult": true  
    },  
    {  
        "Entity": "yahoo.co.uk",  
        "EntityResult": false  
    }  
]
```



#### Add String to Custom List
The action adds a string to a custom list.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|ListItem|The list item string to add to the custom list.|True|String|cajs3i|
|Category|Custom list Category|True|String|WhiteList|



##### JSON Results
```json
[  
    {  
        "Entity": "1.2.3.4",  
        "EntityResult": false  
    },  
    {  
        "Entity": "google.com",  
        "EntityResult": true  
    },  
    {  
        "Entity": "yahoo.co.uk",  
        "EntityResult": false  
    }  
]
```



#### Search Custom Lists
Search a specified string within the records of a custom list. (If no values are provided will return all custom lists records)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|String to Search|String to search within list values|False|String||
|Categories|Comma separated values|False|String||



##### JSON Results
```json
[{"entityIdentifier": "192.168.0.1", "category": "vuln_scanner", "forDBMigration": false, "environments": ["Default Environment"], "id": 5, "creationTimeUnixTimeInMs": 1673953571935, "modificationTimeUnixTimeInMs": 1673953571935}, {"entityIdentifier": "192.168.0.2", "category": "vuln_scanner", "forDBMigration": false, "environments": ["Default Environment"], "id": 6, "creationTimeUnixTimeInMs": 1673953584305, "modificationTimeUnixTimeInMs": 1673953584305}]
```



#### Ping
Check connectivity
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Search Environment Custom Lists
Search a specified string within the records of an environment's custom list. (If no values are provided will return all custom lists records)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|String to Search|String to search within list values|False|String||
|Categories|Comma separated values|False|String||



##### JSON Results
```json
[{"entityIdentifier": "192.168.0.1", "category": "vuln_scanner", "forDBMigration": false, "environments": ["Default Environment"], "id": 5, "creationTimeUnixTimeInMs": 1673953571935, "modificationTimeUnixTimeInMs": 1673953571935}, {"entityIdentifier": "192.168.0.2", "category": "vuln_scanner", "forDBMigration": false, "environments": ["Default Environment"], "id": 6, "creationTimeUnixTimeInMs": 1673953584305, "modificationTimeUnixTimeInMs": 1673953584305}]
```



#### Remove String from Custom List
The action removes a string from a custom list.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Category|Custom list Category|True|String|WhiteList|
|ListItem|The list item string to add to the custom list.|True|String|cajs3i|



##### JSON Results
```json
[  
    {  
        "Entity": "1.2.3.4",  
        "EntityResult": false  
    },  
    {  
        "Entity": "google.com",  
        "EntityResult": true  
    },  
    {  
        "Entity": "yahoo.co.uk",  
        "EntityResult": false  
    }  
]
```






## Jobs



## Connectors


