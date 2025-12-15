# Import modul random
import random

# Set seed sebagai bilangan bulat 0, dan dapat diganti
# dengan bilangan bulat lainnya, sesuai dengan instruksi Senja
random.seed(1234)

# Ambil sampel dalam rentang butir data, yaitu 1 s/d 120
# Inisialisasi sampel
sampel = []
# Looping sebanyak sampel yang ingin ditarik yaitu 10% (12 butir data)
for i in range(12): 
    sampel.append(random.randint(1, 120))
# Cetaklah sampel
print("sampel:", sampel)