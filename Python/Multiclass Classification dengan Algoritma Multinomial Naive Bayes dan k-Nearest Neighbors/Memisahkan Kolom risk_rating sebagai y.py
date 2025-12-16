#Kode program sebelumnya
import pandas as pd
pd.set_option('display.max_column', 20)

df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/credit_scoring_dqlab.xlsx')
df.drop('kode_kontrak', axis=1, inplace=True)

#memeriksa rasio kemunculan label
print('Rasio kemunculan  label:')
print(pd.concat([df['risk_rating'].value_counts(), 100*df['risk_rating'].value_counts(normalize=True).rename('percentage_risk_rating')], axis=1))

#menyimpan kolom 'rating' sebagai list ke dalam variabel y
y = df.pop('risk_rating').to_list()
 
#untuk setiap label jika nilai label = 5 maka kembalikan nilai 4
y = [4 if label == 5 else label for label in y]
 
#mengubah tipe data dari array y menjadi numpy array hal ini dikarenakan beberapa fungsi library scikit-learn hanya kompatibel terhadap numpy array
import numpy as np
y = np.array(y)

print('\nDataset:')
print(df.head())