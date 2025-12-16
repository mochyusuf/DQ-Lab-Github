#Kode program sebelumnya
import pandas as pd
pd.set_option('display.max_column', 20)

df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/cth_churn_analysis_train.xlsx')
df.drop('ID_Customer', axis=1, inplace=True)

#menyimpan kolom 'churn' sebagai list ke dalam variabel y
y = df.pop('churn').to_list()

#mengubah nilai 'Yes' menjadi 1 dan nilai 'No' menjadi 0 agar sesuai dengan format yang sebelumnya telah kita bahas
y = [1 if label == 'Yes' else 0 for label in y]
print(df.head())