#Kode program sebelumnya
import pandas as pd
pd.set_option('display.max_column', 20)

df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/cth_churn_analysis_train.xlsx')
df.drop('ID_Customer', axis=1, inplace=True)
df.drop('harga_per_bulan', axis=1, inplace=True)
df.drop('jumlah_harga_langganan', axis=1, inplace=True)

y = df.pop('churn').to_list()
y = [1 if label == 'Yes' else 0 for label in y]

from sklearn.preprocessing import LabelEncoder
labelers = {}
column_categorical_non_binary = []
for col in df.select_dtypes(include=['object']):
    if len(df[col].unique()) == 2:
        labelers[col] = LabelEncoder()
        df[col] = labelers[col].fit_transform(df[col])
    else:
        column_categorical_non_binary.append(col)

df = pd.get_dummies(df, columns=column_categorical_non_binary)

X = df.to_numpy()

#library yang akan kita gunakan untuk membagi dataset
from sklearn.model_selection import train_test_split
 
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=23)
 
print("Dimensi data X mula-mula:", X.shape)
print("Dimensi data y mula-mula:",len(y),"\n")
 
print("Dimensi data X train:", X_train.shape)
print("Dimensi data y train:", len(y_train),"\n")
 
print("Dimensi data X test:", X_test.shape)
print("Dimensi data y test:", len(y_test),"\n")