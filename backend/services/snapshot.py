from sqlalchemy.orm import Session

from models.AccountBalance import AccountBalance
from models.Snapshot import Snapshot
from services.simplefin import getBalanceByAccount


def getSnapshot(db: Session) -> list[Snapshot]:
    return db.query(Snapshot).order_by(Snapshot.captured_at.desc()).all()


def takeSnapshot(db: Session) -> Snapshot:
    snapshot = Snapshot()
    db.add(snapshot)
    db.flush()

    balances = getBalanceByAccount()
    for account_name, balance in balances.items():
        db.add(
            AccountBalance(
                snapshot_id=snapshot.id,
                account_name=account_name,
                balance=float(balance),
            )
        )

    db.commit()
    db.refresh(snapshot)
    return snapshot


def listSnapshots(db: Session) -> list[dict[str, object]]:
    snapshots = getSnapshot(db)
    return [
        {
            "id": snapshot.id,
            "captured_at": snapshot.captured_at,
        }
        for snapshot in snapshots
    ]


def createSnapshotSummary(db: Session) -> dict[str, object]:
    snapshot = takeSnapshot(db)
    balances = (
        db.query(AccountBalance)
        .filter(AccountBalance.snapshot_id == snapshot.id)
        .order_by(AccountBalance.account_name.asc())
        .all()
    )
    networth = sum(float(item.balance or 0) for item in balances)

    return {
        "id": snapshot.id,
        "captured_at": snapshot.captured_at,
        "account_count": len(balances),
        "networth": round(networth, 2),
    }
