import pandas as pd
import numpy as np

mmkp = pd.read_csv('/opt/airflow/data/MM_KP.csv') #CHANGE THIS

mmkp = mmkp[mmkp['Year'] == 2025]

#renaming columns correctly
mmkp.rename(columns={'Unnamed: 6': 'ORtg Rank'}, inplace=True)
mmkp.rename(columns={'Unnamed: 8': 'DRtg Rank'}, inplace=True)
mmkp.rename(columns={'Unnamed: 10': 'AdjT Rank'}, inplace=True)
mmkp.rename(columns={'Unnamed: 12': 'Luck Rank'}, inplace=True)
mmkp.rename(columns={'NetRtg.1': 'NetRtgSOS'}, inplace=True)
mmkp.rename(columns={'Unnamed: 14': 'NetRtgSOS Rank'}, inplace=True)
mmkp.rename(columns={'ORtg.1': 'ORtgSOS'}, inplace=True)
mmkp.rename(columns={'Unnamed: 16': 'ORtgSOS Rank'}, inplace=True)
mmkp.rename(columns={'DRtg.1': 'DRtgSOS'}, inplace=True)
mmkp.rename(columns={'Unnamed: 18': 'DRtgSOS Rank'}, inplace=True)
mmkp.rename(columns={'NetRtg.2': 'NetRtgSOSNC'}, inplace=True)
mmkp.rename(columns={'Unnamed: 20': 'NetRtgSOSNC Rank'}, inplace=True)
mmkp.rename(columns={'Rk': 'NetRtg Rank'}, inplace=True)

#tournament seed
import re
def extract_seed(team_name):
    match = re.search(r'(\d+)\*?$', team_name)  #match a number or '*' at the end
    return int(match.group(1)) if match else 0  #extract the number if found, else return 0

mmkp['Tourney Seed'] = mmkp['Team'].apply(extract_seed) #tourney seed creation

mmkp['Tourney Seed'] = mmkp['Tourney Seed'].astype(int) #make sure its an int and not string
#only include teams in tourney
mmkp = mmkp[mmkp['Tourney Seed'] != 0]
#tourney didnt happen 2020
mmkp = mmkp[mmkp['Year'] != 2020]

#change team name to get rid of number
mmkp['Team'] = mmkp['Team'].apply(lambda x: re.split(r'\d', x)[0].strip()) 
mmkp['Team'] = mmkp['Team'].str.rstrip() #dont want any spaces after words bc when we encode we want 'Duke' and 'Duke ' to be the same


#assigning winners
mmkp['Winner'] = 0

#win percentage - we want less dimensions
mmkp[['Wins', 'Losses']] = mmkp['W-L'].str.split('-', expand=True).astype(int)
mmkp['Win Percentage'] = mmkp['Wins'] / (mmkp['Wins'] + mmkp['Losses'])
mmkp = mmkp.drop(columns=['W-L'])
#keep wns and losses because one might be more important individually
#also two teams might have same win percentage, but one team has more ones, etc

#turning team name and conference numerical
mmkp['Team_Name'] = pd.factorize(mmkp['Team'])[0]
mmkp['Conf'] = pd.factorize(mmkp['Conf'])[0]

output_path = "/opt/airflow/data/mmkp_test_team_col.csv"
mmkp['Team'].to_csv(output_path, index=False)

#save the cleaned dataframe to CSV

mmkp_train = pd.read_csv('/opt/airflow/data/mmkp_preprocessed_train.csv') #CHANGE THIS
mmkp_train_cols = mmkp_train.columns

mmkp = mmkp[mmkp_train_cols]

output_path = "/opt/airflow/data/mmkp_preprocessed_test.csv"
mmkp.to_csv(output_path, index=False)