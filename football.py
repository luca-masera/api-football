
import requests #vado a installare la libreria con pip install requests
import json # importo json per visionario il dizionario in modo più chiaro

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

# restituisce un JSON
print(response.text)

# converto il file json in un dizionario Python
d= response.json()
print(type(d))

# serializzo, memorizzo i dati in una stringa
print(json.dumps(d, indent=4))

#faccio la chiamata all.endpoin countries
endpoint = "countries"

url = f"{base_url}{endpoint}"
print(url)

#faccio a richiesta api

countries = requests.request("get", url, headers=headers)
print(countries.json())
