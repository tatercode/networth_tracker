const BASE_URL = "http://127.0.0.1:8000/"

export async function getNetworth(): Promise<number> {
  const url = BASE_URL + "networth"
  const response = await fetch(url) 

  if (!response.ok) {
    console.error("Failed to get networth")
  }

  return response.json();
}
  
export async function getAllBalances(): Promise<Record<string, string>[]> {
  const url = BASE_URL + "account-balance"
  const response = await fetch(url)

  if (!response.ok) {
    console.error("Failed to get account balances")
  }

  return response.json();
}
