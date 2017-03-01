from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello")
def hello():
    return jsonify("Hello World!")


@app.route("/multiplicate")
def multiplicate():
    x = int(request.args.get('x', 1))
    y = int(request.args.get('y', 2))
    return jsonify(x*y)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
