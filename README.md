Title: Simple Stock Forecasting App

Description: This repository contains a simple Streamlit application that utilizes the Facebook Prophet library to forecast the stock prices of selected stocks. The app allows users to choose a stock, select the number of years for prediction, and displays a plot of the predicted stock prices. The stock data is fetched using the Yahoo Finance API.

To run the app locally, first install the required packages:
```
pip install streamlit yfinance fbprophet plotly
```

Then, run the app using Streamlit:
```
streamlit run app.py
```

The app should be accessible at `http://localhost:8501`.
