import pandas as pd

# proses ekstraksi data 
data_trx = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.xlsx')

# proses agregasi data 
total_unit_terjual = data_trx.groupby(['trx_date', 'product_id'], as_index=False).agg(
    total_unit=('units', 'sum')
)

# Proses filter data
total_unit_terjual_produk019 = total_unit_terjual[total_unit_terjual['product_id'] == 'DQProduk-019']

# definisikan fungsi
def rolling_outlier(data, window_size): 
    data.sort_values(by=['trx_date'], inplace=True)
    data['q1'] = data['total_unit'].rolling(window=window_size).quantile(0.25)
    data['q3'] = data['total_unit'].rolling(window=window_size).quantile(0.75)
    data['iqr'] = data['q3'] - data['q1']
    data['lower_bound'] = data['q1'] - (1.5 * data['iqr'])
    data['upper_bound'] = data['q3'] + (1.5 * data['iqr'])

    # jika batas bawah negatif, ubah jadi 0
    data.loc[(data['lower_bound'].notnull()) & (data['lower_bound'] < 0), 'lower_bound'] = 0
    
    return data

# terapkan fungsi
total_unit_terjual_produk019 = rolling_outlier(
    data=total_unit_terjual_produk019, 
    window_size=8
)

# berikan kondisi
total_unit_terjual_produk019['flag_outlier'] = total_unit_terjual_produk019.apply(
    lambda row: 'Outlier' if row['total_unit'] < row['lower_bound'] or row['total_unit'] > row['upper_bound'] else 'Inlier',
    axis=1
)

# tampilkan hasilnya
print(total_unit_terjual_produk019.head(10))