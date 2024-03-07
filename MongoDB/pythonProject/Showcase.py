from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

uri = "mongodb+srv://SeanM:Xerials19@cafcon.fmjvvew.mongodb.net/?retryWrites=true&w=majority&appName=CAfcon"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.afcondb

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Function to retrieve player profile
def get_player_profile(player_name):
    player_profile = db.players.find_one({'name': player_name})
    return player_profile

# Function to retrieve match details
def get_match_details(team_name):
    team_matches = db.matches.find({'$or': [{'team_1': team_name}, {'team_2': team_name}]})
    return list(team_matches)

# Function to calculate and view statistics
def view_statistics():
    print("Statistics not implemented yet.")

# Main function for command-line interface
def main():
    print("Welcome to the MongoDB Database Showcase!")
    while True:
        print("\nMenu:")
        print("1. Query Player Profile")
        print("2. Retrieve Match Details")
        print("3. View Statistics")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            player_name = input("Enter player name: ")
            player_profile = get_player_profile(player_name)
            if player_profile:
                print("Player Profile:")
                print(player_profile)
            else:
                print(f"Player '{player_name}' not found.")
        elif choice == '2':
            team_name = input("Enter team name: ")
            match_details = get_match_details(team_name)
            if match_details:
                print("Match Details:")
                for match in match_details:
                    print(match)
            else:
                print(f"Team '{team_name}' not found.")
        elif choice == '3':
            view_statistics()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()