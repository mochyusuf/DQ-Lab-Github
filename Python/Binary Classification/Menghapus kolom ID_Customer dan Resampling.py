#Kode program sebelumnya
import pandas as pd
pd.set_option('display.max_column', 20)

df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/cth_churn_analysis_train.xlsx')

#menghilangkan kolom 'ID_Customer' dari data frame dikarenakan kolom ini tidak relevan untuk dijadikan input dalam tugas klasifikasi (ID customer tidak mempengaruhi apakah customer akan lanjut berlangganan atau tidak
df.drop('ID_Customer', axis=1, inplace=True)
print(df['churn'].value_counts())