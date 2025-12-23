#membaca library
import pandas as pd
import matplotlib.pyplot as plt

#membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')

#Hitung total users di setiap tahap funnel
total_funnel = df_merged[['view', 'click', 'add_to_cart', 'purchase']].sum()

# Hitung drop-off absolut (selisih dari tahap sebelumnya)
dropoff = total_funnel.shift(1) - total_funnel
dropoff = dropoff[1:]  # hilangkan NaN di tahap pertama

#Hitung persentase drop-off dibandingkan tahap sebelumnya
dropoff_percentage = dropoff / total_funnel.shift(1)[1:] * 100

#Plot percentage drop-off
plt.figure(figsize = (8, 4))
dropoff_percentage.plot(kind = 'bar', color = 'skyblue')
plt.title('Percentage Drop-off per Funnel Stage')
plt.ylabel('Persentase Pengguna Hilang (%)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
