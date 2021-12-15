from App.Tables import dal


class Voo(dal.Table):
    def __init__(self):
        super().__init__('Voo', 
        {
            'ID_Aviao':dal.Field(int,'ID_Aviao'),
            'ID_Voo':dal.Field(int,'ID_Voo',pk = True),
            'Partida_Voo':dal.Field(int,'Partida_Voo'),
            'Chegada_Voo':dal.Field(int,'Chegada_Voo'),
        }
        )


    def get_id_aviao(self):
        return self.get_field_value('ID_Aviao') 
    def set_id_aviao(self,value):
        self.set_field_value('ID_Aviao',value)

    id_aviao = property(get_id_aviao,set_id_aviao)


    def get_id_voo(self):
        return self.get_field_value('ID_Voo') 
    def set_id_voo(self,value):
        self.set_field_value('ID_Voo',value)

    id_voo = property(get_id_voo,set_id_voo)


    def get_partida_voo(self):
        return self.get_field_value('Partida_Voo') 
    def set_partida_voo(self,value):
        self.set_field_value('Partida_Voo',value)

    partida_voo = property(get_partida_voo,set_partida_voo)


    def get_chegada_voo(self):
        return self.get_field_value('Chegada_Voo') 
    def set_chegada_voo(self,value):
        self.set_field_value('Chegada_Voo',value)

    chegada_voo = property(get_chegada_voo,set_chegada_voo)
