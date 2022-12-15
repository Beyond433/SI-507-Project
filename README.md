# SI-507-Project

# Project Summary
An interactive program that analyze the factors that affect the salary of NBA players.

Data Source:
Fox Sports: https://www.foxsports.com

# Instructions

0) The program will utilize the online Plotly Website, please see this page if you do not have a plotly account set up. (https://plot.ly/python/getting-started/)

1) Run foxsports_nba_crawler.py to get the most recent data (This might take up to 15-20 minutes if no cache is available because there are more than 300 currently active nba players)
2) Run foxsports_nba_database.py to create the database using the json file created from 1)
3) Run foxsports_nba_plot.py and enjoy!

Optional: foxsports_nba_test.py is the unittest file for this project

Note: Although the html cache is not provided in the repository, the database as well as the json file that is needed to create the database are, so 3) can be executed if you do not care about data potentially being outdated.


# How it works

1) The program scrapes NBA Player Injury data from Fox Sports, caches the html, and stores the useful data into a json file (nba_player_injuries.json)
2) The data from "nba_player_injuries.json" is used to create a sqlite database (nba_player_injuries.db).
3) A separate dictionary file was created (injury_loc_dict.json) that maps common injury location (e.g., knee, ankle) to a certain coordinate.
4) A Player object is created from injury data fetched from the database in 2), and it's then passed to the plot function which will map injury coordinates based on the dictionary in 3), then passed to Plotly.
5) For injuries that are ambiguous (knee injury without specifying sides), they are all pushed to a single coordinate dedicated for vague injuries.


# Program Structure (Major functions)

1) foxsports_nba_crawler.py:

    a) request_with_cache: It makes an online request and will cache anything that returns in every call
        parameters: url
                    cache dictionary
                    optional header
                    optional params
                    delay before request (to prevent server from blocking)
        returns: fetched data in whatever format it came in
        
    b) get_nba_player_injuries: Repeatedly call request_with_cache to get all nba player injury data, then returns them in one big dictionary
        parameter: cache dictionary
        returns: a dictionary containing all injuries data from all active nba players

2) foxsports_nba_database.py:

    a) reset_database: Reset the database, and takes the most updated "nba_player_injury.json" file to populate the database
        parameter: nothing
        returns: nothing
        
3) foxsports_nba_plotly.py:

    a) Player class: a Player object will have 3 instance variables: self.team (a string), self.name (a string), and self.injuries (a list of injuries)
        - Calling the Player object in a print statement will print out the player's team, then the player's name (e.g., Houston Rockets - Chris Paul)
        - If the dictionary passed to the Player object on instantiation has no an empty value in 'name', calling the Player object in a print statement will print "Null Player Object" to show that the object was created, but has no meaningful data (since you don't know which player this is supposed to be)
        
    b) get_player_data: Grabs Player Injury Information from Database
        Parameter: Player Name in String Format:
                  1) 2 words separated by a space           
                  2) 1 word
        Returns: Dictionary containing Player Information
        
    c) plot: Use Player Data to Plot Infographics on Plotly
        Parameter: Player Object created using data returned from get_player_data()
        Returns: nothing 
        
    d) interaction: Handles User Interaction with the program
        Parameter: nothing
        Returns: nothing


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

Note: requirements.txt is also provided

# User Interactions

The program will first prompt the user to enter the name of an nba player:
  - If input can be split into more than 2 strings (For first/last name), the user is reprompted
  - It is possible user only remembers part of the player name, so entering just the first name or last is acceptable
  - If input is "exit" (or other variations like "eXiT"), the program will terminate
  
  If only one player is found, it will proceed to plot immediately:
    - If player has no injury, the plot function will return immediately
    
  If more than one players are found, it will display a list of the players:
    - The user will choose which player they want by entering a number representing the player.
    - Invalid inputs (number too large or too small, or non-digit inputs) will immediately cause reprompt


# Credits

Picture Credit: https://userscontent2.emaze.com/images/0e8ac80a-9117-45a0-b503-41d01ee8ddfa/cefc4149-a2d4-4432-b328-e4c1b3fd0a7a.jpg
