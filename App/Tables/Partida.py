from App.Tables import dal
import datetime

class Partida(dal.Table):
    def __init__(self):
        super().__init__('Partida', 
        {
            'ID_Partida':dal.Field(int,'ID_Partida', pk =True),
            'Data_Hora_Partida':dal.Field(datetime,'Data_Hora_Partida'),
            'ID_Aeroporto':dal.Field(int,'ID_Aeroporto', pk = True),
            'Local_Aeroporto':dal.Field(str,'Local_Aeroporto'),
        }
        )

    def get_id_partida(self):
        return self.get_field_value('ID_Partida') 
    def set_id_partida(self,value):
        self.set_field_value('ID_Partida',value) 

    id_partida = property(get_id_partida,set_id_partida)

    def get_data_hora(self):
        return self.get_field_value('Data_Hora_Partida') 
    def set_data_hora(self,value):
        self.set_field_value('Data_Hora_Partida',value) 

    data_hora = property(get_data_hora,set_data_hora)

    def get_id_aeroporto(self):
        return self.get_field_value('ID_Aeroporto') 
    def set_id_aeroporto(self,value):
        self.set_field_value('ID_Aeroporto',value) 

    id_aeroporto = property(get_id_aeroporto,set_id_aeroporto)

    def get_local_aeroporto(self):
        return self.get_field_value('Local_Aeroporto') 
    def set_local_aeroporto(self,value):
        self.set_field_value('Local_Aeroporto',value) 

    id_aeroporto = property(get_local_aeroporto,set_local_aeroporto)