# Import library Pandas
import pandas as pd

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

# Tampilkan tabel tersebut.
print(daily_df)
