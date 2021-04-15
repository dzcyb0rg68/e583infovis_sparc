import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from forex_python.converter import CurrencyRates
import datetime

import subprocess
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Reads the data from SPARC
data = pd.read_csv('data/bigdeal.csv')

# Generates a csv file that stores currency values ['USD', 'GBP', 'EUR', 'CAD']
currency = pd.DataFrame({'Currency':['USD', 'GBP', 'EUR', 'CAD']})
currency.to_csv('data/currency.csv')

# Generates currency conversion table to currency_rate.csv
currency_list = list(currency['Currency'].unique())
year_dict = {}
year_list = list(np.sort(data['years'].unique())) 
year_dict['year'] = year_list
df = pd.DataFrame(data=year_dict)
c = CurrencyRates()

for cur in currency_list:
    for y in year_list:
        time_obj = datetime.datetime(y, 1, 1, 00, 00, 00, 00000)
        df.loc[df['year'] == y, cur] = c.get_rate('USD', cur, time_obj)
        
df.to_csv('data/currency_rate.csv')

# Gets laditude and longitude information from Google (web scrapping) then exports as data.csv
institution_list = data['institution'].unique()

data['Latitude'] = 'None'
data['Longitude'] = 'None'
i = 1
for institute in institution_list:
    ins_decode = institute.encode('utf-8').decode('ascii', 'ignore')
    url = f'https://www.google.com/search?q={ins_decode} coordinates'.replace('&', ' ').replace(' ', '+')
    req = Request(url,headers={'User-Agent': 'Chrome'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, 'html5lib')
    location = soup.find("div", class_='BNeawe').text.encode('utf-8').decode('ascii', 'ignore')
    cor = str(location).split(', ')
    try:
        data.loc[(data['institution'] == institute), 'Latitude'] = cor[0]
        data.loc[(data['institution'] == institute), 'Longitude'] = cor[1]
    except (IndexError, UnicodeEncodeError):
        data.loc[(data['institution'] == institute), 'Latitude'] = None
        data.loc[(data['institution'] == institute), 'Longitude'] = None

data.to_csv('data/data.csv')