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

1) The program scrapes NBA Player data from Espn Sports, caches the html, and stores the useful data into a csv file (nba.csv)
2) The data from "nba.csv" is used to create a tree structure (nba.json).
3) A Player object is created from injury data fetched from the database in 2), and it's then passed to the plot function which will map information coordinates based on the dictionary in 2), then passed to users.

# Required Packages

- csv
- selenium.webdriver
- time      
- selenium.webdriver.chrome.options

- json
- pandas

- matplotlib.pyplot

# User Interactions

The program will first prompt the user to enter the element of an nba player, and returns the connection between this element and salary.

