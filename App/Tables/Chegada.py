from App.Tables import dal
import datetime

class Chegada(dal.Table):
    def __init__(self):
        super().__init__('Cheagda', 
        {
            'ID_Chegada':dal.Field(int,'ID_Chegada',pk = True),
            'Data_Hora_Chegada':dal.Field(datetime,'Data_Hora_Chegada'),
            'ID_Aeroporto':dal.Field(int,'ID_Aeroporto',pk = True),
        }
        )