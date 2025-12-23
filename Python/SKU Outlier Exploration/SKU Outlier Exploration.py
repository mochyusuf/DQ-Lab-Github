#Import Library
import pandas as pd

#Membaca dataset dari CSV
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')

#mengambil huruf pertama setiap kata
def get_initials(text):
    return ''.join([word[0] for word in text.split() if word[0].isalpha()])

#Membuat kode SKU pada kolom stock_id
df_product['stock_id'] = 'DQ-' + \
    df_product['product_category'].apply(get_initials) + '-' + \
    df_product['product_name'].apply(get_initials)

#Menampilkan hasil
print(df_product)