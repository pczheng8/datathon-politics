import requests

api_key = 'QTRixbdQbwZIcxKBFe11hXSwjtU2NvABeveVfffc'

params = {
     'api_key': api_key,
     'candidate_id': 'P80000722',       #Set to Biden
     'cycle': '2020',                   #Set to 2020
     'election_full': True,
     'per_page': 50,                       
     'page': 1                             
}

# endpoint for electioneering
endpoint = 'https://api.open.fec.gov/v1/electioneering/totals/by_candidate/'

response = requests.get(endpoint, params=params)
data = response.json()

total_electioneering = 0

if response.status_code == 200:
    # Iterate over the results and print electioneering for a candidate
    for item in data.get('results', []):
        print(f"Candidate ID: {item.get('candidate_id')}, Cycle:{item.get('cycle')}, Electioneering: ${item.get('total')}")
        total_electioneering+= item.get('total')
else:
    print("Failed to fetch data:", response.status_code)

print(total_electioneering)