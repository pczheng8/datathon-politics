import requests

api_key = 'QTRixbdQbwZIcxKBFe11hXSwjtU2NvABeveVfffc'

params = {
     'api_key': api_key,
     'candidate_id': 'P80001571',       #Set to Trump
     'cycle': '2016',                   #Set to 2020
     'election_full': True,
     'per_page': 50,                       
     'page': 1                             
}

# endpoint for independent expenditures
endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_e/totals/by_candidate'

response = requests.get(endpoint, params=params)
data = response.json()

total_ind_expenditure = 0

if response.status_code == 200:
    # Iterate over the results and print expenditures (in support) for a candidate
    for item in data.get('results', []):
        print(f"Candidate ID: {item.get('candidate_id')}, Total Independent Expenditures: ${item.get('total')}, S/O: {item.get('support_oppose_indicator')}")
        if(item.get('support_oppose_indicator') == "S"):
            total_ind_expenditure+= item.get('total')
else:
    print("Failed to fetch data:", response.status_code)

print(total_ind_expenditure)
