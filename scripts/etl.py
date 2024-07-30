import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

def fetch_financial_data(symbol, start_date, end_date):
    asset = yf.Ticker(symbol)
    data = asset.history(start=start_date, end=end_date)
    return data

def save_to_database(data, table_name, db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    data.to_sql(table_name, engine, if_exists='replace', index=True)

if __name__ == "__main__":
    symbol = "AAPL"  
    start_date = "2020-01-01"
    end_date = "2023-12-31"
    db_path = "data/finance_data.db"
    
    financial_data = fetch_financial_data(symbol, start_date, end_date)
    save_to_database(financial_data, f"{symbol}_data", db_path)
    print(f"Data for {symbol} saved to database.")