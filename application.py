"""
This script runs the RC application using a development server.
"""

from os import environ, truncate
from re import A
from App import app,application


if __name__ == '__main__':
    if __debug__:     
        HOST = environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555

        application.debug = True
        app.run(HOST, PORT)
    else:
        application.run(host='0.0.0.0')





        print("A seguir a revisão dos testes, Tomás tiveste 8.")