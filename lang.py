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
	at = tokens[1] if len(tokens) > 1 else "84601";
	dat = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + at + ",us&appid=2de143494c0b295cca9337e1e96b00e0").json()
	kelv = [dat["main"]["temp_min"], dat["main"]["temp"], dat["main"]["temp_max"]]
	fare = [str(round(9/float(5) * i  - 459.67, 2)) for i in kelv]
	description = dat["weather"][0]["main"] + ", (" + dat["weather"][0]["description"] + ")";
	result = "Temp (F): min: " + fare[0] + ", avg: " + fare[1] + ", max: " + fare[2] + ", descript: " + description;
	print result
	print len(result)

elif cmd == "hn":
	numStories = max(10, int(tokens[2]) if len(tokens) > 2 else 3);
	topStoriesIds = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
	storyTitles = [];
	for i in range(0, numStories):
		story = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(topStoriesIds[i]) + ".json").json()
		storyTitles.append("(" + story["title"] + ")")
	res = ', '.join(storyTitles);
	print res[0:min(len(res), 150)]

