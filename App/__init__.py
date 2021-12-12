"""
The flask application package.
"""

from flask import Flask
import App.config as config
from App.Tables import dal
from flask_restful import Api
from App.Controllers.teste import UserRegister


app = application = Flask(__name__)
configuration = config.Configuration()
conection = dal.SqlLiteConection(configuration)
api = Api(app)
api.add_resource(UserRegister, '/items')