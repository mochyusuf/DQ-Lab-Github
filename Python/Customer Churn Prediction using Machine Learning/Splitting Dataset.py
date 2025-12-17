import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco_final.csv')
cleaned_df = df_load.drop(['customerID','UpdatedAt'], axis=1)

for column in cleaned_df.columns:
    if cleaned_df[column].dtype == np.number: continue
    cleaned_df[column] = LabelEncoder().fit_transform(cleaned_df[column])

from sklearn.model_selection import train_test_split
# Predictor dan target
X = cleaned_df.drop('Churn', axis = 1)
Y = cleaned_df['Churn']
# Splitting train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
# Print according to the expected result
print('Jumlah baris dan kolom dari X_train adalah:', X_train.shape,', sedangkan Jumlah baris dan kolom dari Y_train adalah:', Y_train.shape)
print('Prosentase Churn di data Training adalah:')
print(Y_train.value_counts(normalize=True))
print('Jumlah baris dan kolom dari X_test adalah:', X_test.shape,', sedangkan Jumlah baris dan kolom dari Y_test adalah:', Y_test.shape)
print('Prosentase Churn di data Testing adalah:')
print(Y_test.value_counts(normalize=True))