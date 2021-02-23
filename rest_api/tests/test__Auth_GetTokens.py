#!/usr/bin/python3
import requests
import json


print('\n 1. Login in Odoo and get access tokens:')
r = requests.get(
    'http://localhost:8069/api/auth/get_tokens',
    headers={'Content-Type': 'text/html; charset=utf-8'},
    data=json.dumps({
        'username': 'admin',
        'password': 'admin',
    }),
    # verify = False      # for TLS/SSL connection
)
print(r.text)
