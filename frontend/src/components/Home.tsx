import { useState, useEffect } from 'react';
import { getNetworth } from '../services/balances';



function Home() {

  const [networth, setNetworth] = useState<number | undefined>();
  
  useEffect(() => {

    async function loadNetWorth() {
      const value = await getNetworth();
      setNetworth(value);
    }

    loadNetWorth();
    
  }, [])

  return (
    <>
      <h1>{networth}</h1>
    </>

  )

}

export default Home;
