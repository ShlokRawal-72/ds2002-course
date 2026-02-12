#!/usr/bin/env python3

import os
import json
import requests

# Get GitHub username from environment
GHUSER = os.getenv('GITHUB_USER')

# Build API URL
url = f'https://api.github.com/users/{GHUSER}/events'

# Fetch data
response = requests.get(url)
r = json.loads(response.text)

# Print first 5 events
for x in r[:5]:
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)
