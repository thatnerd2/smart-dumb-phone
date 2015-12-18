from flask import Flask, request, redirect
import twilio.twiml
from itertools import permutations
import requests;
import math
import random
 
app = Flask(__name__)
 

def messageHandler (m):
    tokens = m.split(" ")
    cmd = tokens[0].lower()
    if cmd == "p":
        return str(eval(' '.join(tokens[1::])))
    elif cmd == "hn":
        numStories = min(10, int(tokens[1]) if len(tokens) > 1 else 3);
        topStoriesIds = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
        storyTitles = [];
        for i in range(0, numStories):
            story = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(topStoriesIds[i]) + ".json").json()
            storyTitles.append("(" + story["title"] + ")")
        res = ', '.join(storyTitles);
        return res[0:min(len(res), 150)]
    elif cmd == "weather":
        at = tokens[1] if len(tokens) > 1 else "84601";
        dat = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + at + ",us&appid=2de143494c0b295cca9337e1e96b00e0").json()
        kelv = [dat["main"]["temp_min"], dat["main"]["temp"], dat["main"]["temp_max"]]
        fare = [str(round(9/float(5) * i  - 459.67, 2)) for i in kelv]
        description = dat["weather"][0]["main"] + ", (" + dat["weather"][0]["description"] + ")";
        result = "Temp (F): min: " + fare[0] + ", avg: " + fare[1] + ", max: " + fare[2] + ", descript: " + description;
        return result;
    else:
        return "Unrecognized command: " + m;


callers = {
    "+15185964072": "Aaron"
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)
    message_body = request.values.get('Body', None)
    if from_number in callers or message_body[0:6] == "PLEASE":
        if message_body[0:6] == "PLEASE":
            message_body = message_body[7::]
        message = messageHandler(message_body);
    else:
        message = "Do not text this number.  Fees will be incurred after 3 texts to this number."
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
