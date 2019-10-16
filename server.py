"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>Hi! This is the home page. 
    <a href="http://localhost:5000/hello">Hello</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <!-- HTML comment
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          compliment you want<select name="compliments">
          <option value="wonderful">Wonderful</option>
          <option value="smashing">smashing</option>
          <option value="lovely">lovely</option>
          <option value="fantabulous">Fantabulous</option>
          </select>
        

        </form>
        -->

        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit"><br>
          Want insults?
          <input type="checkbox" value="stupid" name="insults">Stupid
          <input type="checkbox" value="mediocre" name="insults">Mediocre</input>
          <input type="checkbox" value="fake" name="insults">Fake</input>
          <input type="checkbox" value="loser" name="insults">a loser!</input>
          
        </form>


      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")

    

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss")
def insult_person():
    """ Insult people upon their request """

    player = request.args.get("person")

    insult = request.args.get("insults")


    return """
    <!doctype html>
    <html>
      <head>
        <title>An insult</title>
      </head>
      <body>
        Hi, {}! I think you're {} {} {} {}!
      </body>
    </html>
    """.format(player, insult, insult, insult, insult)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
