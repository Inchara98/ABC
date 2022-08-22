import requests
import json

from utilities.readProperties import ReadConfig

data = ReadConfig()
url = data.getApplicationURL()+"api/common/getReportData"

print(url)
payload = json.dumps({
    "appName": "national",
    "dataSourceName": "nishtha",
    "reportName": "programStatus",
    "reportType": "map",
    "stateCode": "NA"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
info = response.json()
print(info)
