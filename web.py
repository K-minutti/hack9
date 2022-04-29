from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create")
def create_game_page():
    return render_template('create-game.html')

@app.route("/create/<gameinfo>")
def create_game(gameinfo):
    print(gameinfo)
    return jsonify({"game_link": 'https://google.com'})

@app.route("/join")
def join_page():
    return render_template('join-game.html')

@app.route("/join/<gamelink>")
def join_game(gamelink):
    print(gamelink)
    # route to game and redirect
    return jsonify({"status": 200})

if __name__=="__main__":
   app.run(host="localhost", port="8080", debug=True) #Flask listen on port 5000 by default
