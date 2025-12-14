library(ggplot2)
library(hrbrthemes)
ggplot(data = new_cov_jabar, aes(x = tanggal, y = kasus_baru)) +
  geom_col()