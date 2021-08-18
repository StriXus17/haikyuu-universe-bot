from flask import Flask, render_template, request
import os
import json
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
    global fyodor
    global dazai
    print(request.json['query_input']['text']['text'])
    fyodor = request.json['query_input']['text']['text']
    dazai = request.json['query_input']['text']['id']
    import dialogflow
    import random
    import string
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "private_key.json"
    project_id = dazai
    session_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    language_code = "en"
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text = fyodor
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response_dialogflow = session_client.detect_intent(session=session, query_input=query_input)
    return response_dialogflow

    # Here's how you create a route
    # @app.route("/routeName")
    # def functionName():
    #    return render_template("fileName.html")
port = int(os.environ.get("PORT", 17995))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
