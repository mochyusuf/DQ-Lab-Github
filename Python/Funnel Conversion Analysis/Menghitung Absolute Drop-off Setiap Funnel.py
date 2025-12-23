#membaca library
import pandas as pd

#membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')

#Hitung total users di setiap tahap funnel
total_funnel = df_merged[['view', 'click', 'add_to_cart', 'purchase']].sum()

#Hitung jumlah drop-off absolut
dropoff = total_funnel.shift(1) - total_funnel
dropoff = dropoff [1:]

print("\nDrop-off antar tahap:")
print(dropoff)