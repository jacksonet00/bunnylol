from os import environ
from flask import Flask, request, redirect

from constants import alias_table # Dict[str: str] alias => url

def create_app():
    app = Flask(__name__)
    app.debug = environ.get('ENV') != '__prod__'

    @app.route('/search')
    def bunnylol():
        query = request.args.get('q')

        # alias redirect
        if query in alias_table:
            return redirect(alias_table[query])
        
        # github search
        if query[:3] == 'gh ':
            return redirect(f'https://github.com/search?q={query[3:]}')
        
        # wikipedia search
        if query[:2] == 'w ':
            return redirect(f'https://en.wikipedia.org/w/index.php?search={query[2:]}')
        
        # stack overflow search
        if query[:3] == 'so ':
            return redirect(f'https://stackoverflow.com/search?q={query[3:]}')
        
        # amazon search
        if query[:2] == 'a ':
            return redirect(f'https://www.amazon.com/s?k={query[2:]}')

        # fallback to google search by default
        return redirect(f'https://google.com/search?q={query}')

    return app
