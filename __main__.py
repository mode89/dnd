from flask import Flask

def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app = Flask(__name__)

    app.add_url_rule(rule="/", view_func=hello_world)

    app.run()
