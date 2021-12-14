from App.Tables import dal


class Aeroporto(dal.Table):
    def __init__(self):
        super().__init__('Aeroporto', 
        {
            'ID_Aviao':dal.Field(int,'ID_Aviao', pk =True),
            'Nome_Aviao':dal.Field(str,'Nome_Aviao'),
            'Tipo_Aviao':dal.Field(int,'Tipo_Aviao'),
        }
        )

