from flask import Flask
from flask_ask import Ask

app = Flask(__name__)
ask = Ask(app,'/')

@app.route("/")
def homepag():
    return "Estou aqui"

@ask.launch
def start_skill():
    welcome_message = "Olá, como posso ajudar você?"
    return question(welcome_message).repromt("Consigo te enviar lembretes de remédios e buscar por bulas na Internet")

@ask.session_ended
def session_ended():
    return "{}", 200
if __name__=="__main__":
    app.run(debug=True)
