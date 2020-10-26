# Tozny RPS Game

Tozny RPS(Rock-Paper-Scissors) is a back-end game that runs via CL developed for the Tozny final round interview

## Setup

Go to Tozny's e3db GitHub page: [e3db](https://github.com/tozny/e3db-python)

To install e3db for usage follow the documentation on the page or simply run this in your preferred CL
```git
$ pip3 install e3db
```

## Usage
First clone this repository, then
Navigate to the tozny-challenge repository on your computer via these following commands

```bash
$ git clone https://github.com/kvedula/tozny-challenge.git
$ cd tozny-challenge
```

Now all the config files are already set up for use by the application. The following commands should be done in the exact order to play the game properly.

Start with round=10 as I used the previous rounds for testing.

```bash
$ python3 play.py round=10 name=alicia move=paper tozny-client-credentials-filepath=./alicia_creds.json
# Should return: Round 10 Move paper for alicia submitted!

$ python3 play.py round=10 name=bruce move=scissors tozny-client-credentials-filepath=./bruce_creds.json
# Should return: Round 10 Move scissors for bruce submitted!

$ python3 judge.py round=10 tozny-client-credentials-filepath=./clarence_creds.json
# Should return: Round 10 Judged!

$ python3 winner.py round=10 tozny-client-credentials-filepath=./bruce_creds.json
# Should return: Round 10 Winner bruce
```

## Summary
This is a very simple version of the RPS game done via Tozny's SDK. Have fun playing around with it and testing it out! I had a great time coding this over the past couple days.
