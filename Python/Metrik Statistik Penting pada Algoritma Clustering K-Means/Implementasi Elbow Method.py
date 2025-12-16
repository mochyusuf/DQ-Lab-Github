#Import library pandas
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')

#Drop kolom customer_id
RFM_km = data.drop(["customer_id"], axis=1)

#Penerapan RobustScaler
from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
RFM_robust = robust_scaler.fit_transform(RFM_km)
RFM_robust = pd.DataFrame(RFM_robust)
RFM_robust.columns = ["Frequency","Recency","Monetary"]

#Import library Kmeans
from sklearn.cluster import KMeans

#Membuat variable SSE untuk menampung nilai WSS dari setiap nilai k 
SSE = []

#Melakukan k-means berulang dengan nilai k yang berbeda-beda dari 2 sampai 10
for k in range(2, 10):
    k_means = KMeans(n_clusters=k, random_state=0)
    model = k_means.fit(RFM_robust)
    SSE.append(k_means.inertia_)
	
#Mengkonversi hasil ke dalam data frame, kemudian menampilkannya dalam bentuk plot
import matplotlib.pyplot as plt
frame = pd.DataFrame({"Cluster":range(2,10), "SSE":SSE})
plt.figure(figsize=(8,5))
plt.plot(frame["Cluster"], frame["SSE"], marker="o")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()