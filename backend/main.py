from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schemas import AccountsResponse
from services.simplefin import getAccounts, getAccountsTotalBalance, getBalanceByAccount
from services.snapshot import createSnapshotSummary, listSnapshots

Base.metadata.create_all(bind=engine)

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


@app.get("/")
async def root():
    return {"Status": "Online"}


@app.get("/get-everything", response_model=AccountsResponse)
async def get_everything():
    all_accounts = getAccounts()
    return all_accounts


@app.get("/networth")
async def get_networth():
    balance = getAccountsTotalBalance()
    return round(balance, 2)


@app.get("/account-balance")
async def get_balances():
    account_balances = getBalanceByAccount()
    return account_balances


@app.get("/snapshot")
async def list_snapshots(db: Session = Depends(get_db)):
    return listSnapshots(db)


@app.post("/snapshot")
async def create_snapshot(db: Session = Depends(get_db)):
    return createSnapshotSummary(db)
