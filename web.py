from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create")
def create_game():
    return render_template('create-game.html')

@app.route("/join")
def join_game():
    return render_template('join-game.html')


if __name__=="__main__":
   app.run(debug=True) #Flask listen on port 5000 by default
