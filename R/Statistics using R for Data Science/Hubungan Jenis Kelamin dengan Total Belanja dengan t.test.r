## carilah boxplot antara variabel jenis kelamin dengan total belanja
# carilah boxplot antara variabel jenis kelamin dengan total belanja
boxplot(Total~Jenis.Kelamin, data = data_intro)

# Analisis bagaimana hubungan jenis kelamin dengan total belanja mengunakan uji statistik t-test
t.test(Total~Jenis.Kelamin, data = data_intro)