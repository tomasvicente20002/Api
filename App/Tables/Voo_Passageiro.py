from App.Tables import dal


class Voo_Passageiro(dal.Table):
    def __init__(self):
        super().__init__('Voo_Passageiro', 
        {
            'ID_Voo_Passageiro':dal.Field(int,'ID_Voo_Passageiro', pk =True),
            'ID_Voo':dal.Field(int,'ID_Voo', pk = True),
            'ID_Passageiro':dal.Field(int,'ID_Passageiro', pk = True),
        }
        )

    def get_id_voo_passageiro(self):
        return self.get_field_value('ID_Voo_Passageiro') 
    def set_id_voo_passageiro(self,value):
        self.set_field_value('ID_Voo_Passageiro',value) 

    id_voo_passageiro = property(get_id_voo_passageiro,set_id_voo_passageiro)


    def get_id_voo(self):
        return self.get_field_value('ID_Voo') 
    def set_id_voo(self,value):
        self.set_field_value('ID_Voo',value) 

    id_voo = property(get_id_voo,set_id_voo)

    def get_id_passageiro(self):
        return self.get_field_value('ID_Passageiro') 
    def set_id_passageiro(self,value):
        self.set_field_value('ID_Passageiro',value) 

    id_passageiro = property(get_id_passageiro,set_id_passageiro)







