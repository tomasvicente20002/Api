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
from App.Controllers.Aeroporto import Aeroporto
from App.Controllers.Aviao import Aviao
from App.Controlers.Chegada import Chegada
from App.Controlers.Passageiro import Passageiro
from App.Controlers.Partida import Partida
from App.Controllers.Voo import Voo
from App.Controllers.Voo_Passageiro import Voo_Passageiro

app = application = Flask(__name__)
configuration = config.Configuration()
conection = dal.SqlLiteConection(configuration)

#Gatantir que temos todas as tabelas para a aplicação não rebentar
conection.open_transaction()
f = open('./App/Tables/CreateTables.sql', 'r',encoding='utf_8_sig')
conection.execute_non_query(f.read())
f.close()
conection.commit()

app.url_map.strict_slashes = False
api = Api(app)
api.add_resource(Home, '/home')
api.add_resource(Aeroporto, '/aeroporto/','/aeroporto/<int:id>')
api.add_resource(Aviao, '/aviao/','/aviao/<int:id>')
api.add_resource(Chegada, '/chegada/','/chegada/<int:id>')
api.add_resource(Passageiro, '/passageiro/','passageiro/<int:id>')
api.add_resource(Partida, '/partida/','/partida/<int:id>')
api.add_resource(Voo, '/voo/','/voo/<int:id>')
api.add_resource(Voo_Passageiro, '/voo_passageiro/','/voo_passageiro/<int:id>')

#api.add_resource(Aeroporto, '/aeroporto')