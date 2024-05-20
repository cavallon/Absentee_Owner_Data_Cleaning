import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import scipy.stats as st

#import out of state owners file:
file_path = Path("C:/Users/chris/Desktop/Data_Projects/Absentee_Owner_Data_Cleaning/Resources/mercer_county_outofstate_owners.csv")

#create dataframe:
state_data = pd.read_csv(file_path)

#drop nulls:
state_data.dropna(inplace=True)

#drop duplicates from Address column in expired_sold_df. 
state_data.drop_duplicates(subset='Property Address Formatted', keep=False, inplace=True,)

#rename columns:
state_data.rename(columns = {'Property Address Formatted': 'Property Address', 'City': 'Property City', 'State Or Province': 'Property State', 'Postal Code': 'Property Zip Code', 
                                    'Owner Postal Code': 'Owner Zip Code', "Owner Postal 4": 'Owner Zip 4', 'Postal Code Plus 4': 'Property Zip 4'}, inplace = True)

#drop not needed columns:
state_data.drop(["Tax ID", "Current Owner Name", "Owner Do Not Mail YN"], axis=1, inplace=True)

#drop .0 from owner zip code column:
state_data['Owner Zip Code'] = state_data['Owner Zip Code'].astype(str).replace('\.0', '', regex=True)

#correct all zip codes by adding the leading 0:
state_data['Owner Zip Code'] = state_data['Owner Zip Code'].apply(lambda x: '{0:0>5}'.format(x))
state_data['Property Zip Code'] = state_data['Property Zip Code'].apply(lambda x: '{0:0>5}'.format(x))

#sort data by property city:
state_data.sort_values(by=['Property City'], inplace=True)

#export finalized data to csv for mailing:
state_data.to_csv('merc_county_absentee_owner_mailing_list.csv')