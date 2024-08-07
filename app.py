from flask import Flask, render_template
from scripts.visualization import create_candlestick_chart, load_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/candlestick')
def candlestick():
    symbol = "AAPL"
    db_path = "data/finance_data.db"
    stock_data = load_data(symbol, db_path)
    chart = create_candlestick_chart(stock_data)
    return chart.to_html(full_html=False)

if __name__ == '__main__':
    app.run(debug=True)