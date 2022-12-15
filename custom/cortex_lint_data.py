#!/usr/local/bin/python

import json
import requests
import os

service_name = os.environ.get('SERVICE_NAME')
output = json.load(open('report/api_lint_result.json'))
data = {}
data['serviceName'] = service_name
data['key'] = 'spectral'
data['output'] = output
lintdump = json.dumps(data)
lint_file = json.loads(lintdump)
print (lintdump)

url = "https://api.getcortexapp.com/api/v1/custom-integrations/data/f1492006-6383-453a-8313-05757585fa12"
headers = {
            'content-type': 'application/json'
        }

lint = requests.post(url, json=lint_file, headers=headers)
print("Pushed lint data")
