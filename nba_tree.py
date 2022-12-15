import json

import pandas as pd

# Read csv files
df = pd.read_csv('nba.csv')

# All fields are divided into three categories: other personal_info, improvement
other = ['MIN', "DD2", "TD3"]
personal_info = ['POS', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'REB', 'AST', 'STL', 'BLK', 'TO']
improvement = ['GP']

data = {}
for i in range(len(df)):
    print(df["NAME"][i])
    data[df["NAME"][i]] = {}
    # Generate other fields
    data[df["NAME"][i]]['other'] = {}
    for j in other:
        data[df["NAME"][i]]['other'][j] = str(df[j][i])
    # Generate the personal_info field
    data[df["NAME"][i]]['personal_info'] = {}
    for j in personal_info:
        data[df["NAME"][i]]['personal_info'][j] = str(df[j][i])
    # Generate the improvement field
    data[df["NAME"][i]]['improvement'] = {}
    for j in improvement:
        data[df["NAME"][i]]['improvement'][j] = str(df[j][i])

# Generate json file
with open('nba.json', 'w') as f:
    json.dump(data, f)
