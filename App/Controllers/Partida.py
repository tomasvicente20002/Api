from flask_restful import Resource,reqparse
from App.Tables.Partida import Partida as table_partida
import App.config as config
from App.Tables import dal


class Partida(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    parser = reqparse.RequestParser()
    table_partida().add_args(parser)


    #obter registo
    def get(self,id):
        Partida.conection.open_conection()
        partida = table_partida()
        partida.get_by_pk_id(id,Partida.conection)
        return partida.get_json()

    #inserir registo
    def post(self):
        data = Partida.parser.parse_args()
        partida = table_partida()
        partida.read_from_args(data)
        Partida.conection.open_conection()
        partida.update(Partida.conection)
        Partida.conection.commit()
        return {'message': 'Record created successfully.'}, 201