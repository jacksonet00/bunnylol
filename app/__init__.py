from os import environ
from flask import Flask, request, redirect

# from constants import alias_table # Dict[str: str] alias => url

alias_table = {
    'wiki': 'https://www.notion.so/Personal-wiki-ea4d169a831b4a879221f8e45166f3d7',
    'mail': 'https://app.hey.com',
    'roth': 'https://us.etrade.com/etx/pxy/portfolios/positions',
    'edu': 'https://www.notion.so/Education-a19fd25b27604a24b0a9c4b578439de4',
    'canvas': 'https://ufl.instructure.com/',
    'tasks': 'https://www.notion.so/Tasks-fdfed7742ac54430b286ce9ca60b1d1f',
    'task': 'https://www.notion.so/Tasks-fdfed7742ac54430b286ce9ca60b1d1f',
    't': 'https://www.notion.so/Tasks-fdfed7742ac54430b286ce9ca60b1d1f',
    'cal': 'https://calendar.google.com',
}

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
