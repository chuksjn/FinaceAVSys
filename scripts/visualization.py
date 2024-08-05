import pandas as pd
import plotly.graph_objs as go
from sqlalchemy import create_engine

def load_data(symbol, db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    query = f"SELECT * FROM {symbol}_data"
    data = pd.read_sql(query, engine)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def create_candlestick_chart(data):
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
    fig.update_layout(title='Stock Price Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price')
    return fig

if __name__ == "__main__":
    symbol = "AAPL"
    db_path = "data/finance_data.db"
    
    stock_data = load_data(symbol, db_path)
    candlestick_chart = create_candlestick_chart(stock_data)
    candlestick_chart.write_html("app/templates/candlestick.html")
    print("Interactive visualization created.")