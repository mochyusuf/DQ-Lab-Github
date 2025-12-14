library(httr)
set_config(config(ssl_verifypeer = 0L))
resp <- GET("https://storage.googleapis.com/dqlab-dataset/update.json")
cov_id_raw <- content(resp, as = "parsed", simplifyVector = TRUE)