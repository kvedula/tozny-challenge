# Input to CL
# 	python3 winner.py round=10 tozny-client-credentials-filepath=./bruce_creds.json

# Output to CL
#  Round # Winner "player name"

import e3db
import sys
import json
from e3db.types import Search


if __name__ == '__main__':
	roundNum = sys.argv[1].split('=')[1]
	path = sys.argv[2].split('=')[1]

	client = e3db.Client(json.load(open(path)))

	# Search for who the judge dictated was the winner for the given round
	query = Search(include_data=True, include_all_writers=True).match(condition="AND", record_types=['winner'], keys=['round'], values=[roundNum])
	results = client.search(query)

	for r in results:
	   winner = r.to_json()['data']['name']

	print("Round {} Winner {}".format(roundNum, winner))



