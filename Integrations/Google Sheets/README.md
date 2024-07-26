
# Google Sheets

Google Sheets is a spreadsheet program included as part of a free, web-based software office suite offered by Google within its Google Drive service. 

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Credentials Json|View the guide on how to create auth json credentials (service account)https://gspread.readthedocs.io/en/latest/oauth2.html#enable-api-access|True|Password|None|


#### Dependencies
| |
|-|
|chardet-3.0.4-py2.py3-none-any.whl|
|asynctest-0.13.0-py3-none-any.whl|
|attrs-20.2.0-py2.py3-none-any.whl|
|idna-2.10-py2.py3-none-any.whl|
|charset_normalizer-2.1.1-py3-none-any.whl|
|google_auth-2.16.0-py2.py3-none-any.whl|
|urllib3-1.26.14-py2.py3-none-any.whl|
|google_auth-1.22.0-py2.py3-none-any.whl|
|pyasn1-0.4.8-py2.py3-none-any.whl|
|requests_oauthlib-1.3.0-py2.py3-none-any.whl|
|aiosignal-1.3.1-py3-none-any.whl|
|oauthlib-3.1.0-py2.py3-none-any.whl|
|async_timeout-4.0.2-py3-none-any.whl|
|urllib3-1.25.10-py2.py3-none-any.whl|
|aiohttp-3.8.3-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|async_timeout-3.0.1-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|requests-2.28.2-py3-none-any.whl|
|typing_extensions-3.7.4.3-py3-none-any.whl|
|google_auth_oauthlib-0.4.1-py2.py3-none-any.whl|
|aiohttp-3.6.2-cp37-cp37m-manylinux1_x86_64.whl|
|setuptools-50.3.0-py3-none-any.whl|
|pyasn1_modules-0.2.8-py2.py3-none-any.whl|
|google_auth_oauthlib-1.0.0-py2.py3-none-any.whl|
|certifi-2020.6.20-py2.py3-none-any.whl|
|requests-2.24.0-py2.py3-none-any.whl|
|six-1.15.0-py2.py3-none-any.whl|
|certifi-2022.12.7-py3-none-any.whl|
|rsa-4.6-py3-none-any.whl|
|yarl-1.6.0-cp37-cp37m-manylinux1_x86_64.whl|
|frozenlist-1.3.3-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|setuptools-65.5.1-py3-none-any.whl|
|multidict-4.7.6-cp37-cp37m-manylinux1_x86_64.whl|
|gspread-3.6.0-py3-none-any.whl|
|cachetools-4.1.1-py3-none-any.whl|


## Actions
#### Import CSV
Imports data into the first page of the spreadsheet.
*This method removes all other worksheets and then replaces the content of the first worksheet.*
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|CSV Path|The path that locates the CSV file you would like to import.|True|String|/temp/data_to_imprort.csv|



##### JSON Results
```json
{}
```



#### Add or Update Rows
Add or update rows by a given column name.
(If the value isn't found in the sheet it will be added as a new row)
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|End Column|Untill which column number we will update or add the values ​​to the given rows|True|String|2|
|Column Number|The column number by which we will look for the value of the given Field Name in the Json|True|String|1|
|Start Column|From which column number we will update or add the values ​​to the given rows|True|String|1|
|Field Name|This is the field name in the given Json by which we will search for its value in a row by its column number.|True|String|Field_Key_1|
|Json|The JSON values to add or update for the chosen column number and field name. Each item will be one row.Note: each value needs to be unique.|True|Code|[
  {
    "Field_Key_1": "Field_Value_1",
    "Field_Key_2": "Field_Value_2",
    "Field_Key_3": "Field_Value_3"
  }
]|
|Sheet Id|The sheet Id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|



##### JSON Results
```json
{}
```



#### Delete Rows
Deletes rows in a given worksheet 
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|
|From Row|The row number from which you would like to start deleting the rows.|True|String|2|
|To Row|The row number that will define the range of the rows that will be deleted. |True|String|3|



##### JSON Results
```json
{}
```



#### Add Row
Adds a row to a given sheet in Google Sheets
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet Id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|
|Row Index|The location in the spreadsheet where the row is added (one-based). Default is 1. |False|String|<Row-1>|
|Values|The values you would like to add in the row. Values should be comma separated. |True|String|val1,val2,val3|



##### JSON Results
```json
{}
```



#### Search Row
Finds a specific row in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|
|Column Number|The column number for the value you would like to search in the spreadsheet|True|String|1|
|Search value|The value you would like to search for in the sheet|True|String|<Value>|



##### JSON Results
```json
{}
```



#### Ping
Test connectivity with Google Sheets
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Create Sheet
Creates a new Sheet 
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". |True|String|<Sheet-Name>|
|Share with emails|Email address of the person you would like to add permission to the Spreadsheet. You can add multiple emails by adding ";" as a separator. |False|String|email1@gmail.com;email2@gmail.com;email3@gmail.com|



##### JSON Results
```json
{}
```



#### Update Row
Updates a specific row in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|
|Row Number|The row number of the row you would like to update in the sheet. |True|String|1|
|Values|The values you would like to update in the row. |True|String|val_1,val_2,val_3,val_4,val_5|



##### JSON Results
```json
{}
```



#### Update  Cell
Updates a specific cell in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|
|Cell|The cell you would like to update in the sheet|True|String|A12|
|Value|The value you would like to update in the cell|True|String|<Value>|



##### JSON Results
```json
{}
```



#### Search Rows
Finds multiple rows in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|
|Column Number|The column number you would like to search for rows in a given sheet. |True|String|1|
|Search value|The value you would like to search for in the sheet|True|String|<Value>|



##### JSON Results
```json
{}
```



#### Get Range
Retrieves the values for a given range in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|
|Range|The range for which you would like to extract the sheet values - (https://developers.google.com/sheets/api/guides/concepts#a1_notation)|True|String|A1:B1|



##### JSON Results
```json
{}
```



#### Add  Permission
Adds permission to a Google Sheet for a single user or multiple users


Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Role|"Owner"- allows to make any changes to the document"Reader"- allows to open and view the document"Writer"- allows to leave comments in the document|True|List|Writer|
|Emails|Email address of the person you would like to add permission to the Spreadsheet. You can add multiple emails by adding ";" as a separator. |True|String|email1@gmail.com;email2@gmail.com|



##### JSON Results
```json
{}
```



#### Get Row
Retrieves the values of a single row in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The shhet id can be found in the sheet url.|True|String|<Sheet-Id>|
|Worksheet Name|Worksheet Name|False|String|None|
|Row Number|Row number (one-based).|True|String|3|



##### JSON Results
```json
{}
```



#### Update Rows
Updates rows in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Row Number|The row numbers you want to update. Should be comma separated|True|String|1,2|
|Values|The values you want to update. Should be comma separated|True|Content|value1,value2,value3|
|Sheet Id|The sheet Id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|



##### JSON Results
```json
{}
```



#### Get All
Retrieves the values for a given range in a sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<Sheet-Id>|
|Worksheet Name|The worksheet name is the Sheet tab name. The default Sheet name is "Sheet1". Note: it is case sensitive. |False|String|<Sheet-Name>|



##### JSON Results
```json
{}
```



#### Delete Sheet
Deletes a given sheet
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sheet Id|The sheet id can be found in the sheet url.https://docs.google.com/spreadsheets/d/{YourSpreadSheetId}/edit#gid=0|True|String|<sheet_id>|



##### JSON Results
```json
{}
```






## Jobs



## Connectors
#### Sheet Connector
The connector pulls each row in a Google Sheet form

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Name Column Index|Alert Name Column Index|True|Integer|0|
|Credentials Json|Credentials Json|True|String|{}|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|device_event|
|Filter Alert Column Index|Filter Alert Column Index|False|Integer|None|
|Filter Alert Column Value|Filter Alert Column Value|False|String|None|
|Product|Product|True|String|<Sheet>|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|
|Sheet Id|Sheet Id|True|String|<Sheet Id>|
|Worksheet Name|Worksheet Name|True|String|Sheet1|




