#!/usr/local/bin/python

import json
import requests
import os
import sys

service_name = os.environ.get('SERVICE_NAME')
output = json.load(open('rfc3.json'))
data = {}
data['serviceName'] = service_name
data['key'] = 'rfc3'
data['output'] = output
rfc3_data = json.dumps(data)
rfc3_file = json.loads(rfc3_data)
print (rfc3_file)
url = "https://api.getcortexapp.com/api/v1/custom-integrations/data/dbbf5c4a-b371-4194-842c-41bbf1db3655"
headers = {
            'content-type': 'application/json'
        }

rfc3 = requests.post(url, json=rfc3_file, headers=headers)
print("Pushed rfc3 data")
print(rfc3.text)