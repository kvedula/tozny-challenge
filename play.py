# Input Via CL
# 	python3 play.py round=1 name=alicia move=rock tozny-client-credentials-filepath=./alicia_creds.json

# Output to CL
# Round “#” Move “move” for “player" submitted!

import e3db
import sys
import json


if __name__ == '__main__':
	roundNum = sys.argv[1].split('=')[1]
	name = sys.argv[2].split('=')[1]
	move = sys.argv[3].split('=')[1]
	player_path = sys.argv[4].split('=')[1]
	judge_path = './clarence_creds.json'

	player_client = e3db.Client(json.load(open(player_path)))
	judge_client = e3db.Client(json.load(open(judge_path)))

	record_type = 'move'
	data = {
	    'round' : roundNum,
	  	'moveType': move,
	  	'name': name
	}

	metadata = {
	    'round' : roundNum, 
	  	'moveType': move,
	  	'name': name
	}

	# This was how I avoided an error that kept coming up, but I know there could be 
	# better ways to handle this which I would have given more time. Wanted to have 
	# a working solution to submit before playing around with the SDK more. 
	try:
		player_client.share(record_type, judge_client.client_id)
	except:
		print('already initialized')
	record = player_client.write(record_type, data, metadata)

	print("Round {} Move {} for {} submitted!".format(roundNum, move, name))



# Test CL operations
# python3 play.py round=10 name=alicia move=paper tozny-client-credentials-filepath=./alicia_creds.json
# python3 play.py round=10 name=bruce move=scissors tozny-client-credentials-filepath=./bruce_creds.json