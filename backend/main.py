from fastapi import FastAPI

from schemas import AccountsResponse
from services.simplefin import getAccounts, getAccountsTotalBalance, getBalanceByAccount

app = FastAPI()


@app.get("/", response_model=AccountsResponse)
async def root():
    all_accounts = getAccounts()
    return all_accounts

@app.get("/networth")
async def get_networth():
    balance = getAccountsTotalBalance()
    return balance

@app.get("/account-balance")
async def get_balances():
    account_balances = getBalanceByAccount()
    return  account_balances



