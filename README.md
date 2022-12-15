# SI-507-Project

# Project Summary
An interactive program that analyze the factors that affect the salary of NBA players.

Data Source:
Espn Sports: https://www.espn.com/nba/
# Instructions

1) Run nba_data.py to get the most recent data (This might take up to 20 minutes) and get a csv file
2) Run nba_tree.py to create the tree structure and generate the json file nba.json
3) Run nba_data_analysis.ipynb to get results

# How it works

1) The program scrapes NBA Player data from Espn Sports, caches the html, and stores the useful data into a csv file (nba_player_injuries.json)
2) The data from "nba_player_injuries.json" is used to create a sqlite database (nba_player_injuries.db).
3) A separate dictionary file was created (injury_loc_dict.json) that maps common injury location (e.g., knee, ankle) to a certain coordinate.
4) A Player object is created from injury data fetched from the database in 2), and it's then passed to the plot function which will map injury coordinates based on the dictionary in 3), then passed to Plotly.
5) For injuries that are ambiguous (knee injury without specifying sides), they are all pushed to a single coordinate dedicated for vague injuries.

# Required Packages
(* means should be built-in)

- requests          (for requesting web-based data)
- json*             (for encoding/decoding json formatted data)
- bs4               (for parsing and navigating html texts)
- datetime          (for creating timestamp for cache)
- time*             (for pausing in between requests to avoid getting blocked by server)
- re*               (regular expression, useful for finding things based on text patterns)
- sqlite3*          (the chosen database format)
- unidecode         (turns unique letters into one from the standard 26 letter alphabet; e.g., "è" is turned into "e")
- plotly            (needed for plotting on plotly)

# User Interactions

The program will first prompt the user to enter the element of an nba player, and returns the connection between this element and salary.

