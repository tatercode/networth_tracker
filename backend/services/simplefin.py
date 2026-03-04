from collections import defaultdict
import json
from typing import Any, cast

import requests
from config import Settings


def getAccounts() -> dict[str, Any]:
    access_url: str | None = Settings.access_url
    if not access_url:
        return {"Message": "Failed to get access url"}
    scheme, rest = access_url.split('//', 1)
    auth, rest = rest.split('@', 1)
    url = scheme + '//' + rest + '/accounts'
    username, password = auth.split(':', 1)
    response = requests.get(url, auth=(username, password))
    data = cast(dict[str, Any], response.json())
    return data 

def getAccountsTotalBalance() -> float:
    accounts = cast(list[dict[str, Any]], getAccounts()['accounts'])
    balance = 0
    for account in accounts:
        balance += float(account['balance'])

    return balance

def getBalanceByAccount() -> str:
    accounts = cast(list[dict[str, Any]], getAccounts()['accounts'])
    account_balance = defaultdict(float)
    for account in accounts:
        name = account['name']
        balance = account['balance']
        account_balance[name] = balance
    return json.dumps(account_balance)
