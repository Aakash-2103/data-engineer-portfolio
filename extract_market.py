import requests
import pandas as pd
from datetime import datetime
from config import MARKET_STACK_API_KEY  # Fixed name

def extract_market_data(symbols, limit=100):
    BASE_URL = "https://api.marketstack.com/v1/eod"
    params = {
        'access_key': MARKET_STACK_API_KEY,
        'symbols': ','.join(symbols),
        'limit': limit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    print(data)

    if 'data' not in data or not data['data']:
       raise Exception(f"API ERROR: {data}")

    df = pd.json_normalize(data['data'])
    file_name = f"raw_stock_data_{datetime.now().strftime('%Y%m%d%H%M')}.csv"
    df.to_csv(file_name, index=False)
    print(f"Extracted data saved to {file_name}")
    return file_name

if __name__ == "__main__":
    extract_market_data(["AAPL", "MSFT", "GOOG"])  # Fixed tuple to list
