
import { useEffect, useState } from "react";
import { getAllBalances } from '@/services/balances';
import {
  Card,
  CardTitle,
  CardHeader,
  CardContent,
} from "@/components/ui/card"

function AccountBalances() {
  const [accountBalances, setAccountBalances] = useState<Record<string, string> | null>(null);

  useEffect(() => {
    async function loadAccountBalances() {
      const value = await getAllBalances();
      setAccountBalances(value);
    }

    loadAccountBalances();
  }, [])

  return (
    <main className="w-full max-w-lg">
      {accountBalances &&
        Object.entries(accountBalances).map(([name, balance]) => (
          <Card className="w-full max-w-lg shadow-lg" key={name}>
            <CardHeader>
              <CardTitle className="text-2xl">{name}</CardTitle>
            </CardHeader>
            <CardContent>
              <h1 className="mt-2 text-4xl font-semibold tracking-tight">{balance}</h1>
            </CardContent>
          </Card>
        ))}
    </main>
  )
}

export default AccountBalances;
