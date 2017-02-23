import falcon
import waitress

from app.views import HelloView, MultiplicationView

api = falcon.API()

api.add_route('/', HelloView())
api.add_route('/multiplication', MultiplicationView())

if __name__ == '__main__':
    waitress.serve(api, port=5000)
