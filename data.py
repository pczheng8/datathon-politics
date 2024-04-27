import requests
api_key = "QTRixbdQbwZIcxKBFe11hXSwjtU2NvABeveVfffc"

#endpoint for candidate ids
endpoint = 'https://api.open.fec.gov/v1/candidates/search'

years = [2000, 2004, 2008, 2012, 2016, 2020]

params = {
    'api_key': api_key,
    'election_year': 2018,
    'office': 'P',  # 'P' for President
    'sort': 'name'  # Sorting candidates by name
}

response = requests.get(endpoint, params=params)
data = response.json()

page = 1
while True:
    params['page'] = page
    response = requests.get(endpoint, params=params)
    data = response.json()
    if not data['results']:
        break
    for candidate in data['results']:
        if (candidate['party'] == "DEM" or candidate['party'] == "REP"):
            print(candidate['name'], candidate['party'], candidate['candidate_id'])
    page += 1