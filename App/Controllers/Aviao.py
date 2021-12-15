from flask_restful import Resource,reqparse
from App.Tables.Aviao import Aviao as table_aviao
import App.config as config
from App.Tables import dal


class Aviao(Resource):
    configuration = config.Configuration()
    conection = dal.SqlLiteConection(configuration)
    parser = reqparse.RequestParser()
    table_aviao().add_args(parser)


    #obter registo
    def get(self,id):
        Aviao.conection.open_conection()
        aviao = table_aviao()
        aviao.get_by_pk_id(id,Aviao.conection)
        return aviao.get_json()

    #inserir registo
    def post(self):
        data = Aviao.parser.parse_args()
        aviao = table_aviao()
        aviao.read_from_args(data)
        Aviao.conection.open_conection()
        aviao.update(Aviao.conection)
        Aviao.conection.commit()
        return {'message': 'Record created successfully.'}, 201


    