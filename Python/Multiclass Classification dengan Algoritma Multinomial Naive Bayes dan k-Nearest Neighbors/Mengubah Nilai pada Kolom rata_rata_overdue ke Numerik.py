#Kode program sebelumnya
import numpy as np
import pandas as pd
pd.set_option('display.max_column', 20)

df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/credit_scoring_dqlab.xlsx')
df.drop('kode_kontrak', axis=1, inplace=True)

y = df.pop('risk_rating').to_list()
y = [4 if label == 5 else label for label in y]
y = np.array(y)

def convert_kpr_aktif(kpr_aktif):
    if kpr_aktif == 'YA':
        return 1
    return 0

df['kpr_aktif']= df['kpr_aktif'].apply(convert_kpr_aktif)

#rasio kemunculan setiap kategori rata_rata_overdue
print('Rasio kemunculan  setiap kategori rata_rata_overdue:')
print(pd.concat([df['rata_rata_overdue'].value_counts(), 100*df['rata_rata_overdue'].value_counts(normalize=True).rename('percentage_rata_rata_overdue')], axis=1))

#fungsi untuk mengubah nilai dari kolom 'rata_rata_overdue'
def change_overdue(overdue):
	if overdue == '0 - 30 days':
		return 0
	elif overdue == '31 - 45 days':
		return 1
	elif overdue == '46 - 60 days':
		return 2
	elif overdue == '61 - 90 days':
		return 3
	else:
		return 4
	
#mengaplikasikan fungsi pada kolom 'rata_rata_overdue'
df['rata_rata_overdue'] = df['rata_rata_overdue'].apply(change_overdue)

print("\nLima baris dataset teratas:")
print(df.head())