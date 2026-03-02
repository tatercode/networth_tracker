const BASE_URL = "http://127.0.0.1:8000/"

export async function getNetworth(): Promise<number> {
  const url = BASE_URL + "networth"
  const response = await fetch(url) 

  if (!response.ok) {
    console.error("Failed to get networth")
  }

  return response.json();
}
  
