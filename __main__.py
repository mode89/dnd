from flask import Flask
from flask import render_template

def index():
    return render_template("index.html")

if __name__ == "__main__":
    app = Flask(__name__)
    app.add_url_rule(rule="/", view_func=index)
    app.run(host="0.0.0.0")
