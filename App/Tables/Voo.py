from App.Tables import dal


class Voo(dal.Table):
    def __init__(self):
        super().__init__('Voo', 
        {
            'ID_Aviao':dal.Field(int,'ID_Aviao',pk = True),
            'ID_Voo':dal.Field(int,'ID_Voo',pk = True),
            'Partida_Voo':dal.Field(int,'Partida_Voo'),
            'Chegada_Voo':dal.Field(int,'Chegada_Voo'),
        }
        )