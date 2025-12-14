library(openxlsx)
df <- read.xlsx("https://storage.googleapis.com/dqlab-dataset/dqlab_pcadata.xlsx", sheet="3varb")
df <- scale(df, center = TRUE, scale = TRUE)
cormat <- cor(df)
eig <- eigen(cormat)

round(eig$values/ncol(df),3)
round(cumsum(eig$values/ncol(df)),3)

pr.out <- prcomp(df, scale. = TRUE, center = TRUE)
pr.out
summary(pr.out)

library(factoextra)

fviz_eig(pr.out, addlabels = TRUE)

screeplot(pr.out, type = "line")
abline(h = 1, lty = 3, col = "red")