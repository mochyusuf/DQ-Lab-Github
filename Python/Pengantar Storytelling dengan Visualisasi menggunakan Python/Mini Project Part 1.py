#Import library pandas
import pandas as pd
pd.set_option('display.max_column', 10)

#Membaca dan menampilkan dataset
dataset_worldbank = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/atmajaya/worldbank.csv', delimiter=',', encoding='cp1252')

#Melihat tipe data database worldbank.csv
print('\nInformasi dataset_worldbank:')
print('============================')
dataset_worldbank.info()

#Mengganti baris data yang kosong dengan nilai 0
dataset_worldbank = dataset_worldbank.fillna(0)

#Melihat tipe data database worldbank.csv
print('\nInformasi dataset_worldbank setelah .fillna(0):')
print('===============================================')
dataset_worldbank.info()

#Data worldbank dari tahun ... sampai tahun ...
print('\nData worldbank dari tahun ... sampai tahun ...')
print('==============================================')
print(dataset_worldbank['year'].unique())