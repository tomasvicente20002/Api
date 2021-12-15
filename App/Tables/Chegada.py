from App.Tables import dal
from App.helpers import parse_string_to_date
import datetime

class Chegada(dal.Table):
    def __init__(self):
        super().__init__('Chegada', 
        {
            'ID_Chegada':dal.Field(int,'ID_Chegada',pk = True),
            'Data_Hora_Chegada':dal.Field(datetime,'Data_Hora_Chegada'),
            'ID_Aeroporto':dal.Field(int,'ID_Aeroporto'),
        }
        )

    def get_id_chegada(self):
        return self.get_field_value('ID_Chegada') 
    def set_id_cheagda(self,value):
        self.set_field_value('ID_Chegada',value) 

    id_chegada = property(get_id_chegada,set_id_cheagda)




    def get_Data_Hora(self):
        return self.get_field_value('Data_Hora_Chegada') 
    def set_nome_aviao(self,value):
        if(type(value) == str):
            self.set_field_value('Data_Hora_Chegada',parse_string_to_date(value))
        else:
            self.set_field_value('Data_Hora_Chegada',value) 

    data_hora = property(get_Data_Hora,set_nome_aviao)


    def get_id_aeroporto(self):
        return self.get_field_value('ID_Aeroporto') 
    def set_id_aeroporto(self,value):
        self.set_field_value('ID_Aeroporto',value) 

    id_aeroporto = property(set_id_aeroporto,get_id_aeroporto)
