from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 

def messageHandler (m):
    tokens = m.split(" ")
    cmd = tokens[0]
    if cmd == "p":
        return str(eval(' '.join(tokens[1::])))
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
    if from_number in callers:
        message = messageHandler(message_body);
    else:
        message = "Do not text this number.  Fees will be incurred after 3 texts to this number."
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
