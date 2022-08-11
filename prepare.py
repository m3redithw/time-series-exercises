import pandas as pd

import requests

from imports import *

def prep_sales(df):
    # Drop meaningless columns
    df = df.drop(columns = 'Unnamed: 0')
    
    # Convert date to datatime object
    df['sale_date'] = pd.to_datetime(df['sale_date'], infer_datetime_format=True)
    
    # Set date as index
    df.set_index('sale_date', inplace=True)
    # Sort index
    df.sort_index(inplace=True)
    
    # Create month, day_of_week columns
    df['month'] = df.index.strftime('%b')
    df['day_of_week'] = df.index.strftime('%A')
    
    # Create sales total
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df

def prep_ops(df):
    # Change date to datetime object
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    
    # Set the sale_date column as the index
    df.set_index('Date', inplace=True)
    
    # Create column for month
    df['Month'] = df.index.strftime('%b')
    # Create column for yaer
    df['Year'] = df.index.strftime('%Y')
    
    # Fill missing values
    # Replace Wind missing value with mean
    df = df.fillna({"Wind":0})
    # Replace Solar missing value with mean
    df = df.fillna({"Solar":0})
    # Replace Wind + Solar missing value with Wind + Solar
    df = df.fillna({"Wind+Solar":(df.Wind + df.Solar)})
    
    return df