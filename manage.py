from os import environ
from app import create_app

app = create_app()

port = environ.get('PORT')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
