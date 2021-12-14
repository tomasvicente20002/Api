from App.Tables import dal


class Aeroporto(dal.Table):
    def __init__(self):
        super().__init__('Aeroporto', 
        {
            'ID_Passageiro':dal.Field(int,'ID_Aviao', pk =True),
            'Nome_Passageiro':dal.Field(str,'Nome_Aviao'),
            'Morada_Passageiro':dal.Field(int,'Tipo_Aviao'),
        }
        )

