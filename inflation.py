import pandas as pd

#inflation rates for each election year to 2023
ir_2000 = 1.77
ir_2004 = 1.61
ir_2008 = 1.42
ir_2012 = 1.33
ir_2016 = 1.27
ir_2020 = 1.18

# Read the CSV file into a DataFrame
df = pd.read_csv('financial_data_3.csv')

#Iterate over each row in the DataFrame to convert the financial values into 2023 (US) dollars 
for index, row in df.iterrows():
    party_val = row['party expenditures']
    ind_val = row['independent expenditures']
    electioneering_val = row['electioneering costs']
    year = row['year']

    if(year == 2000):
        df.at[index, 'party expenditures'] = party_val*ir_2000
        df.at[index, 'independent expenditures'] = ind_val*ir_2000
        df.at[index, 'electioneering costs'] = electioneering_val*ir_2000
    if(year == 2004):
        df.at[index, 'party expenditures'] = party_val*ir_2004
        df.at[index, 'independent expenditures'] = ind_val*ir_2004
        df.at[index, 'electioneering costs'] = electioneering_val*ir_2004
    if(year == 2008):
        df.at[index, 'party expenditures'] = party_val*ir_2008
        df.at[index, 'independent expenditures'] = ind_val*ir_2008
        df.at[index, 'electioneering costs'] = electioneering_val*ir_2008
    if(year == 2012):
        df.at[index, 'party expenditures'] = party_val*ir_2012
        df.at[index, 'independent expenditures'] = ind_val*ir_2012
        df.at[index, 'electioneering costs'] = electioneering_val*ir_2012
    if(year == 2016):
        df.at[index, 'party expenditures'] = party_val*ir_2016
        df.at[index, 'independent expenditures'] = ind_val*ir_2016
        df.at[index, 'electioneering costs'] = electioneering_val*ir_2016
    if(year == 2020):
        df.at[index, 'party expenditures'] = party_val*ir_2020
        df.at[index, 'independent expenditures'] = ind_val*ir_2020
        df.at[index, 'electioneering costs'] = electioneering_val*ir_2020

#Convert the dataframe back into a csv file containing the new financial data
df.to_csv('final_financial_data.csv', index=False)