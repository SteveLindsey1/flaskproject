# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
     return render_template("index.html")
      




@app.route('/results', methods=['GET', 'POST'])
def fightinggame():
    user_game = request.form["game"]
    print(user_game)
    if user_game =="fighting game":
        return render_template("fighting_game.html")
    # return "fighting game "
    elif user_game =="first person shooter":
         return render_template("first_person_shooter.html")
    elif user_game =="platformer":
        return render_template("platformer.html")

        
    



@app.route('/first person shooter')
def firstpersonshooter():
    return "you have arrived to the first person co-op shooter game called Call of duty it's competiteve online game that pairs up players from around the world to put their skill in war to the test"




@app.route('/platformer')
def platformer():
    return "This is the platformer called mario Odyessey! it's an open world 3D platformer that star's the famous character Mario here to save the princess once more"




