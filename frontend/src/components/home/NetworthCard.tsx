import { useEffect, useState } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { getNetworth } from '@/services/balances';

function NetworthCard() {
  const [networth, setNetworth] = useState<number | undefined>();

  useEffect(() => {
    async function loadNetWorth() {
      const value = await getNetworth();
      setNetworth(value);
    }

    loadNetWorth();
  }, [])

  return (
      <Card className="w-full max-w-lg shadow-lg">
      <CardHeader className="gap-1">
        <CardDescription>Personal balance sheet</CardDescription>
        <CardTitle className="text-2xl">Net Worth</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="rounded-lg bg-muted/50 px-5 py-6">
          <p className="text-sm text-muted-foreground">Current total</p>
          <h1 className="mt-2 text-4xl font-semibold tracking-tight">
            {networth === undefined ? 'Loading...' : `$${networth.toLocaleString()}`}
          </h1>
        </div>
      </CardContent>
    </Card>
  )
}

export default NetworthCard;
