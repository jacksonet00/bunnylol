import os
from flask import Flask, request, redirect
from redis import Redis

def create_app():
    app = Flask(__name__)
    app.debug = os.environ.get('ENV') != '__prod__'

    # r = Redis(host='redis', port=6379)

    # if os.environ.get('ENV') == '__dev__':
        # gen_data()

    # @app.route('/redis')
    # def redis():
    #     r.incr('hits')
    #     hits = r.get('hits')
    #     return f'This Compose/Flask demo has been viewed {hits} time(s).'

    @app.route('/search')
    def bunnylol():
        query = request.args.get('q')

        return redirect(f'https://google.com/search?q={query}')

    return app
