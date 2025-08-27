import pandas as pd
import numpy as np

mmkp = pd.read_csv('/opt/airflow/data/MM_KP.csv') #CHANGE THIS
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


#2002 seeding
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2002), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Tulsa') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Southern Illinois') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Georgia') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'N.C. State') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2002), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Stanford') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Mississippi St.') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wake Forest') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2002), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2002), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'UNC Wilmington') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'California') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kent St.') & (mmkp['Year'] == 2002), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Missouri') & (mmkp['Year'] == 2002), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wyoming') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2002), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2002), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2002), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2002), 'Winner'] = 4/6

#2003
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2003), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'California') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma St.') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2003), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Auburn') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Wake Forest') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2003), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Utah') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Tulsa') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Missouri') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2003), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2003), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Stanford') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2003), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2003), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Central Michigan') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2003), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Arizona St.') & (mmkp['Year'] == 2003), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2003), 'Winner'] = 5/6

#2004
mmkp.loc[(mmkp['Team'] == "Saint Joseph's") & (mmkp['Year'] == 2004), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Texas Tech') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Manhattan') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wake Forest') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma St.') & (mmkp['Year'] == 2004), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UAB') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Pacific') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2004), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Boston College') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Georgia Tech') & (mmkp['Year'] == 2004), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Nevada') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2004), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Seton Hall') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2004), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Mississippi St.') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Stanford') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2004), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Vanderbilt') & (mmkp['Year'] == 2004), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'N.C. State') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'DePaul') & (mmkp['Year'] == 2004), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2004), 'Winner'] = 6/6

#2005
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2005), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2005), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Bucknell') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'N.C. State') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2005), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Nevada') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Milwaukee') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Boston College') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UAB') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2005), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Southern Illinois') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma St.') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Mississippi St.') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2005), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Vermont') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Utah') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2005), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Washington') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Pacific') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Georgia Tech') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2005), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Texas Tech') & (mmkp['Year'] == 2005), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2005), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2005), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Wake Forest') & (mmkp['Year'] == 2005), 'Winner'] = 1/6

#2006
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2006), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Washington') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'George Mason') & (mmkp['Year'] == 2006), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wichita St.') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2006), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Montana') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Boston College') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Milwaukee') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2006), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Georgetown') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'George Washington') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'LSU') & (mmkp['Year'] == 2006), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Northwestern St.') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'N.C. State') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2006), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2006), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Bucknell') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Bradley') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2006), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2006), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2006), 'Winner'] = 5/6

#2007
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2007), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'USC') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Vanderbilt') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Washington St.') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Boston College') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Georgetown') & (mmkp['Year'] == 2007), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2007), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Winthrop') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2007), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'UNLV') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2007), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Virginia') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Nevada') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2007), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2007), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Virginia Tech') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Southern Illinois') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'VCU') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2007), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2007), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2007), 'Winner'] = 4/6

#2008
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2008), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Arkansas') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Washington St.') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2008), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2008), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'UNLV') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Siena') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas St.') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Davidson') & (mmkp['Year'] == 2008), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Georgetown') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2008), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Mississippi St.') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Stanford') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Miami FL') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2008), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2008), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Western Kentucky') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'San Diego') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2008), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2008), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2008), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2008), 'Winner'] = 1/6

#2009
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2009), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma St.') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2009), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2009), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2009), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2009), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Siena') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2009), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Cleveland St.') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Dayton') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2009), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'USC') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2009), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2009), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'LSU') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Western Kentucky') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2009), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Arizona St.') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2009), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2009), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2009), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2009), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Washington') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Missouri') & (mmkp['Year'] == 2009), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2009), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2009), 'Winner'] = 2/6

#2010
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2010), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2010), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'New Mexico') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Cornell') & (mmkp['Year'] == 2010), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Washington') & (mmkp['Year'] == 2010), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Missouri') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wake Forest') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2010), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kansas St.') & (mmkp['Year'] == 2010), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Murray St.') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2010), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2010), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'BYU') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2010), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2010), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2010), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Old Dominion') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == "Saint Mary's") & (mmkp['Year'] == 2010), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'California') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2010), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Ohio') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2010), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2010), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Georgia Tech') & (mmkp['Year'] == 2010), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Northern Iowa') & (mmkp['Year'] == 2010), 'Winner'] = 2/6

#2011
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2011), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2011), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Washington') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'George Mason') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'San Diego St.') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2011), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2011), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Temple') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2011), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Morehead St.') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Richmond') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'VCU') & (mmkp['Year'] == 2011), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Florida St.') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2011), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'BYU') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2011), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kansas St.') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2011), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2011), 'Winner'] = 5/6

#2012
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2012), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Florida St.') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Vanderbilt') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas St.') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Norfolk St.') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2012), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'New Mexico') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Murray St.') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2012), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Saint Louis') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2012), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Lehigh') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2012), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'VCU') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2012), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2012), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Georgetown') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Ohio') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'South Florida') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'N.C. State') & (mmkp['Year'] == 2012), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2012), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2012), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Colorado') & (mmkp['Year'] == 2012), 'Winner'] = 1/6

#2013
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2013), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2013), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Saint Louis') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Colorado St.') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2013), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Harvard') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'La Salle') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Mississippi') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wichita St.') & (mmkp['Year'] == 2013), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Miami FL') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2013), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2013), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'California') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Temple') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida Gulf Coast') & (mmkp['Year'] == 2013), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2013), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2013), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'VCU') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Minnesota') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'San Diego St.') & (mmkp['Year'] == 2013), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2013), 'Winner'] = 1/6

#2014
mmkp.loc[(mmkp['Team'] == 'Wichita St.') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2014), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Mercer') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Saint Louis') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2014), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2014), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2014), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'San Diego St.') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'North Dakota St.') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Virginia') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2014), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Harvard') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2014), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2014), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Stephen F. Austin') & (mmkp['Year'] == 2014), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Dayton') & (mmkp['Year'] == 2014), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Stanford') & (mmkp['Year'] == 2014), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2014), 'Winner'] = 1/6

#2015
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2015), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2015), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wichita St.') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2015), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2015), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Georgia St.') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Arkansas') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Virginia') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2015), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Northern Iowa') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Dayton') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2015), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'N.C. State') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2015), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2015), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'UAB') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Georgetown') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Utah') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2015), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Iowa') & (mmkp['Year'] == 2015), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'San Diego St.') & (mmkp['Year'] == 2015), 'Winner'] = 1/6

#2016
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2016), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Stephen F. Austin') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2016), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Providence') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2016), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2016), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Yale') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Northern Iowa') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'VCU') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == "Saint Joseph's") & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2016), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2016), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Miami FL') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == "Hawaii") & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Wichita St.') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Iowa') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Virginia') & (mmkp['Year'] == 2016), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Middle Tennessee') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Utah') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2016), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arkansas Little Rock') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2016), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2016), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2016), 'Winner'] = 1/6

#2017
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2017), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Virginia') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'USC') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'South Carolina') & (mmkp['Year'] == 2017), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2017), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida St.') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2017), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == "Saint Mary's") & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Northwestern') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2017), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2017), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Middle Tennessee') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wichita St.') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arkansas') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2017), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Louisville') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2017), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Rhode Island') & (mmkp['Year'] == 2017), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2017), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2017), 'Winner'] = 1/6

#2018
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2018), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas Tech') & (mmkp['Year'] == 2018), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Marshall') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Butler') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2018), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Houston') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida St.') & (mmkp['Year'] == 2018), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'UMBC') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Cincinnati') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Buffalo') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Loyola Chicago') & (mmkp['Year'] == 2018), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Nevada') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kansas St.') & (mmkp['Year'] == 2018), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2018), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2018), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Auburn') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Clemson') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2018), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Rhode Island') & (mmkp['Year'] == 2018), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Seton Hall') & (mmkp['Year'] == 2018), 'Winner'] = 1/6

#2019
#some kenpom teams get ranks even when they didnt make the tournament?
remove = ["Texas", "Clemson", "TCU", "N.C. State", "Lipscomb", "Nebraska", "Indiana", "Arkansas",
    "Creighton", "Memphis", "Furman", "Toledo", "Dayton", "Colorado", "Alabama", "Xavier",
    "Wichita St.", "Butler", "Providence", "Davidson", "UNC Greensboro", "San Diego", 
    "South Dakota St.", "Hofstra", "Georgetown", "Harvard", "Wright St.", "Loyola Chicago", 
    "Sam Houston St.", "Campbell", "Norfolk St.", "St. Francis PA"]

# Remove rows where 'Team' is in the list and 'Year' is 2019
mmkp = mmkp[~((mmkp['Team'].isin(remove)) & (mmkp['Year'] == 2019))]

mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2019), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2019), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'LSU') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Virginia Tech') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Liberty') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Minnesota') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCF') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2019), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas Tech') & (mmkp['Year'] == 2019), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Florida St.') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Murray St.') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Buffalo') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Virginia') & (mmkp['Year'] == 2019), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2019), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'UC Irvine') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Iowa') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2019), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Houston') & (mmkp['Year'] == 2019), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Auburn') & (mmkp['Year'] == 2019), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Wofford') & (mmkp['Year'] == 2019), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Washington') & (mmkp['Year'] == 2019), 'Winner'] = 1/6

#2021
#some kenpom teams get ranks even when they didnt make the tournament?
remove = ["Memphis", "Mississippi", "Saint Louis", "SMU", "Boise St.", "Richmond", "Mississippi St.", "Davidson",
    "N.C. State", "Toledo", "Saint Mary's", "Colorado St.", "Buffalo", "Louisiana Tech", "Dayton", "Western Kentucky"]

# Remove rows where 'Team' is in the list and 'Year' is 2021
mmkp = mmkp[~((mmkp['Team'].isin(remove)) & (mmkp['Year'] == 2021))]

mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Loyola Chicago') & (mmkp['Year'] == 2021), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Oregon St.') & (mmkp['Year'] == 2021), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma St.') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Syracuse') & (mmkp['Year'] == 2021), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'West Virginia') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Rutgers') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Houston') & (mmkp['Year'] == 2021), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2021), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Oklahoma') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2021), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Ohio') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'USC') & (mmkp['Year'] == 2021), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2021), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Iowa') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2021), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'LSU') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Colorado') & (mmkp['Year'] == 2021), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Florida St.') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2021), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Abilene Christian') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2021), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2021), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2021), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'North Texas') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas Tech') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arkansas') & (mmkp['Year'] == 2021), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2021), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oral Roberts') & (mmkp['Year'] == 2021), 'Winner'] = 2/6

#2022
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2022), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Richmond') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Providence') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Miami FL') & (mmkp['Year'] == 2022), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Auburn') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Memphis') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'New Mexico St.') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arkansas') & (mmkp['Year'] == 2022), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Notre Dame') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas Tech') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2022), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2022), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == "Saint Mary's") & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Murray St.') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == "Saint Peter's") & (mmkp['Year'] == 2022), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'TCU') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Houston') & (mmkp['Year'] == 2022), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2022), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Ohio St.') & (mmkp['Year'] == 2022), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Villanova') & (mmkp['Year'] == 2022), 'Winner'] = 4/6

#2023
mmkp.loc[(mmkp['Team'] == 'Houston') & (mmkp['Year'] == 2023), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Auburn') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Miami FL') & (mmkp['Year'] == 2023), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Indiana') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Pittsburgh') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Xavier') & (mmkp['Year'] == 2023), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Penn St.') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2023), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arkansas') & (mmkp['Year'] == 2023), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == "Saint Mary's") & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2023), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'TCU') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2023), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Northwestern') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2023), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Fairleigh Dickinson') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Florida Atlantic') & (mmkp['Year'] == 2023), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2023), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Kansas St.') & (mmkp['Year'] == 2023), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2023), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2023), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'San Diego St.') & (mmkp['Year'] == 2023), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Furman') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2023), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Missouri') & (mmkp['Year'] == 2023), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Princeton') & (mmkp['Year'] == 2023), 'Winner'] = 2/6

#2024
mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2024), 'Winner'] = 6/6
mmkp.loc[(mmkp['Team'] == 'Northwestern') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'San Diego St.') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Yale') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duquesne') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2024), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Washington St.') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'North Carolina') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Grand Canyon') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2024), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Clemson') & (mmkp['Year'] == 2024), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Dayton') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Houston') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'James Madison') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2024), 'Winner'] = 3/6
mmkp.loc[(mmkp['Team'] == 'N.C. State') & (mmkp['Year'] == 2024), 'Winner'] = 4/6
mmkp.loc[(mmkp['Team'] == 'Oakland') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Colorado') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Marquette') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2024), 'Winner'] = 5/6
mmkp.loc[(mmkp['Team'] == 'Utah St.') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Kansas') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2024), 'Winner'] = 2/6
mmkp.loc[(mmkp['Team'] == 'Texas') & (mmkp['Year'] == 2024), 'Winner'] = 1/6
mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2024), 'Winner'] = 3/6

#2025 - commented out until 2026 seeding comes out - this will be used as test
mmkp = mmkp[mmkp['Year'] != 2025]
# mmkp.loc[(mmkp['Team'] == 'Purdue') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Wisconsin') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Houston') & (mmkp['Year'] == 2025), 'Winner'] = 5/6
# mmkp.loc[(mmkp['Team'] == 'Auburn') & (mmkp['Year'] == 2025), 'Winner'] = 4/6
# mmkp.loc[(mmkp['Team'] == 'McNeese') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'BYU') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Gonzaga') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Tennessee') & (mmkp['Year'] == 2025), 'Winner'] = 3/6
# mmkp.loc[(mmkp['Team'] == 'Arkansas') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Texas A&M') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Drake') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'UCLA') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == "St. John's") & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Michigan') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Texas Tech') & (mmkp['Year'] == 2025), 'Winner'] = 3/6
# mmkp.loc[(mmkp['Team'] == 'Baylor') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Alabama') & (mmkp['Year'] == 2025), 'Winner'] = 3/6
# mmkp.loc[(mmkp['Team'] == 'Iowa St.') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Colorado St.') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Duke') & (mmkp['Year'] == 2025), 'Winner'] = 4/6
# mmkp.loc[(mmkp['Team'] == "Saint Mary's") & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Mississippi') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Maryland') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Florida') & (mmkp['Year'] == 2025), 'Winner'] = 6/6
# mmkp.loc[(mmkp['Team'] == 'New Mexico') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Kentucky') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Arizona') & (mmkp['Year'] == 2025), 'Winner'] = 2/6
# mmkp.loc[(mmkp['Team'] == 'Connecticut') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Illinois') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Michigan St.') & (mmkp['Year'] == 2025), 'Winner'] = 3/6
# mmkp.loc[(mmkp['Team'] == 'Oregon') & (mmkp['Year'] == 2025), 'Winner'] = 1/6
# mmkp.loc[(mmkp['Team'] == 'Creighton') & (mmkp['Year'] == 2025), 'Winner'] = 1/6

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
# greaterthanNine['Var1 -Target'] = greaterthanNine['Variable 1'].map(target_corr)
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
output_path = '/opt/airflow/data/mmkp_preprocessed_train.csv'
mmkp.to_csv(output_path, index=False)