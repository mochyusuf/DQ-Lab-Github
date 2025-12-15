# Import pandas sebagai aliasnya yaitu
import pandas as pd

# Baca dataset
tinggi_badan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
print("Statistik deskriptif data awal:\n", tinggi_badan.describe().T)

# Modifikasi data maksimum tinggi badan menjadi 186 cm
tinggi_badan_mod = tinggi_badan.replace(tinggi_badan.max(), 186)
print("\nStatistik deskriptif data modifikasi:\n", tinggi_badan_mod.describe().T)

# Import matplotlib.pyplot dan seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
fig, axs = plt.subplots(2, 1, figsize=(12,8), sharex=True)
# Plot data awal
sns.boxplot(data=tinggi_badan, x="tinggi badan (cm)", whis=1.5, color="yellowgreen", ax=axs[0])
sns.swarmplot(data=tinggi_badan, x="tinggi badan (cm)", size=8, color="darkcyan", edgecolor=None, ax=axs[0])
axs[0].grid(axis="x")
axs[0].set_xlabel(None)
axs[0].set_title("Data awal", color="darkcyan", fontsize=16)

# Plot data modifikasi
sns.boxplot(data=tinggi_badan_mod, x="tinggi badan (cm)", whis=1.5, color="yellowgreen", ax=axs[1])
sns.swarmplot(data=tinggi_badan_mod, x="tinggi badan (cm)", size=8, color="darkcyan", edgecolor=None, ax=axs[1])
axs[1].grid(axis="x")
axs[1].set_xlabel(None)
axs[1].set_title("Data modifikasi", color="darkcyan", fontsize=16)

plt.xlabel("Tinggi badan (cm)", fontsize=14)
plt.tight_layout()
plt.show()