library(httr)
set_config(config(ssl_verifypeer = 0L))
resp <- GET("https://storage.googleapis.com/dqlab-dataset/update.json")

resp$status_code
identical(resp$status_code, status_code(resp))