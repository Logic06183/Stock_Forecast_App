import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import numpy as np
import pandas as pd

START = "2018-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('AAPL', 'MSFT')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 2)
period = n_years * 365

st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

def plot_forecast(model, stock, forecast):
    fig = plot_plotly(model, forecast)
    fig.update_layout(
        title=f"{stock} Stock Forecast",
        xaxis_title="Date",
        yaxis_title="Close Price",
        showlegend=False
    )
    st.plotly_chart(fig)

data = load_data(selected_stock)
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

plot_forecast(m, selected_stock, forecast)

