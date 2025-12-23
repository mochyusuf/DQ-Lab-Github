#memanggil library
import matplotlib.pyplot as plt
import pandas as pd

#membuat contoh dataset sederhana
data = {
    'Periode': [
        '201609', '201610', '201611', '201612', '201701', '201702', '201703', '201704', '201705', '201706', '201707',
        '201708', '201709', '201710', '201711', '201712', '201801', '201802', '201803', '201804', '201805', '201806',
        '201807', '201808', '201809'
    ],
    'Jumlah': [
        120, 230, 90, 450, 60, 70, 65, 55, 60, 58, 70,
        1000, 270, 310, 290, 220, 350, 180, 200, 190, 170, 160,
        210, 950, 180
    ]
}

#merubah kedalam tabel dan menyesuaikan format
df = pd.DataFrame(data)
df['Periode'] = pd.to_datetime(df['Periode'], format='%Y%m')

#membuat grafik line chart
plt.figure(figsize = (12, 6))
plt.plot(df['Periode'], df['Jumlah'], marker = 'o', color = 'green', linewidth = 2)
spike_indices = [11, 23]  
for i in spike_indices:
    plt.plot(df['Periode'][i], df['Jumlah'][i], 'o', markersize = 15,
             markerfacecolor = 'none', markeredgecolor = 'blue', markeredgewidth = 2)
plt.grid(True, linestyle = '--', alpha = 0.6)
plt.title('Tren Jumlah per Periode', fontsize = 14)
plt.xlabel('Periode')
plt.ylabel('Jumlah')
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()