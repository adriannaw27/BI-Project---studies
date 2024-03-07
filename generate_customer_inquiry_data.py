import pandas as pd
import random
from datetime import datetime, timedelta

def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime.now()
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_inquiry_category():
    inquiry_categories = [
        'order', 'product', 'shipping', 'refund', 'stock', 
        'customer_satisfaction', 'cancellation', 'discount', 'complaint', 
        'return', 'other', 'collaboration', 'missing_product', 'missing_shipment'
    ]
    return random.choice(inquiry_categories)

def generate_inquiries_count():
    return random.randint(1, 100)

def generate_customers_count(inquiries_count):
    return round(random.uniform(0.8, 1) * inquiries_count)

def generate_daily_aggregated_NPS(inquiry_category):
    if inquiry_category in ['complaint', 'missing_product', 'missing_shipment']:
        return random.randint(30, 70)
    else:
        return random.randint(55, 80)

data = []
for _ in range(100000):
    date = generate_random_date().strftime('%Y-%m-%d')
    inquiry_category = generate_inquiry_category()
    inquiries_count = generate_inquiries_count()
    customers_count = generate_customers_count(inquiries_count)
    daily_aggregated_NPS = generate_daily_aggregated_NPS(inquiry_category)
    data.append([date, inquiry_category, inquiries_count, customers_count, daily_aggregated_NPS])

df = pd.DataFrame(data, columns=['date', 'inquiry_category', 'inquiries_count', 'customers_count', 'daily_aggregated_NPS'])

df.to_csv('daily_customer_inquiries_data.csv', index=False)

