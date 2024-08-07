This project is a web application for analyzing and visualizing financial market data. It fetches stock data from Yahoo Finance, performs analysis, and presents interactive visualizations.

 Features:
- ETL pipeline for fetching and storing financial data
- Data analysis including moving averages and daily returns calculations
- Interactive visualizations with candlestick charts and distribution plots
- Flask web application to serve the analysis and visualizations

Prerequisites:
- Python 3.7+
- pip (Python package installer)
- Git

Installation:
1. Clone the repository
2. Create and activate a virtual environment: 
(python3 -m venv venv
source venv/bin/activate  (On Windows use venv\Scripts\activate))
3. Install required packages: pip install -r requirements.txt

Usage:
1. Run the ETL script to fetch and store data
2. Run the analysis script
3. Generate visualizations
4. Start the Flask application (flask run)
5. Open a web browser and go to `http://127.0.0.1:5000/`

Customization:
- To analyze a different stock, modify the `symbol` variable in `scripts/etl.py`, `scripts/analysis.py`, and `app.py`.
- Adjust the date range by modifying `start_date` and `end_date` in `scripts/etl.py`.

Project Structure:
- `scripts/etl.py`: Fetches data from Yahoo Finance and stores it in SQLite database
- `scripts/analysis.py`: Performs data analysis and generates static plots
- `scripts/visualization.py`: Creates interactive Plotly visualizations
- `app.py`: Flask application serving the web interface
- `app/templates/index.html`: HTML template for the web interface


