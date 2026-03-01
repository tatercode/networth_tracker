from __future__ import annotations

from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Organization(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    domain: str
    name: str
    sfin_url: str = Field(alias="sfin-url")
    url: str
    id: str


class Transaction(BaseModel):
    id: str
    posted: int
    amount: Decimal
    description: str
    payee: str
    memo: str
    transacted_at: int


class Account(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    currency: str
    balance: Decimal
    available_balance: Decimal = Field(alias="available-balance")
    balance_date: int = Field(alias="balance-date")
    transactions: list[Transaction]
    holdings: list[dict[str, Any]]
    org: Organization


class AccountsResponse(BaseModel):
    accounts: list[Account]
