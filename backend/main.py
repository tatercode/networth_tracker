from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import AccountsResponse
from services.simplefin import getAccounts, getAccountsTotalBalance, getBalanceByAccount

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=[
      "http://localhost:5173",
      "http://127.0.0.1:5173",
  ],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/", response_model=AccountsResponse)
async def root():
    all_accounts = getAccounts()
    return all_accounts

@app.get("/networth")
async def get_networth():
    balance = getAccountsTotalBalance()
    return round(balance, 2)

@app.get("/account-balance")
async def get_balances():
    account_balances = getBalanceByAccount()
    return  account_balances



