library(openxlsx)
df <- read.xlsx("https://storage.googleapis.com/dqlab-dataset/dqlab_pcadata.xlsx", sheet="3varb")
df <- scale(df, center = TRUE, scale = TRUE)

pr.out <- prcomp(df, scale. = TRUE, center = TRUE)

pr.out$rotation
biplot(pr.out, scale = 0)