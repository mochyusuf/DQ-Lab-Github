#membaca library
import pandas as pd

#membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')

#Hitung total users di setiap tahap funnel
total_funnel = df_merged[['view', 'click', 'add_to_cart', 'purchase']].sum()
print("Jumlah total users di setiap tingkatan funnel:")
print(total_funnel)