from flask import Flask, render_template
from flask_frozen import Freezer
import sys

app = Flask(__name__)

app.config['FREEZER_DESTINATION'] = 'docs'

@app.route("/")
def index():
    return render_template("index.html")

freezer = Freezer(app)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)