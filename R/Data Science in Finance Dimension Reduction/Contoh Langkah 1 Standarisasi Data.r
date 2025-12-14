library(openxlsx)
df <- read.xlsx("https://storage.googleapis.com/dqlab-dataset/dqlab_pcadata.xlsx", sheet="3varb")

#standarisasi variabel (centering dan scaling)
df <- scale(df, center = TRUE, scale = TRUE)
head(df, 3)