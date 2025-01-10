from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 
    
with app.test_request_context():
    rendered = app.full_dispatch_request().data.decode()
    with open("templates/index.html", "w") as f:
        f.write(rendered)