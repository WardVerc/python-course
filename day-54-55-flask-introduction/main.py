## Library: you use a function of that module
## Framework: you need to use the architecture and follow the rules of that framework on how to use it

## Flask is a (beginner friendly) framework to make a Python back-end for web applications
## Django is the same, but used for bigger projects


## Virtual environments are independent groups of Python libraries, one for each project. 
## Packages installed for one project will not affect other projects or the operating system’s packages.

## OPTIONAL:
## 1) First make a virtual environment (venv) for Flask:
## Run this command in your project folder: python3 -m venv .venv
## 2) Then activate the environment: . .venv/bin/activate
## 3) Finally install Flask in the activated env: pip3 install Flask

## We only did the last command here

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# ------------------------ make bold decorator ------------------------ #

# This is, like @app.route(), a Python decorator
# It takes a function, adds functionality to that function, 
# wraps it in a function and returns that wrapper function:
def make_bold(func):
    def wrapper_func():
        return '<b>' + func() + '</b>'
    return wrapper_func

@app.route("/bye")
# Now we can add this decorator to any function
@make_bold
def bye():
    return "Salu maateke"

# ------------------------ is_authenticated_decorator ------------------------ #
class User:
    def __init__(self, name: str):
        self.name = name
        self.is_logged_in = False # set this to True and create_blog_post will run as you can see in the decorator func

def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Ward")
create_blog_post(new_user)

# ------------------------ ------------------------- ------------------------ #

# With this block we can run this python file like other python files
# Else, we have to run the command: flask --app main run
# (with 'main' as the name of your file)
if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)