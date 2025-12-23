# Import library Pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Baca dataset “funnel.csv”
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/komdigi/tbl_funnel.csv")

# Agregasi tabel berdasarkan kolom date dan # Agregasi tabel berdasarkan kolom date dan jumlahkan metrik numerik lainnya kecuali sku_id menggunakan .groupby(), simpan hasil agregasi dalam variabel daily_df
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

# Hitung threshold click_velocity_rolling dari quantile ke-90 dan simpan dalam variabel cv_threshold
cv_threshold = daily_df['click_velocity_rolling'].quantile(0.90)

# Hitung threshold referral_entropy dari quantile ke-25 dan simpan dalam variabel entropy_threshold
entropy_threshold = daily_df['referral_entropy'].quantile(0.25)

# Buat kolom spike_flag_clicks yang berisi angka 1 jika click_velocity_rolling berada di atas threshold dan 0 jika berada di bawah threshold
daily_df['spike_flag_clicks'] = np.where(daily_df['click_velocity_rolling'] >  cv_threshold, 1, 0)

# Buat kolom spike_flag_entropy yang berisi angka 1 jika referral_entropy berada di bawah threshold dan 0 jika berada di atas threshold
daily_df['spike_flag_entropy'] = np.where(daily_df['referral_entropy'] < entropy_threshold, 1, 0)

# Buat kolom spike_flag yang berisi angka 1 jika dan hanya jika spike_flag_clicks dan spike_flag_entropy bernilai 1
daily_df['spike_flag'] = (
    (daily_df['spike_flag_clicks'] == 1) &
    (daily_df['spike_flag_entropy'] == 1)
).astype(int)

# Definisikan figure grafik dengan ukuran (18,6)
plt.figure(figsize=(18, 6))

# Plot grafik date vs click_velocity_rolling, berikan label 'Click Velocity Rolling' dan warna biru
plt.plot(daily_df['date'], daily_df['click_velocity_rolling'], label='Click Velocity Rolling', color='blue')

# Plot grafik date vs referral_entropy, berikan label ‘Referral Entropy’ dan warna hijau
plt.plot(daily_df['date'], daily_df['referral_entropy'], label='Referral Entropy', color='green')

# Definisikan daftar tanggal yang spike_flag = 1 dan simpan dalam variabel spike_dates
spike_dates = daily_df[daily_df['spike_flag'] == 1]['date']

# Plot area pada grafik yang terdapat spike_flag = 1 untuk grafik date vs click_velocity_rolling dan grafik date vs referral_entropy
plt.plot(spike_dates, daily_df[daily_df['spike_flag'] == 1]['click_velocity_rolling'], 'ro', markersize=5, label='Spike Candidate (Quantile) - CV', alpha=0.7)
plt.plot(spike_dates, daily_df[daily_df['spike_flag'] == 1]['referral_entropy'], 'ro', markersize=5, alpha=0.7)

# Berikan nama pada: sumbu X sebagai ‘Date’; sumbu Y sebagai ‘value’, dan judul sebagai ‘Click Velocity Rolling and Referral Entropy Over Time with Spike Flag (Quantile Method)’
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Click Velocity Rolling and Referral Entropy Over Time with Spike Flag (Quantile Method)')

# Munculkan legend
plt.legend()

# Tampilkan keseluruhan grafik tersebut.
plt.show()
