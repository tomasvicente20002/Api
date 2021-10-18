"""
The flask application package.
"""

from flask import Flask

#extra variable for aws web server
application = app = Flask(__name__)

import App.views
