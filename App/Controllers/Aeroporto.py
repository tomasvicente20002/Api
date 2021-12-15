from sqlite3.dbapi2 import connect
from flask_restful import Resource
from App.Tables.Aeroporto import Aeroporto as table_aeroporto
import App.config as config
from App.Tables import dal


class Aeroporto(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    
    def get(self,id):
        Aeroporto.conection.open_conection()
        aero = table_aeroporto()
        aero.get_by_pk_id(1,Aeroporto.conection)
        return aero.get_json()

    