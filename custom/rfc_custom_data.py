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

output = json.load(open('rfc5.json'))
data = {}
data['serviceName'] = service_name
data['key'] = 'rfc5'
data['output'] = output
rfc5_data = json.dumps(data)
rfc5_file = json.loads(rfc5_data)
print (rfc5_file)
url = "https://api.getcortexapp.com/api/v1/custom-integrations/data/4d7d9a5f-6034-4d86-a1ab-ebf90e8f60ce"
headers = {
            'content-type': 'application/json'
        }

rfc5 = requests.post(url, json=rfc5_file, headers=headers)
print("Pushed rfc5 data")
print(rfc5.text)

output = json.load(open('rfc7.json'))
data = {}
data['serviceName'] = service_name
data['key'] = 'rfc7'
data['output'] = output
rfc7_data = json.dumps(data)
rfc7_file = json.loads(rfc7_data)
print (rfc7_file)
url = "https://api.getcortexapp.com/api/v1/custom-integrations/data/c785f666-b6d4-46e3-bc32-95fa60217673"
headers = {
            'content-type': 'application/json'
        }

rfc7 = requests.post(url, json=rfc7_file, headers=headers)
print("Pushed rfc5 data")
print(rfc7.text)
