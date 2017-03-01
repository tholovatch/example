from flask import Flask, request, jsonify
from app.views import second_hello, ThirdHelloView

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify("Hello World!")


@app.route("/multiplicate")
def multiplicate():
    x = int(request.args.get('x', 1))
    y = int(request.args.get('y', 2))
    return jsonify(x*y)


app.add_url_rule('/second_hello', 'second_hello', second_hello)

app.add_url_rule('/third_hello', view_func=ThirdHelloView.as_view('third_hello'))



if __name__ == "__main__":
    app.run(host='0.0.0.0')
