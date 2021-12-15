from flask_restful import Resource
from App.Tables.Aeroporto import Aeroporto

class Aeroporto(Resource):

    def get(self,id):        
        aero = Aeroporto.get_by_pk_id(1)
        return aero.get_json()