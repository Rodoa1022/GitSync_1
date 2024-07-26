<p align="center"><img src="./Resources/VirusTotal.svg" 
     alt="VirusTotal" width="200"/></p>

# VirusTotal

VirusTotal is a service that analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content. VirusTotal aggregates many antivirus products and online scan engines to check for viruses that the user's own antivirus may have missed, or to verify against any false positives. Use VirusTotal to investigate suspicious files, domains, URLs, IP addresses, and hashes.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api key|None|True|Password|None|
|Verify SSL|None|False|Boolean|None|


#### Dependencies
| |
|-|
|asn1crypto-1.5.1-py2.py3-none-any.whl|
|bcrypt-4.1.3-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl|
|paramiko-3.4.0-py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|
|cryptography-42.0.5-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|requests-2.31.0-py3-none-any.whl|
|idna-3.6-py3-none-any.whl|
|cffi-1.16.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Scan IP
Scan IP via VirusTotal. Returns table of reverse domains and full Json result
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threshold|Specify the accepted threshold for the detected samples related to the IP address. If the number of engines that marked related samples as malicious is higher than the specified threshold, IP address will be marked as suspicious.|False|String|25|



##### JSON Results
```json
[{"EntityResult": {"asn": 4436, "undetected_urls": [["http://domain-example.il/short/commerce/2015/links/79/", "2ed06796f95e7c1cf48d4bd68d81754acf535c999e901bfe2cf9c45612396f66", 0, 66, "2017-11-23 06:51:49"]], "undetected_downloaded_samples": [{"date": "2018-07-09 07:53:30", "positives": 0, "sha256": "6a0bf66dbbd6473ddc73d7e64eb2ff0dd3512c5378c0c63c2ad4e13c0e1429fe", "total": 60}], "country": "US", "response_code": 1, "as_owner": "nLayer Communications, Inc.", "verbose_msg": "IP address in dataset", "detected_downloaded_samples": [{"date": "2015-05-26 08:38:00", "positives": 6, "sha256": "9cf5c07c99c3b261f97342d83b241c25850da0bf231ee150cb962cab1e8399cb", "total": 57}], "resolutions": [{"last_resolved": "2014-05-13 00:00:00", "hostname": "40515350444d1369ff68-2f7735d5ad283fa41a203a082d9a8f25.ssl.cf3.rackcdn.com"}], "detected_urls": [{"url": "http://domain-example.co.il/flowplayerlive/VideoLiveTricastHdsMbrNa.html?,,,470,268", "positives": 2, "total": 67, "scan_date": "2018-05-20 07:16:45"}]}, "Entity": "1.1.1.1"}]
```



#### Scan Hash
Scan Hash via VirusTotal. *Mark entity as suspicious and show insights if risk score matches a given threshold.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threshold|Mark entity as suspicious if number of negative engines is equal or above the given threshold|True|String||
|Rescan after days|Action will fetch the latest result. If the result is older than mentioned days it will automatically rescan the entity|False|String||



##### JSON Results
```json
[{"EntityResult": {"permalink": "https://www.virustotal.com/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/analysis/1549381312/", "sha1": "3395856ce81f2b7382dee72602f798b642f14140", "resource": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F", "response_code": 1, "scan_date": "2019-02-05 15:41:52", "scan_id": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f-1549381312", "verbose_msg": "Scan finished, information embedded", "total": 60, "positives": 54, "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f", "md5": "44d88612fea8a8f36de82e1278abb02f", "scans": {"Bkav": {"detected": true, "version": "1.1.1.1", "result": "DOS.EiracA.Trojan", "update": "20190201"}, "MicroWorld-eScan": {"detected": true, "version": "14.0.297.0", "result": "EICAR-Test-File", "update": "20190205"}}}, "Entity": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F"}]
```



#### Upload And Scan Files
Upload and scan files via VirusTotal. *Files can be uploaded from remote path (Windows share or Linux remote server).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Linux Password||False|Password||
|Threshold|Entity risk threshold.|True|String||
|File Paths|Target file path.|True|String||
|Linux Server Address|Linux server address(e.g: x.x.x.x).|False|String||
|Linux User||False|String||



##### JSON Results
```json
[{"EntityResult": {"vhash": null, "submission_names": ["file_name", "query.php", "xmldumper.php", "676f6f676c652xxx6d.exe", "isys_update_xxx.php", "wjzniacz", "acesso_seguro"], "scan_date": "2020-11-20 09:40:29", "first_seen": "2010-12-04 07:53:45", "total": 61, "additional_info": {"email_parents": [], "magic": "ASCII text, with no line terminators", "sigcheck": {}, "compressed_parents": ["2441fadeafe3b3fdb63d8a3a16ce900e44a28cddbf52dc279axxxxxx", "8c336c2adc8018ccbb71b45e797488b80d10da410a5c79fe250xxxx", "8eeab24940070ad89a835838b9392402844bcdfacfdbaa4ce4axxxxx", "79d8158ba573310183b46beba49c3596c321a2d369d62fe1792d3756xxxx", "ea10afd6489aba575c3a6bf359abe225b409f5265a1ad7f432bbxxxx"], "exiftool": {"MIMEType": "text/plain", "FileType": "TXT", "WordCount": "1", "LineCount": "1", "MIMEEncoding": "us-ascii", "FileTypeExtension": "txt", "Newlines": "(none)"}, "trid": "Unknown!", "positives_delta": 0, "pe_resource_parents": ["c14c00750ccf2b4ce39ed570bd3deb66bfc7ae126c5f557796a75axxxxx"]}, "size": 10, "scan_id": "d4c9d9027326271a89ce51fcaf328ed673f17be33469fab8dd501e664f-xxxxx", "times_submitted": 5, "harmless_votes": 0, "verbose_msg": "Scan finished, information embedded", "sha256": "d4c9d9027326271a89ce51fcaf328ed673f17be33469ff979exxxxx", "type": "Text", "scans": {"Bkav": {"detected": false, "version": "1.x.x.9899", "result": null, "update": "20201119"}, "MicroWorld-eScan": {"detected": false, "version": "14.x.x.0", "result": null, "update": "20201120"}, "FireEye": {"detected": false, "version": "32.x.x.0", "result": null, "update": "20201120"}, "CAT-QuickHeal": {"detected": false, "version": "14.xx", "result": null, "update": "20201119"}, "McAfee": {"detected": false, "version": "6.x.x.653", "result": null, "update": "20201120"}, "Malwarebytes": {"detected": false, "version": "3.x.x.335", "result": null, "update": "20201120"}, "Zillya": {"detected": false, "version": "2.x.x.4227", "result": null, "update": "20201120"}, "Sangfor": {"detected": false, "version": "1.x", "result": null, "update": "20201116"}, "K7AntiVirus": {"detected": false, "version": "11.xx.35774", "result": null, "update": "20201120"}, "K7GW": {"detected": false, "version": "11.151.xx", "result": null, "update": "20201120"}, "Invincea": {"detected": false, "version": "1.x.x.0", "result": null, "update": "20201120"}, "Baidu": {"detected": false, "version": "1.x.x.2", "result": null, "update": "20190318"}, "Cyren": {"detected": false, "version": "6.x.x.2", "result": null, "update": "20201120"}, "Symantec": {"detected": false, "version": "1.x.x.0", "result": null, "update": "20201120"}, "TotalDefense": {"detected": false, "version": "37.x.x.1", "result": null, "update": "20201120"}, "TrendMicro-HouseCall": {"detected": false, "version": "10.x.x.1040", "result": null, "update": "20201120"}, "Avast": {"detected": false, "version": "20.x.x.0", "result": null, "update": "20201120"}, "ClamAV": {"detected": false, "version": "0.x.x.0", "result": null, "update": "20201119"}, "Kaspersky": {"detected": false, "version": "15.x.x.13", "result": null, "update": "20201120"}, "BitDefender": {"detected": false, "version": "7.x", "result": null, "update": "20201120"}, "NANO-Antivirus": {"detected": false, "version": "1.x.x.25233", "result": null, "update": "20201120"}, "ViRobot": {"detected": false, "version": "2014.x.x.0", "result": null, "update": "20201120"}, "AegisLab": {"detected": false, "version": "4.x", "result": null, "update": "20201120"}, "Tencent": {"detected": false, "version": "1.x.x.1", "result": null, "update": "20201120"}, "Ad-Aware": {"detected": false, "version": "3.x.x.117", "result": null, "update": "20201120"}, "Sophos": {"detected": false, "version": "4.x.0", "result": null, "update": "20201120"}, "Comodo": {"detected": false, "version": "336", "result": null, "update": "20201120"}, "F-Secure": {"detected": false, "version": "12.0.x.x", "result": null, "update": "20201120"}, "DrWeb": {"detected": false, "version": "7.x.x.9080", "result": null, "update": "20201120"}, "VIPRE": {"detected": false, "version": "88336", "result": null, "update": "20201120"}, "TrendMicro": {"detected": false, "version": "11.x.x.1006", "result": null, "update": "20201120"}, "McAfee-GW-Edition": {"detected": false, "version": "v2019.1.2+xx", "result": null, "update": "20201119"}, "CMC": {"detected": false, "version": "2.7.x.1", "result": null, "update": "20201119"}, "Emsisoft": {"detected": false, "version": "2018.x.x.1641", "result": null, "update": "20201120"}, "Ikarus": {"detected": false, "version": "0.x.x.2", "result": null, "update": "20201119"}, "Jiangmin": {"detected": false, "version": "16.x.x", "result": null, "update": "20201120"}, "Avira": {"detected": false, "version": "8.x.x.8", "result": null, "update": "20201120"}, "Antiy-AVL": {"detected": false, "version": "3.0.0.1", "result": null, "update": "20201120"}, "Kingsoft": {"detected": false, "version": "2017.9.x.x", "result": null, "update": "20201120"}, "Microsoft": {"detected": false, "version": "1.1.x.x", "result": null, "update": "20201120"}, "Gridinsoft": {"detected": false, "version": "1.0.x.x", "result": null, "update": "20201120"}, "Arcabit": {"detected": false, "version": "1.0.x.x", "result": null, "update": "20201120"}, "SUPERAntiSpyware": {"detected": false, "version": "5.6.x.x", "result": null, "update": "20201113"}, "ZoneAlarm": {"detected": false, "version": "1.0", "result": null, "update": "20201120"}, "GData": {"detected": false, "version": "A:25.xxx:xx.20945", "result": null, "update": "20201120"}, "Cynet": {"detected": false, "version": "4.0.0.24", "result": null, "update": "20201120"}, "AhnLab-V3": {"detected": false, "version": "3.19.x.xx", "result": null, "update": "20201120"}, "BitDefenderTheta": {"detected": false, "version": "7.2.xx.x", "result": null, "update": "20201113"}, "ALYac": {"detected": false, "version": "1.x.x.5", "result": null, "update": "20201120"}, "TACHYON": {"detected": false, "version": "2020-11-20.02", "result": null, "update": "20201120"}, "VBA32": {"detected": false, "version": "4.4.1", "result": null, "update": "20201120"}, "Zoner": {"detected": false, "version": "0.x.x.0", "result": null, "update": "20201119"}, "ESET-NOD32": {"detected": false, "version": "223x", "result": null, "update": "20201119"}, "Rising": {"detected": false, "version": "25.0.x.x", "result": null, "update": "20201120"}, "Yandex": {"detected": false, "version": "5.5.x.xx", "result": null, "update": "20201117"}, "MAX": {"detected": false, "version": "2019.9.x.x", "result": null, "update": "20201120"}, "MaxSecure": {"detected": false, "version": "1.0.x.x", "result": null, "update": "20201119"}, "Fortinet": {"detected": false, "version": "6.2.x.x", "result": null, "update": "20201120"}, "AVG": {"detected": false, "version": "20.10.xx.x", "result": null, "update": "20201120"}, "Panda": {"detected": false, "version": "4.6.x.x", "result": null, "update": "20201119"}, "Qihoo-360": {"detected": false, "version": "1.0.x.xx", "result": null, "update": "20201120"}}, "tags": ["text"], "authentihash": null, "unique_sources": 4, "positives": 0, "ssdeep": "3:duK:IK", "md5": "1d5920f4b44b27a802bd77c4f053xxxx", "permalink": "https://www.virustotal.com/gui/file/d4c9d9027326271a89ce51fcaf328ed673f17be33469ff979e8abxxxx/detection/f-d4c9d9027326271a89ce51f8ed673f17be33469ff979e8ab8dd501e664f-xxxx", "sha1": "baea954b95731c68ae6e45bd1e252eb4xxxx", "resource": "d4c9d9027326271a89ce51f8ed673f17be33469ff979e8ab8dd501e664f-xxxxx", "response_code": 1, "community_reputation": 0, "malicious_votes": 0, "ITW_urls": ["http://52.xx.xx.234/tranquilapi/routes/query.php", "http://130.xx.81.xx/seeddms/pear/query.php", "http://110.5.xx.xx/conf/xmldumper.php", "http://bb.lucidweb.space/", "http://195.201.xx.xx/updates/classes/isys_update_sync.php?forumID=26120176&method=up", "http://195.xx.xx.26/updates/classes/isys_update_sync.php"], "last_seen": "2020-11-20 09:40:29"}, "Entity": "/opt/siemplify/siemplify_xxxx/Logs/file_name.txt"}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Get Domain Report
Scan Domain via VirusTotal. *Check online report for full details.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"detected_downloaded_samples": [], "undetected_downloaded_samples": [{"date": "2018-08-08 22:48:28", "positives": 0, "sha256": "ef1955ae757c8b966c83248350331bd3a30f658ced11f387f8ebf05ab3368000", "total": 59}], "resolutions": [{"last_resolved": "2019-01-13 03:31:09", "ip_address": "1.1.1.1"}], "Opera domain info": "The URL domain/host was seen to host badware at some point in time", "domain_siblings": [], "BitDefender domain info": "This URL domain/host was seen to host badware at some point in time", "whois": "Domain Name: GOOGLE.CO.IN\\nRegistry Domain ID: D8357-AFIN\\nRegistrar URL: http://www.markmonitor.com\\nUpdated Date: 2018-05-22T09:30:37Z\\nCreation Date: 2003-06-23T14:02:33Z\\nRegistry Expiry Date: 2019-06-23T14:02:33Z\\nRegistrar: MarkMonitor Inc.\\nRegistrar IANA ID: 292\\nDomain Status: clientDeleteProhibited\\nDomain Status: clientTransferProhibited\\nDomain Status: clientUpdateProhibited\\nRegistrant Country: US\\nName Server: NS1.GOOGLE.COM\\nName Server: NS2.GOOGLE.COM\\nName Server: NS3.GOOGLE.COM\\nName Server: NS4.GOOGLE.COM\\nDNSSEC: unsigned", "Alexa domain info": "google.co.in is one of the top 100 sites in the world and is in the Search_Engines category", "verbose_msg": "Domain found in dataset", "BitDefender category": "searchengines", "undetected_referrer_samples": [{"date": "2019-02-05 13:20:39", "positives": 0, "sha256": "3baf9f2a2d2b152193d2af602378b71e40d381e835b0aa3111851b2f29e64f38", "total": 71}], "whois_timestamp": 1548379042, "WOT domain info": {"Vendor reliability": "Excellent", "Child safety": "Excellent", "Trustworthiness": "Excellent", "Privacy": "Excellent"}, "detected_referrer_samples": [{"date": "2019-02-05 01:11:35", "positives": 1, "sha256": "097ea19b440441248b157698e2b23555cdf6117491b5f49f7ec8e492550cb02c", "total": 70}], "Forcepoint ThreatSeeker category": "search engines and portals", "Alexa category": "search_engines", "detected_communicating_samples": [{"date": "2019-01-28 23:58:13", "positives": 30, "sha256": "e65faa1283f8941d98dc23ff6822be228a24cb4489a5e5b01aeee749bf851658", "total": 70}], "TrendMicro category": "search engines portals", "categories": ["searchengines", "search engines and portals"], "undetected_urls": [["http://google.co.in/cwcspnqyntq", "daed97b2c77f0f72c9e4ee45506e3e1bc4e34d7b8846246877a02779bb85dd5b", 0, 70, "2019-02-04 14:58:23"]], "response_code": 1, "Webutation domain info": {"Safety score": 100, "Adult content": "no", "Verdict": "safe"}, "subdomains": ["www.google.co.in"], "Websense ThreatSeeker category": "search engines and portals", "detected_urls": [{"url": "http://google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&sqi=2&ved=0CCQQFjAB&url=http://www.vicky.in/bike/honda/activa/on-road-price-in-jamnagar/&ei=ApojVdTGE4KBuwTD14HIBw&usg=AFQjCNH5-ir0ZlKxQELVfE2iB-HbUyFsRg&bvm=bv.89947451d.c2E&cad=rja", "positives": 2, "total": 66, "scan_date": "2018-01-13 00:38:35"}], "Alexa rank": 100, "undetected_communicating_samples": [{"date": "2018-11-17 03:19:28", "positives": 0, "sha256": "e2a6ab7d594490c62bd3bb508dc38d7191ad48977da4d8dcce08dcb8af0070e9", "total": 68}], "pcaps": ["97e4a17068ce3ed01ed1c25c3d263fc0145e5ecc53b7db6f2ba84496b53d4a65"]}, "Entity": "google.co.in"}]
```



#### Scan URL
Scan URL via VirusTotal. *Mark entity as suspicious and show insights if risk score matches a given threshold.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threshold|Mark entity as suspicious if number of negative engines is equal or above the given threshold|True|String||
|Rescan after days|Action will fetch the latest result. If the result is older than mentioned days it will automatically rescan the entity|False|String||



##### JSON Results
```json
[{"EntityResult": {"permalink": "https://www.virustotal.com/url/057e8630c8880da8778b4f99e048933efb7cee9abdcf57fad89a7e7a2c7eae04/analysis/1549258134/", "resource": "http://domain-example.com/F1q7QX.php", "url": "http://domain-example.com/F1q7QX.php", "response_code": 1, "scan_date": "2019-02-04 05:28:54", "scan_id": "057e8630c8880da8778b4f99e048933efb7cee9abdcf57fad89a7e7a2c7eae04-1549258134", "verbose_msg": "Scan finished, scan information embedded in this object", "filescan_id": null, "positives": 5, "total": 67, "scans": {"CLEAN MX": {"detected": false, "result": "clean site"}, "DNS8": {"detected": false, "result": "clean site"}}}, "Entity": "http://domain-example.com/F1q7QX.php"}]
```






## Jobs



## Connectors


