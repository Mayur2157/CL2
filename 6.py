#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        soup = BeautifulSoup(plain, 'html.parser')
        product_name = []
        prices = []
        for link in soup.findAll('h3', {'class':'w-full'}):
            name = link.get_text(',')
            product_name.append(name)
        for link in soup.findAll('span', {'class':['whitespace-nowrap text-base font-bold override:opacity-100',
                                                   'whitespace-nowrap text-base text-puma-red font-bold']}):
            price = link.get_text(' ')
            prices.append(price)
    return product_name,prices

name,prices=web(1,'https://in.puma.com/in/en/collections/collections-football/collections-football-manchester-city-fc')

df = pd.DataFrame({'Product Name':name,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')
df

