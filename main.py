
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

uri = "mongodb+srv://SeanM:Xerials19@cafcon.fmjvvew.mongodb.net/?retryWrites=true&w=majority&appName=CAfcon"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.Afcon_db

matchesdata = [
    {
        "team_1": "Mali",
        "team_2": "Burkina Faso",
        "score_team1": 2,
        "score_team2": 1,
        "date": datetime(2023, 1, 30)
    },
    {
        "team_1": "Mali",
        "team_2": "Côte d'Ivoire",
        "score_team1": 1,
        "score_team2": 2,
        "date": datetime(2023, 2, 3)
    },
    {
        "team_1": "Côte d'Ivoire",
        "team_2": "Congo DR",
        "score_team1": 1,
        "score_team2": 0,
        "date": datetime(2023, 2, 7)
    },
    {
        "team_1": "Congo DR",
        "team_2": "Guinea",
        "score_team1": 3,
        "score_team2": 1,
        "date": datetime(2023, 2, 2)
    },
    {
        "team_1": "South Africa",
        "team_2": "Congo DR",
        "score_team1": 6,
        "score_team2": 5,
        "date": datetime(2023, 2, 10)
    },
    {
        "team_1": "Nigeria",
        "team_2": "Côte d'Ivoire",
        "score_team1": 1,
        "score_team2": 2,
        "date": datetime(2023, 2, 11)
    },
    {
        "team_1": "Nigeria",
        "team_2": "South Africa",
        "score_team1": 5,
        "score_team2": 3,
        "date": datetime(2023, 2, 7)
    },
    {
        "team_1": "Nigeria",
        "team_2": "Angola",
        "score_team1": 1,
        "score_team2": 0,
        "date": datetime(2023, 2, 3)
    },
    {
        "team_1": "Cabo Verde",
        "team_2": "South Africa",
        "score_team1": 1,
        "score_team2": 2,
        "date": datetime(2023, 2, 3)
    },
    {
        "team_1": "Congo DR",
        "team_2": "Guinea",
        "score_team1": 3,
        "score_team2": 1,
        "date": datetime(2023, 2, 2)
    },
    {
        "team_1": "Senegal",
        "team_2": "Côte d'Ivoire",
        "score_team1": 5,
        "score_team2": 6,
        "date": datetime(2023, 1, 29)
    },
    {
        "team_1": "Team B",
        "team_2": "Team A",
        "score_team1": 0,
        "score_team2": 3,
        "date": datetime(2023, 1, 5)
    },
    {
        "team_1": "Egypt",
        "team_2": "Congo DR",
        "score_team1": 8,
        "score_team2": 9,
        "date": datetime(2023, 1, 28)
    },
    {
        "team_1": "Equatorial Guinea",
        "team_2": "Guinea",
        "score_team1": 0,
        "score_team2": 1,
        "date": datetime(2023, 1, 28)
    },
    {
        "team_1": "Morocco",
        "team_2": "South Africa",
        "score_team1": 0,
        "score_team2": 2,
        "date": datetime(2023, 1, 30)
    },
    {
        "team_1": "Cabo Verde",
        "team_2": "Mauritania",
        "score_team1": 1,
        "score_team2": 0,
        "date": datetime(2023, 1, 5)
    },
    {
        "team_1": "Nigeria",
        "team_2": "Cameroon",
        "score_team1": 2,
        "score_team2": 0,
        "date": datetime(2023, 1, 5)
    },
    {
        "team_1": "Angola",
        "team_2": "Namibia",
        "score_team1": 3,
        "score_team2": 0,
        "date": datetime(2023, 1, 5)
    }
]

db.matches.insert_many(matchesdata)

playerdata = [
    {
        "name": "Emilio Nsue",
        "team": "Equ. Guinea",
        "position": "FW",
        "goals_scored": 5,
        "assists": 0
    },
    {
        "name": "Gelson",
        "team": "Angola",
        "position": "FW,MF",
        "goals_scored": 4,
        "assists": 1
    },
    {
        "name": "Mostafa Mohamed",
        "team": "Egypt",
        "position": "FW",
        "goals_scored": 4,
        "assists": 0
    },
    {
        "name": "Ademola Lookman",
        "team": "Nigeria",
        "position": "FW",
        "goals_scored": 3,
        "assists": 1
    },
    {
        "name": "Baghdad Bounedjah",
        "team": "Algeria",
        "position": "FW",
        "goals_scored": 3,
        "assists": 0
    },
    {
        "name": "Mohamed Lamine Bayo",
        "team": "Guinea",
        "position": "FW",
        "goals_scored": 3,
        "assists": 0
    },
    {
        "name": "Mabululu",
        "team": "Angola",
        "position": "FW",
        "goals_scored": 3,
        "assists": 0
    },
    {
        "name": "Lassine Sinayoko",
        "team": "Mali",
        "position": "FW",
        "goals_scored": 3,
        "assists": 0
    },
    {
        "name": "Bertrand Traoré",
        "team": "Burkina Faso",
        "position": "MF,FW",
        "goals_scored": 3,
        "assists": 0
    },
    {
        "name": "William Troost-Ekong",
        "team": "Nigeria",
        "position": "DF",
        "goals_scored": 3,
        "assists": 0
    },


    {
        "name": "Jordan Ayew",
        "team": "Ghana",
        "position": "MF",
        "goals_scored": 2,
        "assists": 1
    },
    {
        "name": "Franck Kessié",
        "team": "Côte d'Ivoire",
        "position": "MF",
        "goals_scored": 2,
        "assists": 1
    },
    {
        "name": "Ryan Mendes",
        "team": "Cape Verde",
        "position": "FW,MF",
        "goals_scored": 2,
        "assists": 1
    },
    {
        "name": "Teboho Mokoena",
        "team": "South Africa",
        "position": "MF",
        "goals_scored": 2,
        "assists": 1
    },
    {
        "name": "Themba Zwane",
        "team": "South Africa",
        "position": "MF,FW",
        "goals_scored": 2,
        "assists": 1
    },
    {
        "name": "Lamine Camara",
        "team": "Senegal",
        "position": "MF",
        "goals_scored": 2,
        "assists": 0
    },
    {
        "name": "Habib Diallo",
        "team": "Senegal",
        "position": "FW",
        "goals_scored": 2,
        "assists": 0
    },
    {
        "name": "Sébastien Haller",
        "team": "Côte d'Ivoire",
        "position": "FW",
        "goals_scored": 2,
        "assists": 0
    },
    {
        "name": "Kudus Mohammed",
        "team": "Ghana",
        "position": "MF",
        "goals_scored": 2,
        "assists": 0
    },
    {
        "name": "Yoane Wissa",
        "team": "Congo DR",
        "position": "MF",
        "goals_scored": 2,
        "assists": 0
    },
    {
        "name": "Sadio Mané",
        "team": "Senegal",
        "position": "FW",
        "goals_scored": 1,
        "assists": 3
    },
    {
        "name": "Simon Adingra",
        "team": "Côte d'Ivoire",
        "position": "FW",
        "goals_scored": 1,
        "assists": 2
    },
    {
        "name": "Ismaila Sarr",
        "team": "Senegal",
        "position": "FW",
        "goals_scored": 1,
        "assists": 2
    },
    {
        "name": "Trézéguet",
        "team": "Egypt",
        "position": "MF,FW",
        "goals_scored": 1,
        "assists": 2
    },
    {
        "name": "Gilson Benchimol",
        "team": "Cape Verde",
        "position": "FW",
        "goals_scored": 1,
        "assists": 1
    },
    {
        "name": "Geny Catamo",
        "team": "Mozambique",
        "position": "MF,FW",
        "goals_scored": 1,
        "assists": 1
    },
    {
        "name": "Patson Daka",
        "team": "Zambia",
        "position": "FW",
        "goals_scored": 1,
        "assists": 1
    },
    {
        "name": "Meschak Elia",
        "team": "Congo DR",
        "position": "MF",
        "goals_scored": 1,
        "assists": 1
    },
    {
        "name": "Seko Fofana",
        "team": "Côte d'Ivoire",
        "position": "MF,FW",
        "goals_scored": 1,
        "assists": 1
    },
    {
        "name": "Pablo Ganet",
        "team": "Equ. Guinea",
        "position": "MF",
        "goals_scored": 1,
        "assists": 1
    },
]

db.players.insert_many(playerdata)