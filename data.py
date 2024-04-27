import requests
import csv
import pandas as pd

api_key = "MSlqr8knhEU4tZuCrnYEA4Dq9VgF6DLzBZjyHEaV"

# ADDING CANDIDATES

# #endpoint for candidate ids
# endpoint = 'https://api.open.fec.gov/v1/candidates/search'

# years = [2000, 2004, 2008, 2012, 2016, 2020]

# candidates_per_year = []

# for year in years: 
#     candidates_list = []
#     params = {
#         'api_key': api_key,
#         'election_year': year,
#         'office': 'P',  # 'P' for President
#         'sort': 'name',  # Sorting candidates by name
#         'per_page': 100
#     }

#     response = requests.get(endpoint, params=params)
#     data = response.json()

#     page = 1
#     while True:
#         params['page'] = page
#         response = requests.get(endpoint, params=params)
#         data = response.json()
#         if 'results' not in data or not data['results']:
#             break
#         for candidate in data['results']:
#             if (candidate['party'] == "DEM" or candidate['party'] == "REP"):
#                 candidates_list.append([candidate['name'], year, candidate['party'], candidate['candidate_id']])
#         page += 1

#     candidates_per_year.extend(candidates_list)

# #write candidates to csv file      
# filename = "financial_data.csv"
# with open(filename, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "year", "party", "id"])
#     for row in candidates_per_year:
#         writer.writerow(row)


#ADDING PARTY EXPENDITURES
df = pd.read_csv("financial_data.csv")

party = []

endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_f/'

party = []

for index, row in df.iloc[0:100].iterrows():
    params = {
        'api_key': api_key,
        'candidate_id': row['id'],          # Set to Biden
        'cycle': row['year'],                      # Set to 2020
        'election_full': True,
        'per_page': 50,                       
        'page': 1                            
    }

    response = requests.get(endpoint, params=params)

    total_party_coordinated_expenditures = 0

    if response.status_code == 200:
        data = response.json()
        for item in data.get('results', []):
            total_party_coordinated_expenditures += item.get('expenditure_amount')
    else:
        print("Failed to fetch data:", response.status_code)

    party.append(total_party_coordinated_expenditures)

print(party)



