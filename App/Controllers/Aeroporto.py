from flask_restful import Resource,reqparse
from App.Tables.Aeroporto import Aeroporto as table_aeroporto
import App.config as config
from App.Tables import dal


class Aeroporto(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    parser = reqparse.RequestParser()
    table_aeroporto().add_args(parser)


    #obter registo
    def get(self,id):
        Aeroporto.conection.open_conection()
        aero = table_aeroporto()
        aero.get_by_pk_id(id,Aeroporto.conection)
        return aero.get_json()

    #inserir registo
    def post(self):
        data = Aeroporto.parser.parse_args()
        aero = table_aeroporto()
        aero.read_from_args(data)
        Aeroporto.conection.open_conection()
        aero.insert(Aeroporto.conection)
        Aeroporto.conection.commit()
        return {'message': 'Record created successfully.'}, 201


    