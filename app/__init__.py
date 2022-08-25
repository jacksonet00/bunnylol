from os import environ
from flask import Flask, request, redirect
from constants import alias_table

def create_app():
    app = Flask(__name__)
    app.debug = environ.get('ENV') != '__prod__'

    @app.route('/search')
    def bunnylol():
        query = request.args.get('q')

        if query in alias_table:
            return redirect(alias_table[query])
        
        if query[:2] == 'gh':
            return redirect(f'https://github.com/search?q={query[2:]}')

        return redirect(f'https://google.com/search?q={query}')

    return app
