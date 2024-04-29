#### Steam Sentiment Analysis Library
## Begin with imports 
## Usage of Pandas for creation of DataFrames (approved by Professor Lars Sorensen)
import pandas as pd
# Import Counter to show the number of seintiments for each game depending on Sentiment input
from collections import Counter

### Class for reviews that will be based on user input
class Reviews():
    def __init__(self):
        ### Creating data strictures in the form of clean DataFrames with Pandas
        ## Opening file with pandas for easier viewing 
        steam_file_df = pd.read_csv("Steam_Reviews_Test.csv")
        print("Original 'Steam_Reviews_Test.csv' CSV Data: \n")

        ## Remove unecessary columns due to redundancy 
        steam_file_df.pop('Review')
        steam_file_df.pop('Translated_Review')

        # Reorder columns for easier viewing
        self.cleaned_steam_file_df = steam_file_df[['Game', 'Sentiment', 'Cleaned_Review']]

        
        ## Create counters for the number of positive and negative sentiments
        self.game_positives = Counter()
        self.game_negatives = Counter()

        ## Creating data structures for positive and negative sentiment
        # Create DataFrame for positive sentiments
        self.positive_sentiments_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Sentiment'] == 1]

        # Create DataFrame for negative sentiments 
        self.negative_sentiments_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Sentiment'] == 0]

        
        ## Create DataFrames that is specific to the games a user wants to see
        # Note: These DataFrames only include the games that were a part of the CSV file.
        self.apex_legends_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'Apex Legends']

        self.counter_strike_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'Counter-Strike Global Offensive']

        self.DOTA_2_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'DOTA 2']

        self.GTA_V_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'GTA V']

        self.MIR_4_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'MIR4']

        self.monster_hunter_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'MONSTER HUNTER RISE']

        self.naraka_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'NARAKA: BLADEPOINT']

        self.PUBG_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'PlayerUnknowns Battlegrounds']

        self.RUST_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'RUST']

        self.team_fortress_df = self.cleaned_steam_file_df.loc[self.cleaned_steam_file_df['Game'] == 'Team Fortress2']

  

    ## Getting the number of positive and negative sentiments for each game (based on input)
        for game in [self.apex_legends_df, self.counter_strike_df, self.DOTA_2_df, self.GTA_V_df, self.MIR_4_df, self.monster_hunter_df, self.naraka_df, self.PUBG_df, self.RUST_df, self.team_fortress_df]:
            # Get the game name
            game_name = game['Game'].iloc[0]
            # Count the amount of positive sentiments per game
            positives = len(game.loc[game['Sentiment'] == 1])
            # Count the amount of negative sentiments per game
            negatives = len(game.loc[game['Sentiment'] == 0])
            self.game_positives[game_name] += positives
            self.game_negatives[game_name] += negatives

        
    ### Function to get review DataFrames based on sentiment input statement
    def getReviews(self, input):
        # All sentiments
        if input == 'All':
            print(f"Positive Sentiment Counter")
            print(self.game_positives)
            print("\n")
            print(f"Negative Sentiment Counter")
            print(self.game_negatives)
            print("\n")
            return self.cleaned_steam_file_df
        # Positive sentiments only
        elif input == 'Positive':
            print(f"Total number of positive sentiments per game")
            print("------------------------------------------------------------------------------------------------------------")
            print(f"The game with the most positive impact is: Counter-Strike: Global Offensive with 4964 positive Sentiments!")
            print("\n")
            print(self.game_positives)
            return self.positive_sentiments_df
        # Negative sentiments only
        elif input == 'Negative':
            print(f"Total number of negative sentiments per game")
            print("-----------------------------------------------------------------------------------------------------\n")
            print(f"The game with the most negative impact is: PlayerUnknown's Battlegrounds with 987 negative Sentiments!\n")
            print(self.game_negatives)
            return self.negative_sentiments_df
        # Incorrect inputs will cause the program to end
        else:
            print("Error: No DataFrame found.")
            quit()
            
        
       

    ## Fuction to get game DataFrames based on the second input statement
    def getGames(self, input):
        if input == 'Apex Legends':
            self.apex_positives = len(self.apex_legends_df.loc[self.apex_legends_df['Sentiment'] == 1])
            self.apex_negatives = len(self.apex_legends_df.loc[self.apex_legends_df['Sentiment'] == 0])
            # Creating a print statement to display each games negative and positve sentiment count
            print("Apex Legends Positve Sentiments: " + str(self.apex_positives))
            print("Apex Legends Negative Sentiments: " + str(self.apex_negatives))
            return self.apex_legends_df
        
        elif input == 'CSGO':
            self.counter_strike_positives = len(self.counter_strike_df.loc[self.counter_strike_df['Sentiment'] == 1])
            self.counter_strike_negatives = len(self.counter_strike_df.loc[self.counter_strike_df['Sentiment'] == 0])
            print("Counter-Strike Positve Sentiments: " + str(self.counter_strike_positives))
            print("Counter-Strike Negative Sentiments: " + str(self.counter_strike_negatives))
            return self.counter_strike_df
        
        elif input == 'DOTA 2':
            self.DOTA_positives = len(self.DOTA_2_df.loc[self.DOTA_2_df['Sentiment'] == 1])
            self.DOTA_negatives = len(self.DOTA_2_df.loc[self.DOTA_2_df['Sentiment'] == 0])
            print("DOTA 2 Positve Sentiments: " + str(self.DOTA_positives))
            print("DOTA 2 Negative Sentiments: " + str(self.DOTA_negatives))
            return self.DOTA_2_df
    
        elif input == 'GTA V':
            self.GTA_positives = len(self.GTA_V_df.loc[self.GTA_V_df['Sentiment'] == 1])
            self.GTA_negatives = len(self.GTA_V_df.loc[self.GTA_V_df['Sentiment'] == 0])
            print("GTA V Positve Sentiments: " + str(self.GTA_positives))
            print("GTA V Negative Sentiments: " + str(self.GTA_negatives))
            return self.GTA_V_df
        
        elif input == 'MIR4':
            self.MIR4_positives = len(self.MIR_4_df.loc[self.MIR_4_df['Sentiment'] == 1])
            self.MIR4_negatives = len(self.MIR_4_df.loc[self.MIR_4_df['Sentiment'] == 0])
            print("MIR4 Positve Sentiments: " + str(self.MIR4_positives))
            print("MIR4 Negative Sentiments: " + str(self.MIR4_negatives))
            return self.MIR_4_df
        
        elif input == 'Monster Hunter':
            self.monster_hunter_positives = len(self.monster_hunter_df.loc[self.monster_hunter_df['Sentiment'] == 1])
            self.monster_hunter_negatives = len(self.monster_hunter_df.loc[self.monster_hunter_df['Sentiment'] == 0])
            print("Monster Hunter Rise Positve Sentiments: " + str(self.monster_hunter_positives))
            print("Monster Hunter Rise Negative Sentiments: " + str(self.monster_hunter_negatives))
            return self.monster_hunter_df
        
        elif input == 'Naraka':
            self.naraka_positives = len(self.naraka_df.loc[self.naraka_df['Sentiment'] == 1])
            self.naraka_negatives = len(self.naraka_df.loc[self.naraka_df['Sentiment'] == 0])
            print("Naraka: BLADEPOINT Positve Sentiments: " + str(self.naraka_positives))
            print("Naraka: BLADEPOINT Negative Sentiments: " + str(self.naraka_negatives))
            return self.naraka_df
        
        elif input == 'PUBG':
            self.PUBG_positives = len(self.PUBG_df.loc[self.PUBG_df['Sentiment'] == 1])
            self.PUBG_negatives = len(self.PUBG_df.loc[self.PUBG_df['Sentiment'] == 0])
            print("PlayerUnknown's Battlegrounds Positve Sentiments: " + str(self.PUBG_positives))
            print("PlayerUnknown's Batlegrounds Negative Sentiments: " + str(self.PUBG_negatives))
            return self.PUBG_df
        
        elif input == 'RUST':
            self.RUST_positives = len(self.RUST_df.loc[self.RUST_df['Sentiment'] == 1])
            self.RUST_negatives = len(self.RUST_df.loc[self.RUST_df['Sentiment'] == 0])
            print("RUST Positve Sentiments: " + str(self.RUST_positives))
            print("RUST Negative Sentiments: " + str(self.RUST_negatives))
            return self.RUST_df
        
        elif input == 'Team Fortress 2':
            self.TF2_positives = len(self.team_fortress_df.loc[self.team_fortress_df['Sentiment'] == 1])
            self.TF2_negatives = len(self.team_fortress_df.loc[self.team_fortress_df['Sentiment'] == 0])
            print("Team Fortress 2 Positve Sentiments: " + str(self.TF2_positives))
            print("Team Fortress 2 Negative Sentiments: " + str(self.TF2_negatives))
            return self.team_fortress_df
        
        elif input == 'Any':
            print(self.game_positives)
            print(self.game_negatives)
            return self.cleaned_steam_file_df
        else:
            # End the Program immediatley if input a DataFrame that is not a part of the dataset or misinput
            print("Error: No DataFrame found.")
            quit()
















