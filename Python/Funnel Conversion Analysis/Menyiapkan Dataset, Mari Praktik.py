# membaca library
import pandas as pd

# membaca dataset
df_funnel = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')

# menggabungkan dua dataset
df_merged = pd.merge(df_funnel, df_product, on='product_id', how='left')

# pilih kolom yang ada saja (hindari KeyError)
kolom_dipakai = [col for col in [
    'date', 'product_id', 'product_name', 'product_category',
    'purchase', 'add_to_cart', 'click', 'view'
] if col in df_merged.columns]

df_merged = df_merged[kolom_dipakai]

# menampilkan dataset
print(df_merged.head())