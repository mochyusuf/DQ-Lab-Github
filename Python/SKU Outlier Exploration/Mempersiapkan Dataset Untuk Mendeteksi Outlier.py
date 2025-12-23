#membaca library
import pandas as pd

#membaca dataset dari file csv
df_stock = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_stock.csv')
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')

#mengambil huruf pertama setiap kata
def get_initials(text):
    return ''.join([word[0] for word in text.split() if word[0].isalpha()])

#Membuat kode SKU pada kolom stock_id
df_product['stock_id'] = 'DQ-' + \
    df_product['product_category'].apply(get_initials) + '-' + \
    df_product['product_name'].apply(get_initials)

#menggabungkan dua dataset
df_merged = pd.merge(df_stock, df_product, on = 'product_id', how = 'left')

#memilih dataset yang digunakan
df_merged = df_merged[['stock_id', 'product_name', 'product_category', 'unit_sold']]

#menampilkan dataset
print(df_merged.head())