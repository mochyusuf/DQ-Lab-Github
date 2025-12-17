import requests
resp = requests.get('https://storage.googleapis.com/dqlab-dataset/update.json', verify=False)

cov_id_raw = resp.json()