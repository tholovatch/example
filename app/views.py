from flask import jsonify
from flask.views import MethodView


def second_hello():
    return jsonify("second hello")


class ThirdHelloView(MethodView):
    def get(self):
        return jsonify("third hello")
