import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sales(stock, date, price):
    base_sales = random.randint(30, 50)  
    seasonal_factor = 1 + np.sin((date.month - 1) * 2 * np.pi / 12) * 0.2 
    trend_factor = 1 + 0.05 * (date.year - 2023)  
    price_effect = 1 + (price - 50) / 100  
    return int(base_sales * seasonal_factor * trend_factor * price_effect)

def generate_item_id():
    return ''.join(random.choices('abcd0123456789', k=6))

def generate_sales_and_inventory_data(item_id):

    data = []

    start_date = datetime(2023, 1, 1)
    end_date = datetime.now()

    stock = 1000

    current_date = start_date
    while current_date <= end_date:
        price = random.randint(35, 100) 
        sales = generate_sales(stock, current_date, price)
        if current_date.day == 1:  
            stock += 2000
        data.append([current_date.strftime('%Y-%m-%d'), item_id, price, sales, stock])
        stock -= sales
        current_date += timedelta(days=1)

    df = pd.DataFrame(data, columns=['date', 'item_id', 'price', 'sales', 'stock'])
    return df

dfs = []

for _ in range(10):
    item_id = generate_item_id()
    df = generate_sales_and_inventory_data(item_id)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

combined_df.to_csv('3_sales_and_inventory_data.csv', index=False)
