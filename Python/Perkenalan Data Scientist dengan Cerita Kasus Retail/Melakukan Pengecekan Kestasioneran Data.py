#Kode sebelumnya
import pandas as pd
import datetime

dataset_retail = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/data_retail.csv', delimiter=';')

dataset_retail['First_Transaction'] = pd.to_datetime(pd.to_datetime(dataset_retail['First_Transaction']/1000, unit='s', origin='1970-01-01')).dt.date
dataset_retail['Last_Transaction'] = pd.to_datetime(pd.to_datetime(dataset_retail['Last_Transaction']/1000, unit='s', origin='1970-01-01')).dt.date
dataset_retail.sort_values('First_Transaction', inplace=True)

daily_avg_trx = dataset_retail.groupby('First_Transaction').mean()['Average_Transaction_Amount'].reset_index()

#Mengimpor library adfuller
from statsmodels.tsa.stattools import adfuller

#Mengecek stationary data
df_stationarityTest = adfuller(daily_avg_trx['Average_Transaction_Amount'])
print("p-value: ", df_stationarityTest[1])