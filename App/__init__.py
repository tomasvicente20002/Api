"""
The flask application package.
"""

from flask import Flask
import App.config as config
from App.Tables import dal


app = Flask(__name__)
configuration = config.Configuration()
conection = dal.SqlLiteConection(configuration)


import App.Views