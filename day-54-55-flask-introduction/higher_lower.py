from flask import Flask
from random import randint

app = Flask(__name__)
answer = randint(0, 10)

@app.route("/")
def hello_world():
    return "<h1 style='color: orange'>Guess a numbah (0-10)!</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"

def check_numbah(func):
    # IMPORTANT: name of this parameter must be the same as the name of the variable in the route
    def wrapper(guess: int):
        if guess == answer:
            return "<h2 style='color: brown'>Correct!" + func() + "</h2>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"
        elif guess > answer:
            return "<h2 style='color: purple'>Too high" + "</h2>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
        else:
            return "<h2 style='color: red'>Too low" + "</h2>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    return wrapper

# IMORTANT: name of this variable must be the same name as the parameter in the decorator!
@app.route("/<int:guess>")
@check_numbah
def guessed_number():
    return "You win!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)