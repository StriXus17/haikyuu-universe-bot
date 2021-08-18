from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route('/', methods=['POST'])
def result():
    print(request.json)

import os
import dialogflow
import random
import string
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "private_key.json"
project_id = "hinata-shoyo-ghey"
session_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
language_code = "en"
session_client = dialogflow.SessionsClient()
session = session_client.session_path(project_id, session_id)
text = "Hello"
text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
query_input = dialogflow.types.QueryInput(text=text_input)
response_dialogflow = session_client.detect_intent(session=session, query_input=query_input)
print(response_dialogflow)

# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
