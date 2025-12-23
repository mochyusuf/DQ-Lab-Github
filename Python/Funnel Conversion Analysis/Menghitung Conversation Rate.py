#membaca library
import pandas as pd

#membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')

#Hitung total users di setiap tahap funnel
total_funnel = df_merged[['view', 'click', 'add_to_cart', 'purchase']].sum()

#Hitung rasio konversi antar tahap funnel
conversion_rate = (total_funnel / total_funnel.shift(1)) *100
conversion_rate = conversion_rate[1:]  #Hapus nilai NaN pertama

print("\nConversion Rate antar tahap:")
print(conversion_rate)