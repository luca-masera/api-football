
import requests #vado a stampare la libreria con pip install requests

API_KEY = 'a7a65c15b993bf511bbbc57ec6671322'

#dizionario di coppie chiave valore
headers = {
    "x-apisports-key": API_KEY
}

#nell'url salvo il sito per le chiamate
base_url = "https://v3.football.api-sports.io/"

endpoint = "status"

url = f"{base_url}{endpoint}"
print(url)

response = requests.request("GET", url, headers=headers)
print(response.status_code)