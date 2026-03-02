import base64
import requests
from config import Settings
import json
from collections import defaultdict

def getAccounts() -> json:
    access_url = Settings.access_url
    scheme, rest = access_url.split('//', 1)
    auth, rest = rest.split('@', 1)
    url = scheme + '//' + rest + '/accounts'
    username, password = auth.split(':', 1)
    response = requests.get(url, auth=(username, password))
    data = response.json()
    return data 

def getAccountsTotalBalance() -> float:
    accounts = getAccounts()['accounts']
    print(accounts)
    balance = 0
    for account in accounts:
        balance += float(account['balance'])

    return balance

def getBalanceByAccount() -> json:
    accounts = getAccounts()['accounts']
    account_balance = defaultdict(float)
    for account in accounts:
        name = account['name']
        balance = account['balance']
        account_balance[name] = balance
    return json.dumps(account_balance)
