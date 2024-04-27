import requests

api_key = 'QTRixbdQbwZIcxKBFe11hXSwjtU2NvABeveVfffc'
#endpoint for electioneering
endpoint = 'https://api.open.fec.gov/v1/electioneering/totals/by_candidate'

# params = {
#     'api_key': api_key,
#     'candidate_id': 'P80001571', 
#     'cycle': '2024',          
#     'election_full': True,
#     'per_page': 50,                       # You can adjust this value
#     'page': 1                             # Start with the first page
# }

# # response = requests.get(endpoint, params=params)
# # data = response.json()

# # if response.status_code == 200:
# #     for item in data.get('results', []):
# #         print(f"Candidate ID: {item['candidate_id']}")
# #         print(f"Total Electioneering Cost: ${item['total']}")
# # else:
# #     print("Failed to fetch data:", response.status_code)


# #endpoint for independent expenditures
# endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_e/totals/by_candidate'

# response = requests.get(endpoint, params=params)
# data = response.json()

# # if response.status_code == 200:
# #     # Iterate over the results and print total expenditures for each candidate
# #     for item in data.get('results', []):
# #         print(f"Candidate ID: {item.get('candidate_id')}, Total Independent Expenditures: ${item.get('total')}")
# # else:
# #     print("Failed to fetch data:", response.status_code)

# #endpoint for disbursments by purpose
endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_b/by_purpose/'
endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_b/'

params = {
    'api_key': api_key,
    'cycle': 2024,
    'committee_id': 'C00794065',
    'page': 1,  # Start with the first page
    'per_page': 50,
    'purpose': ['ADMINISTRATIVE', 'ADVERTISING', 'CONTRIBUTIONS', 'EVENTS', 'FUNDRAISING', 'LOAN-REPAYMENTS',
                'MATERIALS', 'OTHER', 'POLLING', 'REFUNDS', 'TRANSFERS', 'TRAVEL']  # Disbursement purpose categories
}

disbursements_by_purpose = {}

while True:
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        print(data)
        for item in data.get('results', []):
            purpose = item.get('purpose')
            total_disbursement = item.get('total')
            total_disbursement = float(total_disbursement) 
            disbursements_by_purpose.setdefault(purpose, 0)
            disbursements_by_purpose[purpose] += total_disbursement

        if not data['pagination']['pages'] or data['pagination']['page'] >= data['pagination']['pages']:
            break
        params['page'] += 1
    else:
        print("Failed to fetch data:", response.status_code)
        break

# Print or save the disbursements by purpose
for purpose, total_disbursement in disbursements_by_purpose.items():
    print(f"Purpose: {purpose}, Total Disbursement: ${total_disbursement}")


# #endpoint for party coordinated expenditures
# endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_f/'


# total_expenditures = 0
# while True:
#     response = requests.get(endpoint, params=params)
#     data = response.json()

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Sum the expenditure amounts for the given candidate
#         total_expenditures += sum(item.get('expenditure_amount', 0) for item in data.get('results', []))
        
#         # Break the loop if we are on the last page
#         if not data['pagination']['pages'] or data['pagination']['page'] >= data['pagination']['pages']:
#             break
        
#         # Otherwise, increment the page number for the next loop iteration
#         params['page'] += 1
#     else:
#         print("Failed to fetch data:", response.status_code)
#         break

# # Print the total expenditures for the candidate
# print(f"Total Party-Coordinated Expenditures: ${total_expenditures}")

