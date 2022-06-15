from flask import Flask, render_template
import os

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route("/")
def home():
    # return "Hello, World!"
    return render_template('layouts/index.html')

if __name__ == "main":
    app.run(debug=True)