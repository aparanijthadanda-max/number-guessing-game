
import flask
import random

app = flask.Flask(__name__)

secret_number = random.randint(1, 10)
attempts = 0
message = "Guess a number between 1 and 10!"

@app.route("/", methods=["GET", "POST"])
def home():
    global secret_number, attempts, message

    if flask.request.method == "POST":
        guess = int(flask.request.form["guess"])
        attempts += 1

        if guess > secret_number:
            message = "Too high! Try again."
        elif guess < secret_number:
            message = "Too low! Try again."
        else:
            message = f"Correct! You won in {attempts} attempts!"

    return flask.render_template(
        "index.html",
         message=message,
         attempts=attempts
    )
    

if __name__ == "__main__":
    app.run(host="127.0.0.1",
port=5000, debug=True)