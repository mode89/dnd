from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

def index():
    return render_template("index.html")

if __name__ == "__main__":
    app = Flask(__name__)
    Bootstrap(app)

    app.add_url_rule(rule="/", view_func=index)

    app.run()
