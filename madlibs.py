"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Does the user want to play a game."""



# if request is yes, render game.html template
# if no, render template goodbye.html
 
 # what we need to do next: color, noun, nombre, adjective
    response = request.args.get("answer")



    if response == "yes":
        return render_template("game.html")
        # do we need extra arguments?
        # We don't think so ...

    if response == "no":
        return render_template("goodbye.html")    

@app.route('/madlib')
def show_madlib():
    return render_template("madlib.html",
                            color=request.args.get("color"),
                            noun=request.args.get("noun"),
                            name=request.args.get("nombre"),
                            adjective=request.args.get("adjective")
                            )

# from flask import render_template
# from random import choice

# COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

# @app.route('/greet')
# def greet_person():
#     """Return customized compliment along with person name."""

#     player = request.args.get("person")
#     nice_thing = choice(COMPLIMENTS)
#     return render_template("compliment.html",
#                            name=player,
#                            compliment=nice_thing)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
