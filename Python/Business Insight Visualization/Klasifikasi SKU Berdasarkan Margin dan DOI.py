# Import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/margin_doi.csv')

# ======== VISUALISASI ========= #
sns.set(style="whitegrid")
plt.figure(figsize=(14, 9))

# Scatter plot
scatter = sns.scatterplot(
    data = df,
    x = 'doi',
    y = 'margin',
    hue = 'sku_category',
    size = 'unit_sold',
    sizes = (50, 300),
    palette = 'Set2',
    alpha = 0.8,
    edgecolor = 'black'
)
# Hitung kuartil
margin_q = df['margin'].quantile([0.25, 0.5, 0.75])
doi_q = df['doi'].quantile([0.25, 0.5, 0.75])

# Garis kuartil
plt.axhline(margin_q[0.25], color = 'red', linestyle = '--', linewidth = 1) 
plt.axhline(margin_q[0.75], color = 'red', linestyle = '--', linewidth = 1)
plt.axvline(doi_q[0.25], color = 'blue', linestyle = '--', linewidth = 1)
plt.axvline(doi_q[0.75], color = 'blue', linestyle = '--', linewidth=1)

# Tambahkan label nama produk di setiap titik
for i, row in df.iterrows():
    if not pd.isna(row['doi']) and not pd.isna(row['margin']):
        plt.text(row['doi'] + 1, row['margin'], row['product_name'], 
                 fontsize = 8, alpha = 0.7)

# Label dan layout
plt.title('Klasifikasi SKU Berdasarkan Margin dan DOI (Oktober)', fontsize = 16)
plt.xlabel('Days of Inventory (DOI)')
plt.ylabel('Margin (%)')
plt.legend(title = 'Kategori SKU', bbox_to_anchor=(1.05, 1), loc = 'upper left')
plt.tight_layout()

# Tampilkan
plt.show()