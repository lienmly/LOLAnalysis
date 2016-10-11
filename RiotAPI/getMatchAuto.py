#=========================================
# Lien Ly - main functions file
# 
# Parse JSON data and create .csv for 
# R visualization 
#=========================================
from RiotAPI import RiotAPI
import RiotContants as Consts
import json

def automate_get_match():
    # Get the seed players'summoner ids
    summonerIds = {}
    with open("seedData/matches1.json") as json_file:
        json_data = json.load(json_file)
        for x in range(0, 100):
            for y in range(0, 10):
                summonerIds[10*x + y] = json_data["matches"][x]["participantIdentities"][y]["player"]["summonerId"]
    print("There are ",len(summonerIds)," seed players.")

    # Get one random match from each player's match history
    api = RiotAPI('314c9e1a-a062-40e0-acc4-c4ff55eefb2b')
    for x in range(0,len(summonerIds)):
        matchHistory = api.get_match_history(summonerIds[x])
        print("SummonerID: ",summonerIds[x])
        print("Length of match history is ",len(matchHistory["matches"]))

def getGoldFrames():
	print('Getting team gold at each frame of seed matches')
	
	# Open the file to save the output data in
	with open('outputData/matchGold.csv','w') as outfile:
		# Write the header
		outfile.write("match, timestamp, team1Gold, team2Gold, winner\n")
		
		# Go through each of the 10 seed files
		for fileNum in range(1,11):
			fileName = "seedData/matches"+str(fileNum)+".json"

			# Open the matches seed data
			with open(fileName) as json_file:
				json_data = json.load(json_file)

				for matchNumber in range(0, 100):
					print("Match "+str(matchNumber + (fileNum-1)*100))
					match = json_data["matches"][matchNumber]
					
					# Find the winning team
					winner = 100
					firstTeamWon = match["teams"][0]["winner"]
					if not firstTeamWon:
						winner = 200
					
					# What players in what team
					playerTeamMap = {}
					for participant in match["participants"]:
						pId = participant["participantId"]
						tId = participant["teamId"]
						# Map participant id to team id
						playerTeamMap[pId] = tId
					
					# Keep track of team gold at each frame (60 seconds)
					team1Gold = {}
					team2Gold = {}
					frames = match["timeline"]["frames"]
					for currentFrame in frames:
						timestamp = currentFrame["timestamp"]
						team1Gold[timestamp] = 0
						team2Gold[timestamp] = 0
						for pFrameKey in currentFrame["participantFrames"]:
							pFrame = currentFrame["participantFrames"][pFrameKey]
							totalGold = pFrame["totalGold"]
							if playerTeamMap[pFrame["participantId"]] == 100:
								team1Gold[timestamp] += totalGold
							else:
								team2Gold[timestamp] += totalGold
		
						for key in team1Gold:
							outfile.write(str(matchNumber + (fileNum-1)*100))
							outfile.write(", ")
							outfile.write(str(key)) # write the timestamp
							outfile.write(", ")
							outfile.write(str(team1Gold[key]))
							outfile.write(", ")
							outfile.write(str(team2Gold[key]))
							outfile.write(", ")
							outfile.write(str(winner)) # write which team won
							outfile.write("\n")
	