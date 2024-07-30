import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

def load_data(symbol, db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    query = f"SELECT * FROM {symbol}_data"
    data = pd.read_sql(query, engine)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

def perform_analysis(data):
    
    data['Daily_Return'] = data['Close'].pct_change()
    
    
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    
    
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close')
    plt.plot(data.index, data['MA50'], label='50-day MA')
    plt.plot(data.index, data['MA200'], label='200-day MA')
    plt.title('Stock Price with Moving Averages')
    plt.legend()
    plt.savefig('app/static/price_ma_plot.png')
    plt.close()
    
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Daily_Return'].dropna(), kde=True)
    plt.title('Distribution of Daily Returns')
    plt.savefig('app/static/returns_dist.png')
    plt.close()

if __name__ == "__main__":
    symbol = "AAPL"
    db_path = "data/finance_data.db"
    
    stock_data = load_data(symbol, db_path)
    perform_analysis(stock_data)
    print("Analysis completed and plots saved.")