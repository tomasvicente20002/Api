"""
This script runs the RC application using a development server.
"""

from os import environ
from App import app,conection
from App.Tables import voos
from flask import render_template
from App import conection

tables = conection.execute_query('''SELECT 
                                name
                            FROM 
                                sqlite_master 
                            WHERE 
                                type ='table' AND 
                                name NOT LIKE 'sqlite_%';''')

for row in tables:
    table = row[0]
    fields = conection.execute_query(f'pragma table_info({table});')

    for row_column in fields:
        print(row_column[1])
        print(row_column[2])


files  = []
teste = render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


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