from flask_restful import Resource,reqparse
from App.Tables.Voo import Voo as table_voo
import App.config as config
from App.Tables import dal


class Voo(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    parser = reqparse.RequestParser()
    table_voo().add_args(parser)


    #obter registo
    def get(self,id):
        Voo.conection.open_conection()
        voo = table_voo()
        voo.get_by_pk_id(id,Voo.conection)
        return voo.get_json()

    #inserir registo
    def post(self):
        data = Voo.parser.parse_args()
        voo = table_voo()
        voo.read_from_args(data)
        Voo.conection.open_conection()
        voo.update(Voo.conection)
        Voo.conection.commit()
        return {'message': 'Record created successfully.'}, 201
