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

    from App.Tables import dal

    def get_id_aviao(self):
        return self.get_field_value('ID_Aviao') 
    def set_id_aviao(self,value):
        self.set_field_value('ID_Aviao',value) 

    id_aviao = property(get_id_aviao,set_id_aviao)


    def get_nome_aviao(self):
        return self.get_field_value('Nome_Aviao') 
    def set_nome_aviao(self,value):
        self.set_field_value('Nome_Aviao',value)

    nome_aeroporto = property(get_nome_aviao,set_field_value)


    def get_tipo_aviao(self):
        return self.get_field_value('Tipo_Aviao') 
    def set_tipo_aviao(self,value):
        self.set_field_value('Tipo_Aviao',value) 

    id_aviao = property(get_tipo_aviao,set_tipo_aviao)
