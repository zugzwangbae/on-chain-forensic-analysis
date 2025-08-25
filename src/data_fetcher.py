import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class BlckDataFetcher:
  def __init__(self):
    self.etherscan_api_key = os.getenv('ETHERSCAN_API_KEY')
    if not self.etherscan_api_key:
      print("Warning: ETHERSCAN_API_KEY not found in env variables.")

  def gte_etherscan_transaction(self, address, startblock=0, endblock=999999999, sort='asc'):
    base_ur="https://api.etherscan.io/api"
    params={
      'module': 'account',
      'action': 'txlist',
      'address': address,
      'startblock': startblock,
      'endblock': endblock,
      'sort': sort,
      'apikey': self.etherscan_api_key
    }

    try:
      response=requests.get(base_url, params=params)
      data=response.json()
      if data['status'] == '1':
        df=pd.DataFrame(data['result'])
        # convert wei to ETH and standardize column names
        df['value'] = (df['value'].astype(float) / 1e18).round(4)
        df['gasPrice'] = (df['gasPrice'].astype(float) / 1e9).round(2) # convert to Gwei
        df['timestamp'] = pd.to_datetime(df['timestamp'].astype(int), unit='s')
        return df
      else:
        print(f"Etherscan API Error: {data['message']}")
        return pd.DataFrame()
    expect requests.exceptions.RequestException as e:
      print(f"Request failed: {e}")
      return pd.DataFrame()

# Example usage for the notebook:
# fetcher = BlockchainDataFetcher()
# df_txs = fetcher.get_etherscan_transactions('0xSOME_WALLET_ADDRESS')
