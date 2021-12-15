from flask_restful import Resource,reqparse
from App.Tables.Voo_Passageiro import Voo_Passageiro as table_voo_passageiro
import App.config as config
from App.Tables import dal


class Voo_Passageiro(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    parser = reqparse.RequestParser()
    table_voo_passageiro().add_args(parser)


    #obter registo
    def get(self,id):
        Voo_Passageiro.conection.open_conection()
        voo_passageiro = table_voo_passageiro()
        voo_passageiro.get_by_pk_id(id,Voo_Passageiro.conection)
        return voo_passageiro.get_json()

    #inserir registo
    def post(self):
        data = Voo_Passageiro.parser.parse_args()
        voo_passageiro = table_voo_passageiro()
        voo_passageiro.read_from_args(data)
        Voo_Passageiro.conection.open_conection()
        voo_passageiro.update(Voo_Passageiro.conection)
        Voo_Passageiro.conection.commit()
        return {'message': 'Record created successfully.'}, 201
