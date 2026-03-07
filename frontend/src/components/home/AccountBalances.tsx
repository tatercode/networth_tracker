
import { useEffect, useState } from "react";
import { getAllBalances } from '@/services/balances';

function AccountBalances() {
  const [accountBalances, setAccountBalances] = useState<Record<string, string> | null>(null);

  useEffect(() => {
    async function loadAccountBalances() {
      const value = await getAllBalances();
      setAccountBalances(value);
    }

    loadAccountBalances();
  }, [])

  if (!accountBalances) {
    return <p className="text-sm text-muted-foreground">Loading balances...</p>;
  }

  return (
    <div className="space-y-2">
      {Object.entries(accountBalances).map(([name, balance]) => (
        <div className="flex items-center justify-between rounded-md border px-3 py-2" key={name}>
          <p className="pr-4 text-sm">{name}</p>
          <p className="text-sm font-semibold">{balance}</p>
        </div>
      ))}
    </div>
  )
}

export default AccountBalances;
