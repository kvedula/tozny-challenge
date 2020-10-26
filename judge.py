# Input to CL 
# 	python3 judge.py round=10 tozny-client-credentials-filepath=./clarence_creds.json

# Output to CL
# 	Round # Judged!

# Rock Paper Scissors Logic
# p1    p2   winner
# rock paper p2
# paper scissors p2
# scissors rock p2

# rock scissors p1
# paper rock p1
# scissors paper p1

import e3db
import sys
import json
from e3db.types import Search

if __name__ == '__main__':
	# print(sys.argv)
	roundNum = sys.argv[1].split('=')[1]
	path = sys.argv[2].split('=')[1]
	alicia_path = './alicia_creds.json'
	bruce_path = './bruce_creds.json'

	client = e3db.Client(json.load(open(path)))
	alicia_client = e3db.Client(json.load(open(alicia_path)))
	bruce_client = e3db.Client(json.load(open(bruce_path)))

	# Query for the data from the players inputs for the given round
	query = Search(include_data=True, include_all_writers=True).match(condition="AND", record_types=['move'], keys=['round'], values=[roundNum])
	results = client.search(query)

	player_move_dict = {}

	for r in results:
	   move = r.to_json()['data']['moveType']
	   name = r.to_json()['data']['name']

	   player_move_dict[name] = move

	# Fill in player move dict with the players moves for easier reference for the logic
	bruce_move = player_move_dict['bruce']
	alicia_move = player_move_dict['alicia']


	# Basic Rock Paper Scissors Logic to decide who wins
	if bruce_move == alicia_move:
		winner = "No Winner"

	elif (bruce_move == "rock" and alicia_move == "paper") or (bruce_move == "paper" and alicia_move == "scissors") or (bruce_move == "scissors" and alicia_move == "rock"):
		winner = "alicia"

	else:
		winner = "bruce"


	# Share a record with both players who won the round
	record_type = 'winner'
	data = {
	    'round' : roundNum, 
	  	'name': winner
	}

	metadata = {
	    'round' : roundNum, 
	  	'name': winner
	}

	# This was how I avoided an error that kept coming up, but I know there could be 
	# better ways to handle this which I would have given more time. Wanted to have 
	# a working solution to submit before playing around with the SDK more. 
	try:
		client.share(record_type, alicia_client.client_id)
		client.share(record_type, bruce_client.client_id)
	except:
		print('already initialized')
	record = client.write(record_type, data, metadata)

	print("Round {} Judged!".format(roundNum))















