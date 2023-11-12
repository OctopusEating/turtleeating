from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/We-like-kinoko")
def tanaka():
    return render_template("sora.html")

@app.route("/because-kinoko-is-very-delicious")
def index():
    return render_template("shakoeating.html")


app.run(host="0.0.0.0", port=5000)