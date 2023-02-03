from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hehe Boy!</p>"
    return "<h1> testando meu semi deploy </h1>"
