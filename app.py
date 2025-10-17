from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/roll')
def roll_dice():
    return jsonify({"result": random.randint(1, 6)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
