import requests
import csv

api_key = "QTRixbdQbwZIcxKBFe11hXSwjtU2NvABeveVfffc"

#endpoint for candidate ids
endpoint = 'https://api.open.fec.gov/v1/candidates/search'

years = [2000, 2004, 2008, 2012, 2016, 2020]

candidates_per_year = []

for year in years: 
    candidates_list = []
    params = {
        'api_key': api_key,
        'election_year': year,
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
        if 'results' not in data or not data['results']:
            break
        for candidate in data['results']:
            if (candidate['party'] == "DEM" or candidate['party'] == "REP"):
                candidates_list.append([candidate['name'], year, candidate['party'], candidate['candidate_id']])
        page += 1

    candidates_per_year.extend(candidates_list)

#write candidates to csv file      
filename = "financial_data.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "year", "party", "id"])
    for row in candidates_per_year:
        writer.writerow(row)


