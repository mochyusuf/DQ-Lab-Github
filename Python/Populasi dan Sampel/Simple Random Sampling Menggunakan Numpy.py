# Import numpy sebagai aliasnya np
import numpy as np

# Set seed sebagai bilangan bulat 0, dan dapat diganti
# dengan bilangan bulat lainnya
np.random.seed(0)

# Ambil sampel dalam rentang butir data, yaitu 1 s/d 120,
# sebanyak 10% (12 butir data)
sampel = np.random.randint(1, 121, size=12)
# Cetaklah sampel
print("sampel:", sampel)