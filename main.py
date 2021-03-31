from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"hello": "world"})

@app.route("/form", methods=["POST"])
def save_form():
    foo = request.form.get("foo")
    bar = request.form.get("bar")
    response = Response("This is a test response")
    response.headers["X-foo-bar"] = "{}; {}".format(foo, bar)
    return response
