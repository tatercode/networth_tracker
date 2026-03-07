from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class AccountBalance(Base):
    __tablename__ = "account_balances"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    snapshot_id: Mapped[int] = mapped_column(ForeignKey("snapshots.id"), index=True)
    account_name: Mapped[str] = mapped_column(String, index=True)
    balance: Mapped[float] = mapped_column(Float)
