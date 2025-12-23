#Import Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Membaca dataset
df_funnel = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_funnel.csv')
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')
 
# Menggabungkan dua dataset
df_merged = pd.merge(df_funnel, df_product, on='product_id', how='left')
 
# Hitung total users di setiap tahap funnel
total_funnel = df_merged[['view', 'click', 'add_to_cart', 'purchase']].sum()
 
# Urutkan tahap dari atas ke bawah funnel
stages = total_funnel.index.tolist()
values = total_funnel.values.tolist()
 
# Warna gradasi
colors = sns.color_palette("Blues", len(stages))[::-1]
 
plt.figure(figsize=(8, 5))
for i, (stage, value) in enumerate(zip(stages, values)):
	plt.barh(stage, value, color=colors[i], edgecolor="black")
	
	# Hitung persentase dari tahap awal
	percent = f"{value/values[0]*100:.1f}%"
	
	# Teks di luar bar (kanan)
	plt.text(value + max(values)*0.01, i, percent, va='center', ha='left',
             color='black', fontsize=11, fontweight='bold')
             
plt.gca().invert_yaxis()
plt.title("Funnel Conversion Chart", fontsize=14, fontweight='bold')
plt.xlabel("Jumlah Users")
plt.tight_layout()
plt.show()