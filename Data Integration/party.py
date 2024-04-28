import requests

api_key = "QTRixbdQbwZIcxKBFe11hXSwjtU2NvABeveVfffc"

params = {
    'api_key': api_key,
    'candidate_id': 'P80000722',          # Set to Biden
    'cycle': '2020',                      # Set to 2020
    'election_full': True,
    'per_page': 50,                       
    'page': 1                            
}

endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_f/'

response = requests.get(endpoint, params=params)
data = response.json()

total_party_coordinated_expenditures = 0

if response.status_code == 200:
    for item in data.get('results', []):
        print(f"Candidate ID: {item.get('candidate_id')}, Party Coordinated Expenditure: ${item.get('expenditure_amount')}")
        total_party_coordinated_expenditures += item.get('expenditure_amount')
else:
    print("Failed to fetch data:", response.status_code)

print(total_party_coordinated_expenditures)