import pandas as pd
import random
from datetime import datetime, timedelta

def generate_browsing_history(users, products, num_browsing_events):
    browsing_data = []
    for user in users:
        for _ in range(num_browsing_events):
            product = random.choice(products)
            date = datetime.now() - timedelta(days=random.randint(1, 365))
            browsing_data.append({'User_ID': user, 'Product_ID': product, 'Date': date})
    return pd.DataFrame(browsing_data)

def generate_purchase_history(users, products, max_purchase_events_per_user):
    purchase_data = []
    for user in users:
        num_purchase_events = random.randint(1, max_purchase_events_per_user)
        for _ in range(num_purchase_events):
            product = random.choice(products)
            date = datetime.now() - timedelta(days=random.randint(1, 365))
            purchase_data.append({'User_ID': user, 'Product_ID': product, 'Date': date})
    return pd.DataFrame(purchase_data)

num_users = 10000
users = ['User_' + str(i) for i in range(1, num_users + 1)]

num_products = 200
products = ['Product_' + str(i) for i in range(1, num_products + 1)]

num_browsing_events = 1000  
browsing_history = generate_browsing_history(users, products, num_browsing_events)

max_purchase_events_per_user = 50 
purchase_history = generate_purchase_history(users, products, max_purchase_events_per_user)

browsing_history.to_csv('browsing_history.csv', index=False)
purchase_history.to_csv('purchase_history.csv', index=False)




