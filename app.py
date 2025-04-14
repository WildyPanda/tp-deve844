from flask import Flask, request
import requests

FIREBASE_DB_URL = "https://tp-cloud-deve844-91f46-default-rtdb.europe-west1.firebasedatabase.app/messages.json"

app = Flask(__name__)

@app.route('/')
def index():
    res = """
    <h2>Bienvenue sur votre app Flask hébergée sur Render !</h2> \n
    <form action="/form" method="POST">
        <label for="nom">Nom :</label><br>
        <input type="text" id="nom" name="nom"><br>
        <label for="message">Message :</label><br>
        <input type="text" id="message" name="message"><br><br>
        <input type="submit" value="Envoyer">
    </form>"""
    return res

@app.route('/form', methods=['POST'])
def index(data):
    requests.post(FIREBASE_DB_URL, json=data)
    return "ok"

@app.route('/all', methods=['GET'])
def index():
    response = requests.get(FIREBASE_DB_URL)
    if response.ok:
        messages = response.json()
        res = ""
        for k, msg in messages.items():
            res += f"- {msg['nom']}: {msg['message']}"
        return res
    else:
        return "Erreur lors de la lecture :" + response.text

@app.route('/hello', methods=['GET'])
def hello():
    return {"message": "Bonjour depuis Render Flask API"}
