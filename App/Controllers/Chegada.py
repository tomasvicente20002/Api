from flask_restful import Resource,reqparse
from App.Tables.Chegada import Chegada as table_chegada
import App.config as config
from App.Tables import dal


class Chegada(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    parser = reqparse.RequestParser()
    table_chegada().add_args(parser)


    #obter registo
    def get(self,id):
        Chegada.conection.open_conection()
        chegada = table_chegada()
        chegada.get_by_pk_id(id,Chegada.conection)
        return chegada.get_json()

    #inserir registo
    def post(self):
        data = Chegada.parser.parse_args()
        chegada = table_chegada()
        chegada.read_from_args(data)
        Chegada.conection.open_conection()
        chegada.update(Chegada.conection)
        Chegada.conection.commit()
        return {'message': 'Record created successfully.'}, 201


    