#Import library pandas
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')

#Drop kolom customer_id
RFM_km = data.drop(["customer_id"], axis=1)

#Import library robust scaler
from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
RFM_robust = robust_scaler.fit_transform(RFM_km)
RFM_robust = pd.DataFrame(RFM_robust)
RFM_robust.columns = ["Frequency","Recency","Monetary"]

#Import library matplotlib.pyplot dan seaborn
import matplotlib.pyplot as plt
import seaborn as sns

#Menampilkan boxplot data frequency, recency, dan monetary
fig, ax = plt.subplots(3, 1, figsize=(8,5))
sns.boxplot(RFM_robust["Frequency"], ax=ax[0])
sns.boxplot(RFM_robust["Recency"], ax=ax[1])
sns.boxplot(RFM_robust["Monetary"], ax=ax[2])
plt.tight_layout()
plt.show()