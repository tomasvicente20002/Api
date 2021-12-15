from App.Tables import dal

class Aeroporto(dal.Table):
    def __init__(self):
        super().__init__('Voos', 
        {
            'ID_Aeroporto':dal.Field(int,'ID_Aeroporto',True),
            'Nome_Aeroporto':dal.Field(str,'Nome_Aeroporto'),
            'ID_Local':dal.Field(str,'ID_Local'),
            'Local_Aeroporto':dal.Field(str,'Local_Aeroporto'),
        }
        )



    @property
    def name(self):
        return self.fields['pkvoos'].value
    
    @name.setter
    def name(self, value):
        self.fields['pkvoos'].value = value