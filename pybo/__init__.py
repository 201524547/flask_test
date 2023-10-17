from flask import Flask, request

app = Flask(__name__)
def create_app():
    app = Flask(__name__)

    @app.route('/', methods=["POST", "GET"])
    def index():
        if (request.method == "POST"):
            resp = request.get_json()
            print(resp)

    return "Done"

    return app