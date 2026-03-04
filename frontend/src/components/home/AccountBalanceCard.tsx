import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

function AccountBalanceCard() {

  return (
      <Card className="w-full max-w-lg shadow-lg">
      <CardHeader className="gap-1">
        <CardTitle className="text-2xl">Account Name</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="rounded-lg bg-muted/50 px-5 py-6">
          <p className="text-sm text-muted-foreground">Current total</p>
          <h1 className="mt-2 text-4xl font-semibold tracking-tight">
          </h1>
        </div>
      </CardContent>
    </Card>
  )
}

export default AccountBalanceCard();
