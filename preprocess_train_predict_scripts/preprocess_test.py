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

#correlation matrix, getting rid of correlated features with lower correlation to target as we go
# cm = mmkp.drop(columns=['Winner', 'Team', 'ORtgSOS Rank', 'Losses', 'DRtgSOS Rank', 
#                         'Luck Rank', 'NetRtgSOS Rank', 'NetRtg Rank', 'DRtg Rank',
#                         'ORtgSOS', 'ORtg Rank', 'DRtgSOS', 'Tourney Seed', 'AdjT Rank',
#                         'NetRtgSOSNC', 'ORtg', 'NetRtgSOS']).corr()

# #correlation to target
# target_corr = mmkp.drop(columns='Team').corr()['Winner'].drop('Winner')

# #trying to make it into a table so i can see each variable, their corr with target variable, and corr with each other
# pairs = cm.unstack().reset_index()
# pairs.columns = ['Variable 1', 'Variable 2', 'Correlation']

# #drop duplicates
# pairs = pairs.drop_duplicates(subset=['Correlation'])

# #filter correlations with magnitude >= 0.8
# greaterthanNine = pairs[pairs['Correlation'].abs() >= 0.8]

# #correlation to target for each
# greaterthanNine['Var1 C-Target'] = greaterthanNine['Variable 1'].map(target_corr)
# greaterthanNine['Var2 C-Target'] = greaterthanNine['Variable 2'].map(target_corr)

# #sort by magnitude
# greaterthanNine = greaterthanNine.sort_values(by='Correlation', key=np.abs, ascending=False)

# greaterthanNine = pd.DataFrame(greaterthanNine[['Variable 1', 'Var1 C-Target', 'Variable 2', 'Var2 C-Target', 'Correlation']])

#all of these are above 0.9
#based on this, drop:
#ORtgSOS Rank (keep NetRtgSOS Rank)
#Losses (keep Win Percentage)
#DRtgSOS Rank (keep NetRtgSOS Rank)
#Luck Rank (keep Luck)
#NetRtgSOS Rank (keep NetRtgSOS)
#NetRtg Rank (keep NetRtg)
#DRtg Rank (keep DRtg)
#ORtgSOS (keep NetRtgSOS)
#ORtg Rank (keep ORtg)
#DRtgSOS (keep NetRtgSOS)
#all of these are above 0.8:
#i say keep win percentage bc different teams might play different amounts of games
#Tourney Seed (keep NetRtg)
#AdjT Rank (keep AdjT)
#NetRtgSOSNC (keep NetRtgSOSNC Rank)
#ORtg (keep NetRtg)
#NetRtgSOS (keep NetRtg)

#save the cleaned dataframe to CSV

output_path = "/opt/airflow/data/mmkp_preprocessed_test.csv"
mmkp.to_csv(output_path, index=False)