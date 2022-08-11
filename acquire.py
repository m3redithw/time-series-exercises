#Import dependencies
import pandas as pd
import requests

def get_items():
    
    base_url = 'https://python.zgulde.net'
    
    response = requests.get('https://python.zgulde.net/api/v1/items')
    
    data = response.json()
    
    items = pd.DataFrame(data['payload']['items'])
    
    next_page = data['payload']['next_page']
    
    while next_page != None:
        
        response = requests.get(base_url + next_page)
        
        data = response.json()
        
        next_page = data['payload']['next_page']
        
        new_items = pd.DataFrame(data['payload']['items'])
        
        items = pd.concat([items, new_items])
    
    items.reset_index(drop=True, inplace=True)
    
    #items.to_csv('items.csv')
    
    return items

def get_sales():
    
    base_url = 'https://python.zgulde.net'
    
    response = requests.get('https://python.zgulde.net/api/v1/sales')
    
    data = response.json()
    
    items = pd.DataFrame(data['payload']['sales'])
    
    next_page = data['payload']['next_page']
    
    while next_page != None:
        
        response = requests.get(base_url + next_page)
        
        data = response.json()
        
        next_page = data['payload']['next_page']
        
        new_items = pd.DataFrame(data['payload']['sales'])
        
        items = pd.concat([items, new_items])
    
    items.reset_index(drop=True, inplace=True)
    
    items.to_csv('sales.csv')
    
    return items

def get_whole_sales():
    df = pd.read_csv('complete_sale.csv')
    return df

def get_ops_data():
    if os.path.exists('opsd.csv'):
        return pd.read_csv('opsd.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('opsd.csv', index=False)
    return df
