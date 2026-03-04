import NetworthCard from "./NetworthCard"
import AccountBalances from "./AccountBalances"

function Home() {

  return (
    <main className="flex flex-col items-center justify-center bg-muted/30 px-6 py-10">
      <NetworthCard/>
      <AccountBalances/>
    </main>
  )
}

export default Home;
