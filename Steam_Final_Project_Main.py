### Importing from Final Porject Library (import everything)
from Steam_Final_Project_Lib import *

# Calling the class
review_dfs = Reviews()
game_dfs = Reviews()


## Opening Statement when Running Program
print(f"Welcome to the Steam Sentiment Analysis!")
print(f"Note: Steam Sentiments are based on 1's (Good sentiments) and 0's (Bad sentiments)!")
print("------------------------------------------------------------------------------\n")


## Input Statement for users to look at good or bad reviews
review_input = input("Please type in a type of sentiment you would like to see: ")
# Retrieve specific dataframes based on review inputs
reviews_df = review_dfs.getReviews(review_input)


# If a valid entry is returned, print out contents
if reviews_df is not None:
    print(reviews_df)

## Create a second input statement for those who want to look at a specific game.
print("------------------------------------------------------------------------------------------------\n")
game_input = input("Is there a specific game you would like to see? ")
# Retrieve dataframes based on input given
games_df = game_dfs.getGames(game_input)

# If the entry is valid, print out contents
if games_df is not None:
    print(games_df)


## After the program has run, create output files for the review and games selected
if review_input == 'All':
    reviews_df.to_csv("cleaned_steam_reviews.csv")

elif review_input == 'Positive':
    reviews_df.to_csv("positive_reviews.csv")

elif review_input == "Negative":
    reviews_df.to_csv("negative_reviews.csv")

if game_input == 'Apex Legends':
    games_df.to_csv("apex_legends.csv")

elif game_input == 'CSGO':
    games_df.to_csv("counter-strike.csv")

elif game_input == 'DOTA 2':
    games_df.to_csv("DOTA_2.csv")

elif game_input == 'GTA V':
    games_df.to_csv("GTA_V.csv")

elif game_input == 'Monster Hunter':
    games_df.to_csv("Monster_Hunter.csv")

elif game_input == 'Naraka':
    games_df.to_csv("Naraka.csv")

elif game_input == 'PUBG':
    games_df.to_csv("PUBG.csv")

elif game_input == 'RUST':
    games_df.to_csv("RUST.csv")

elif game_input == 'Team Fortress 2':
    games_df.to_csv("TF2.csv")

elif game_input == 'MIR4':
    games_df.to_csv("MIR4.csv")


# Ending Statement
print("------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"You can re-run the program to look at more sentiments or check out the CSV file that has downloaded on your device based on the sentiment type and game you input!\n")