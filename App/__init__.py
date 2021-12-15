"""
The flask application package.
"""

from sqlite3.dbapi2 import Connection
from flask import Flask
import App.config as config
from App.Tables import dal
from flask_restful import Api
from App.Controllers.teste import UserRegister
from App.Controllers.home import Home
from App.helpers import combine_with_base_path
from App.Controllers import Aeroporto

app = application = Flask(__name__)
configuration = config.Configuration()
conection = dal.SqlLiteConection(configuration)

#Gatantir que temos todas as tabelas para a aplicação não rebentar
conection.open_transaction()
f = open('./App/Tables/CreateTables.sql', 'r',encoding='utf_8_sig')
conection.execute_non_query(f.read())
f.close()
conection.commit()


api = Api(app)
api.add_resource(UserRegister, '/items')
api.add_resource(Home, '/home')