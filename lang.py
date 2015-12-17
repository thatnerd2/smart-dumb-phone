import sys
import requests;
import json
from flask import jsonify

if len(sys.argv) == 1:
	print "Usage: python lang-sandbox.py \"<command>\"";
	sys.exit()

tokens = sys.argv[1].split(" ")
cmd = tokens[0]

## Hardcode possible commands
if cmd == "echo":
	print ' '.join(tokens[1::])
elif cmd == "p":
	print str(eval(' '.join(tokens[1::])))
elif cmd == "weather":
	if len(tokens > 2):
		at = tokens[2];
	print "weather not supported yet"
elif cmd == "hn":
	if len(tokens) > 2:
		numStories = int(tokens[2])

print jsonify(requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json())
