from flask import Flask


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def welcome():
    return "Meditations & Perspectiion"


if __name__ == "__main__":
    app.run(debug=True)

