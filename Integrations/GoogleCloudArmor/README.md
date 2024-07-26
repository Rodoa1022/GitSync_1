
# GoogleCloudArmor

Google Cloud Armor helps you protect your Google Cloud deployments from multiple types of threats, including distributed denial-of-service (DDoS) attacks and application attacks like cross-site scripting (XSS) and SQL injection (SQLi). Google Cloud Armor features some automatic protections and some that you need to configure manually.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Google Cloud Armor service.|True|String|https://compute.googleapis.com/compute/v1/|
|Project ID|Project ID to use for the Cloud Armor integration. If no value is provided, the Project ID is extracted from the JSON file content provided in the User Service Account parameter.|False|String||
|Workload Identity Email|Client email of your service account. You can configure either this parameter or the User Service Account parameter. Note: To impersonate service accounts with the Workload Identity Email, grant the Service Account Token Creator role to your service account. For more details about workload identities and how to work with them, see Identities for workloads (https://cloud.google.com/iam/docs/workload-identities).|False|String||
|User Service Account|Content of the service account JSON file that you use for the Google Cloud Armor service. Provide a full content of the service account JSON file. You can configure either this parameter or the Workload Identity Email parameter.|False|Password|None|
|Verify SSL|If selected, the parameter verifies that the SSL certificate for the connection to the Google Cloud Armor service is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|cross/idna-3.3-py3-none-any.whl|
|cross/google_auth-2.5.0-py2.py3-none-any.whl|
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
#### Update a Security Policy
Update the existing security policy in the Google Cloud Armor service. The action cannot update rules in a policy. To add a rule to the related policy, use the Add a Rule to a Security Policy action. This action doesn't run on Google SecOps SOAR entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy Name|Security policy name to update.|True|String||
|Region|Region for the updated policy. If no value is provided, the global-level security policy is created.|False|String||
|Policy JSON|JSON definition of the policy to update. For more information about the policy updates, see Method: securityPolicies.patch (https://cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/patch). You cannot update rules with this action. To add a rule to a policy, use the Add a Rule to a Security Policy action.|True|Content|{
  "userDefinedFields": [
    {
    "name": string,
    "base": enum,
    "offset": integer,
    "size": integer,
    "mask": string
    }
  ],
  "name": string,
  "description": string,
  "rules": [
    {
    "description": string,
    "priority": integer,
    "match": {
      "expr": {
      "expression": string,
      "title": string,
      "description": string,
      "location": string
      },
      "exprOptions": {
      "recaptchaOptions": {
        "actionTokenSiteKeys": [
        string
        ],
        "sessionTokenSiteKeys": [
        string
        ]
      }
      },
      "versionedExpr": enum,
      "config": {
      "srcIpRanges": [
        string
      ]
      }
    },
    "networkMatch": {
      "userDefinedFields": [
      {
        "name": string,
        "values": [
        string
        ]
      }
      ],
      "srcIpRanges": [
      string
      ],
      "destIpRanges": [
      string
      ],
      "ipProtocols": [
      string
      ],
      "srcPorts": [
      string
      ],
      "destPorts": [
      string
      ],
      "srcRegionCodes": [
      string
      ],
      "srcAsns": [
      integer
      ]
    },
    "action": string,
    "preview": boolean,
    "rateLimitOptions": {
      "rateLimitThreshold": {
      "count": integer,
      "intervalSec": integer
      },
      "conformAction": string,
      "exceedAction": string,
      "exceedRedirectOptions": {
      "type": enum,
      "target": string
      },
      "enforceOnKey": enum,
      "enforceOnKeyName": string,
      "enforceOnKeyConfigs": [
      {
        "enforceOnKeyType": enum,
        "enforceOnKeyName": string
      }
      ],
      "banThreshold": {
      "count": integer,
      "intervalSec": integer
      },
      "banDurationSec": integer
    },
    "headerAction": {
      "requestHeadersToAdds": [
      {
        "headerName": string,
        "headerValue": string
      }
      ]
    },
    "redirectOptions": {
      "type": enum,
      "target": string
    },
    "preconfiguredWafConfig": {
      "exclusions": [
      {
        "targetRuleSet": string,
        "targetRuleIds": [
        string
        ],
        "requestHeadersToExclude": [
        {
          "val": string,
          "op": enum
        }
        ],
        "requestCookiesToExclude": [
        {
          "val": string,
          "op": enum
        }
        ],
        "requestQueryParamsToExclude": [
        {
          "val": string,
          "op": enum
        }
        ],
        "requestUrisToExclude": [
        {
          "val": string,
          "op": enum
        }
        ]
      }
      ]
    }
    }
  ],
  "adaptiveProtectionConfig": {
    "layer7DdosDefenseConfig": {
    "enable": boolean,
    "ruleVisibility": enum,
    "thresholdConfigs": [
      {
      "name": string,
      "autoDeployLoadThreshold": number,
      "autoDeployConfidenceThreshold": number,
      "autoDeployImpactedBaselineThreshold": number,
      "autoDeployExpirationSec": integer
      }
    ]
    }
  },
  "ddosProtectionConfig": {
    "ddosProtection": enum
  },
  "advancedOptionsConfig": {
    "jsonParsing": enum,
    "jsonCustomConfig": {
    "contentTypes": [
      string
    ]
    },
    "logLevel": enum,
    "userIpRequestHeaders": [
    string
    ]
  },
  "recaptchaOptionsConfig": {
    "redirectSiteKey": string
  },
  "fingerprint": string,
  "type": enum,
  "labels": {
    string: string,
    ...
  },
  "labelFingerprint": string
  }|



##### JSON Results
```json
{"kind":"compute#securityPolicy","id":"2753918331621109894","creationTimestamp":"2024-04-14T05:39:05.798-07:00","name":"testintegration","description":"Testforintegration","rules":[{"kind":"compute#securityPolicyRule","description":"test","priority":100,"match":{"versionedExpr":"SRC_IPS_V1","config":{"srcIpRanges":["*"]}},"action":"allow","preview":false},{"kind":"compute#securityPolicyRule","description":"Defaultrule,higherpriorityoverridesit","priority":2147483647,"match":{"versionedExpr":"SRC_IPS_V1","config":{"srcIpRanges":["*"]}},"action":"allow","preview":false}],"fingerprint":"A3hq2ZQYxj8=","selfLink":"https://www.googleapis.com/compute/v1/projects/xyz/regions/northamerica-northeast1/securityPolicies/testintegration","type":"CLOUD_ARMOR","labelFingerprint":"42WmSpB8rSM=","region":"https://www.googleapis.com/compute/v1/projects/xyz/regions/northamerica-northeast1"}
```



#### Create a Security Policy
Create a security policy in the Google Cloud Armor service. This action doesn't run on Google SecOps SOAR entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Region|The region to create a policy in. If no value is provided, the global-level security policy is created.|False|String||
|Policy JSON|The JSON definition of the policy to create. For more information about policies, see REST Resource: securityPolicies (https://cloud.google.com/compute/docs/reference/rest/v1/securityPolicies).|True|Content|{
  "userDefinedFields": [
    {
      "name": string,
      "base": enum,
      "offset": integer,
      "size": integer,
      "mask": string
    }
  ],
  "name": string,
  "description": string,
  "rules": [
    {
      "description": string,
      "priority": integer,
      "match": {
        "expr": {
          "expression": string,
          "title": string,
          "description": string,
          "location": string
        },
        "exprOptions": {
          "recaptchaOptions": {
            "actionTokenSiteKeys": [
              string
            ],
            "sessionTokenSiteKeys": [
              string
            ]
          }
        },
        "versionedExpr": enum,
        "config": {
          "srcIpRanges": [
            string
          ]
        }
      },
      "networkMatch": {
        "userDefinedFields": [
          {
            "name": string,
            "values": [
              string
            ]
          }
        ],
        "srcIpRanges": [
          string
        ],
        "destIpRanges": [
          string
        ],
        "ipProtocols": [
          string
        ],
        "srcPorts": [
          string
        ],
        "destPorts": [
          string
        ],
        "srcRegionCodes": [
          string
        ],
        "srcAsns": [
          integer
        ]
      },
      "action": string,
      "preview": boolean,
      "rateLimitOptions": {
        "rateLimitThreshold": {
          "count": integer,
          "intervalSec": integer
        },
        "conformAction": string,
        "exceedAction": string,
        "exceedRedirectOptions": {
          "type": enum,
          "target": string
        },
        "enforceOnKey": enum,
        "enforceOnKeyName": string,
        "enforceOnKeyConfigs": [
          {
            "enforceOnKeyType": enum,
            "enforceOnKeyName": string
          }
        ],
        "banThreshold": {
          "count": integer,
          "intervalSec": integer
        },
        "banDurationSec": integer
      },
      "headerAction": {
        "requestHeadersToAdds": [
          {
            "headerName": string,
            "headerValue": string
          }
        ]
      },
      "redirectOptions": {
        "type": enum,
        "target": string
      },
      "preconfiguredWafConfig": {
        "exclusions": [
          {
            "targetRuleSet": string,
            "targetRuleIds": [
              string
            ],
            "requestHeadersToExclude": [
              {
                "val": string,
                "op": enum
              }
            ],
            "requestCookiesToExclude": [
              {
                "val": string,
                "op": enum
              }
            ],
            "requestQueryParamsToExclude": [
              {
                "val": string,
                "op": enum
              }
            ],
            "requestUrisToExclude": [
              {
                "val": string,
                "op": enum
              }
            ]
          }
        ]
      }
    }
  ],
  "adaptiveProtectionConfig": {
    "layer7DdosDefenseConfig": {
      "enable": boolean,
      "ruleVisibility": enum,
      "thresholdConfigs": [
        {
          "name": string,
          "autoDeployLoadThreshold": "number",
          "autoDeployConfidenceThreshold": "number",
          "autoDeployImpactedBaselineThreshold": "number",
          "autoDeployExpirationSec": integer
        }
      ]
    }
  },
  "ddosProtectionConfig": {
    "ddosProtection": enum
  },
  "advancedOptionsConfig": {
    "jsonParsing": enum,
    "jsonCustomConfig": {
      "contentTypes": [
        string
      ]
    },
    "logLevel": enum,
    "userIpRequestHeaders": [
      string
    ]
  },
  "recaptchaOptionsConfig": {
    "redirectSiteKey": string
  },
  "fingerprint": string,
  "type": enum,
  "labels": {
    string: string,
    ...
  },
  "labelFingerprint": string
}|



##### JSON Results
```json
{"kind":"compute#securityPolicy","id":"2753918331621109894","creationTimestamp":"2024-04-14T05:39:05.798-07:00","name":"testintegration","description":"Testforintegration","rules":[{"kind":"compute#securityPolicyRule","description":"test","priority":100,"match":{"versionedExpr":"SRC_IPS_V1","config":{"srcIpRanges":["*"]}},"action":"allow","preview":false},{"kind":"compute#securityPolicyRule","description":"Defaultrule,higherpriorityoverridesit","priority":2147483647,"match":{"versionedExpr":"SRC_IPS_V1","config":{"srcIpRanges":["*"]}},"action":"allow","preview":false}],"fingerprint":"A3hq2ZQYxj8=","selfLink":"https://www.googleapis.com/compute/v1/projects/xyz/regions/northamerica-northeast1/securityPolicies/testintegration","type":"CLOUD_ARMOR","labelFingerprint":"42WmSpB8rSM=","region":"https://www.googleapis.com/compute/v1/projects/xyz/regions/northamerica-northeast1"}
```



#### Ping
Test connectivity to the Google Cloud Armor service with parameters provided at the integration configuration page.
Timeout - 600 Seconds



#### Add a Rule to a Security Policy
Add a new rule to the security policy in the Google Cloud Armor service. This action doesn't run on Google SecOps SOAR entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy Name|Security policy name to add a new rule to.|True|String||
|Region|Region for the policy to add the rule in. If no value is provided, the rule is added to the global-level security policy.|False|String||
|Rule JSON|JSON definition of the rule to add. For more information about adding a rule to a policy, see Method: securityPolicies.addRule (https://cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/addRule).|True|Content|{
  "kind": string,
  "description": string,
  "priority": integer,
  "match": {
    "expr": {
    "expression": string,
    "title": string,
    "description": string,
    "location": string
    },
    "exprOptions": {
    "recaptchaOptions": {
      "actionTokenSiteKeys": [
      string
      ],
      "sessionTokenSiteKeys": [
      string
      ]
    }
    },
    "versionedExpr": enum,
    "config": {
    "srcIpRanges": [
      string
    ]
    }
  },
  "networkMatch": {
    "userDefinedFields": [
    {
      "name": string,
      "values": [
      string
      ]
    }
    ],
    "srcIpRanges": [
    string
    ],
    "destIpRanges": [
    string
    ],
    "ipProtocols": [
    string
    ],
    "srcPorts": [
    string
    ],
    "destPorts": [
    string
    ],
    "srcRegionCodes": [
    string
    ],
    "srcAsns": [
    integer
    ]
  },
  "action": string,
  "preview": boolean,
  "rateLimitOptions": {
    "rateLimitThreshold": {
    "count": integer,
    "intervalSec": integer
    },
    "conformAction": string,
    "exceedAction": string,
    "exceedRedirectOptions": {
    "type": enum,
    "target": string
    },
    "enforceOnKey": enum,
    "enforceOnKeyName": string,
    "enforceOnKeyConfigs": [
    {
      "enforceOnKeyType": enum,
      "enforceOnKeyName": string
    }
    ],
    "banThreshold": {
    "count": integer,
    "intervalSec": integer
    },
    "banDurationSec": integer
  },
  "headerAction": {
    "requestHeadersToAdds": [
    {
      "headerName": string,
      "headerValue": string
    }
    ]
  },
  "redirectOptions": {
    "type": enum,
    "target": string
  },
  "preconfiguredWafConfig": {
    "exclusions": [
    {
      "targetRuleSet": string,
      "targetRuleIds": [
      string
      ],
      "requestHeadersToExclude": [
      {
        "val": string,
        "op": enum
      }
      ],
      "requestCookiesToExclude": [
      {
        "val": string,
        "op": enum
      }
      ],
      "requestQueryParamsToExclude": [
      {
        "val": string,
        "op": enum
      }
      ],
      "requestUrisToExclude": [
      {
        "val": string,
        "op": enum
      }
      ]
    }
    ]
  }
}|



##### JSON Results
```json
{"kind":"compute#securityPolicy","id":"2753918331621109894","creationTimestamp":"2024-04-14T05:39:05.798-07:00","name":"testintegration","description":"Testforintegration","rules":[{"kind":"compute#securityPolicyRule","description":"test","priority":100,"match":{"versionedExpr":"SRC_IPS_V1","config":{"srcIpRanges":["*"]}},"action":"allow","preview":false},{"kind":"compute#securityPolicyRule","description":"Defaultrule,higherpriorityoverridesit","priority":2147483647,"match":{"versionedExpr":"SRC_IPS_V1","config":{"srcIpRanges":["*"]}},"action":"allow","preview":false}],"fingerprint":"A3hq2ZQYxj8=","selfLink":"https://www.googleapis.com/compute/v1/projects/xyz/regions/northamerica-northeast1/securityPolicies/testintegration","type":"CLOUD_ARMOR","labelFingerprint":"42WmSpB8rSM=","region":"https://www.googleapis.com/compute/v1/projects/xyz/regions/northamerica-northeast1"}
```






## Jobs



## Connectors


