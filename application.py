"""
This script runs the RC application using a development server.
"""

from os import environ
from App import app,conection
from App.Tables.Aeroporto import Aeroporto
from App import conection

aero = Aeroporto()
aero.get_by_pk_id(1,conection)

if __name__ == '__main__':
    if __debug__:     
        HOST = environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555
            
        app.debug = True
        app.run(HOST, PORT)
    else:
        app.run(host='0.0.0.0')    