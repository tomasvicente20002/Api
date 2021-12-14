from App.Tables import dal


class Aeroporto(dal.Table):
    def __init__(self):
        super().__init__('Aeroporto', 
        {
            'ID_Aeroporto':dal.Field(int,'ID_Aeroporto', pk =True),
            'Nome_Aeroporto':dal.Field(str,'Nome_Aeroporto'),
            'ID_Local':dal.Field(str,'ID_Local'),
            'Local_Aeroporto':dal.Field(str,'Local_Aeroporto'),
        }
        )
<<<<<<< Updated upstream

    def get_id_aeroporto(self):
        return self.get_field_value('ID_Aeroporto') 
    def set_id_aeroporto(self,value):
        self.set_field_value('ID_Aeroporto',value) 

    id_aeroporto = property(get_id_aeroporto,set_id_aeroporto)


    def get_nome_aeroporto(self):
        return self.get_field_value('Nome_Aeroporto') 
    def set_nome_aeroporto(self,value):
        self.set_field_value('Nome_Aeroporto',value)

    nome_aeroporto = property(get_nome_aeroporto,set_nome_aeroporto)


    def get_id_local(self):
        return self.get_field_value('ID_Local') 
    def set_id_local(self,value):
        self.set_field_value('ID_Local',value)

    nome_aeroporto = property(get_id_local,set_id_local)

    def get_local_aeroporto(self):
        return self.get_field_value('Local_Aeroporto') 
    def set_local_aeroporto(self,value):
        self.set_field_value('Local_Aeroporto',value)

    nome_aeroporto = property(get_local_aeroporto,set_local_aeroporto)
=======
>>>>>>> Stashed changes
