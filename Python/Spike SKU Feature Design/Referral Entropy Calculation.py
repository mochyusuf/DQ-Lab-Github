# Import library Pandas
import pandas as pd
import numpy as np

# Baca dataset “funnel.csv”
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/komdigi/tbl_funnel.csv")

# Agregasi tabel berdasarkan kolom date dan jumlahkan metrik numerik lainnya kecuali sku_id menggunakan .groupby(), simpan hasil agregasi dalam variabel daily_df
daily_df = df.groupby ('date').sum(numeric_only=True).reset_index()

# Lakukan perhitungan click velocity pada kolom clicks, kemudian simpan hasilnya pada kolom baru bernama click_velocity
daily_df['click_velocity'] = daily_df['clicks'].pct_change()

# Lakukan perhitungan untuk rolling mean selama 7 hari
daily_df['rolling_mean_click'] = daily_df['clicks'].shift(1).rolling(window=7, min_periods=1).mean()

# Lakukan perhitungan untuk click velocity harian
daily_df['click_velocity_rolling'] = daily_df['clicks'] / daily_df['rolling_mean_click']

# Mendefinisikan fungsi perhitungan entropy
def calculate_entropy(clicks_series):
    total_clicks = clicks_series.sum()
    if total_clicks == 0:
        return 0
    probabilities = clicks_series / total_clicks
    entropy = -np.sum(probabilities * np.log2(probabilities + 0.0000001))
    return entropy

# Definisikan nama dari kolom-kolom yang berisi informasi sumber referral dan masukkan ke dalam list yang disimpan sebagai variabel click_source_columns
click_source_columns = ['direct_clicks', 'google_clicks', 'ads_clicks', 'email_clicks', 'instagram_clicks']

# Gunakan fungsi yang tadi sudah didefinisikan, aplikasikan pada kolom-kolom yang mengandung informasi sumber referral. Hasilnya disimpan dalam kolom baru yang dinamakan referral_entropy
daily_df['referral_entropy'] = daily_df[click_source_columns].apply(lambda X: calculate_entropy(X.to_numpy()), axis=1)

# Tampilkan tabel tersebut.
print(daily_df)
