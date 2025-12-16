#Kode sebelumnya
import pandas as pd
import datetime

dataset_retail = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/data_retail.csv', delimiter=';')

dataset_retail['First_Transaction'] = pd.to_datetime(pd.to_datetime(dataset_retail['First_Transaction']/1000, unit='s', origin='1970-01-01')).dt.date
dataset_retail['Last_Transaction'] = pd.to_datetime(pd.to_datetime(dataset_retail['Last_Transaction']/1000, unit='s', origin='1970-01-01')).dt.date
dataset_retail.sort_values('First_Transaction', inplace=True)

daily_avg_trx = dataset_retail.groupby('First_Transaction').mean()['Average_Transaction_Amount'].reset_index()

train_data = daily_avg_trx['Average_Transaction_Amount'][:len(daily_avg_trx)-10]
test_data = daily_avg_trx['Average_Transaction_Amount'][len(daily_avg_trx)-10:]

from statsmodels.tsa.ar_model import AutoReg

ar_model = AutoReg(train_data, lags=10).fit()

#Membuat prediksi dengan model
pred = ar_model.predict(start=len(train_data), end=(len(train_data)+len(test_data)-1), dynamic=False).rename('AR Predictions')

#Plot
import matplotlib.pyplot as plt
pred.plot(legend=True)
test_data.plot(legend=True)
plt.xlabel('Urutan data First_Transaction ke-')
plt.tight_layout()
plt.show()