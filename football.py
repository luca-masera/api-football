
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

#faccio a richiesta api per i continenti

countries = requests.request("get", url, headers=headers)

c_dict= countries.json()['response']
print(len(c_dict))
print(json.dumps(c_dict[0], indent=4))

#stampo tutti i paesi con le iniziali
for i in c_dict:
    print(f"{i["name"]} -> {i["code"]}")
    

params = {
    "code" : "IT"
}

italy = requests.request("get", url, headers=headers, params=params)
print(italy.json())
print(italy.request.url)

#faccio a richiesta api per i campionati e prendo la serie A

endpoint = "leagues"

url = f"{base_url}{endpoint}"
print(url)

leagues = requests.request("get", url, headers=headers, params=params)
print(json.dumps(leagues.json()['response'], indent=4))

italy_leagues = leagues.json()['response']
serie_a = italy_leagues[0]
print(serie_a['league'])

serie_a_id= serie_a['league']['id']
print(serie_a_id)