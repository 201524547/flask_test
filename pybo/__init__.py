from flask import Flask
app = Flask(__name__)
def create_app():
    app = Flask(__name__)
    print("aaa")

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app