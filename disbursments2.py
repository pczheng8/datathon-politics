import requests

api_key = 'QTRixbdQbwZIcxKBFe11hXSwjtU2NvABeveVfffc'

endpoint = 'https://api.open.fec.gov/v1/schedules/schedule_b/'

params = {
    'api_key': api_key,
    'cycle': 2024,
    'per_page': 50,
    'candidate_id': 'P8001571', 
}

disbursements_by_purpose = {}

num_iterations = 10
iteration_count = 0

while iteration_count < num_iterations:
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        print(data)
        print(" ")
        for item in data.get('results', []):
            purpose = item.get('disbursement_purpose_category')
            disbursement_amount = item.get('disbursement_amount', 0)
            
            # Initialize total disbursement for the purpose if not exists
            if purpose not in disbursements_by_purpose:
                disbursements_by_purpose[purpose] = 0
                
            # Add disbursement amount to the total for the purpose
            disbursements_by_purpose[purpose] += disbursement_amount

        # Increment the iteration count
        iteration_count += 1

        # Fetch the next page using last_indexes
        if not data['results']:
            break
        params.update(data['pagination']['last_indexes'])
    else:
        print("Failed to fetch data:", response.status_code)
        break

# Print or save the disbursements by purpose
for purpose, total_disbursement in disbursements_by_purpose.items():
    print(f"Purpose: {purpose}, Total Disbursement: ${total_disbursement}")
