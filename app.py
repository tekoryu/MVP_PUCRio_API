from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """
    Aqui vai entrar na tela da OPenAPI, quando houver.
    """
    return "Hello, world!"

