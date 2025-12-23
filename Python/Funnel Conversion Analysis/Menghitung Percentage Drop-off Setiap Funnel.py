#membaca library
import pandas as pd

#membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')

#Hitung total users di setiap tahap funnel
total_funnel = df_merged[['view', 'click', 'add_to_cart', 'purchase']].sum()

# Hitung jumlah drop-off absolut (selisih dari tahap sebelumnya)
dropoff = total_funnel.shift(1) - total_funnel
dropoff = dropoff[1:]  # hilangkan NaN di tahap pertama

#Hitung persentase drop-off dibandingkan tahap sebelumnya
dropoff_percentage = dropoff / total_funnel.shift(1)[1:] * 100

print("\nPercentage Drop-off antar tahap:")
print(dropoff_percentage.round(2))