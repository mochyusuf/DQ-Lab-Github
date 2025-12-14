library(openxlsx)

df <- read.xlsx("https://storage.googleapis.com/dqlab-dataset/dqlab_pcadata.xlsx", sheet="3varb")
df <- scale(df, center = TRUE, scale = TRUE)

cormat <- cor(df)
cormat