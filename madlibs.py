from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)




@app.route('/game')
def show_game_form():
    playgame =request.args.get("playgame")
    if playgame == "yes":
        game= choice(["game1.html", "game2.html"])
        return render_template(game)
    else:
        return render_template("goodbye.html")

@app.route('/madlib1')
def show_madlib():
    person = request.args.get("Person")
    color = request.args.get("Color")
    noun = request.args.get("Noun")
    adjective = request.args.get("Adjective")
    pets = request.args.getlist("pets")
    print pets

    if person == "Barack Obama" or person == "Santa Claus":
        pronoun= "his"
    else:
        pronoun="her"
    
    num_pets = len(pets)

    
    return render_template("madlib1.html", person=person, color=color, noun=noun, adjective=adjective, pets=pets, pronoun=pronoun, num_pets=num_pets)

@app.route('/madlib2')
def show_madlib2():
    country = request.args.get("Country")
    food = request.args.get("Food")
    action = request.args.get("Action")

    return render_template("madlib2.html",country=country, food=food, action=action)
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
