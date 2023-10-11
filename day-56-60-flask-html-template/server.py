from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html") 


@app.route("/login", methods=["POST"])
def receive_data():
    if request.method == 'POST':
        return f"Hello {request.form['name']}! Nice password: {request.form['pasw']}"
    return "a string, not a POST"



if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    # If access denied (403), change the port and run again
    app.run(port=8000, debug=True)