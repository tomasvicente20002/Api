from flask_restful import Resource,reqparse
from App.Tables.Passageiro import Passageiro as table_passageiro
import App.config as config
from App.Tables import dal


class Passageiro(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    parser = reqparse.RequestParser()
    table_passageiro().add_args(parser)


    #obter registo
    def get(self,id):
        Passageiro.conection.open_conection()
        passageiro = table_passageiro()
        passageiro.get_by_pk_id(id,Passageiro.conection)
        return passageiro.get_json()

    #inserir registo
    def post(self):
        data = Passageiro.parser.parse_args()
        passageiro = table_passageiro()
        passageiro.read_from_args(data)
        Passageiro.conection.open_conection()
        passageiro.update(Passageiro.conection)
        Passageiro.conection.commit()
        return {'message': 'Record created successfully.'}, 201