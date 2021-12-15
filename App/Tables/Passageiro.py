from App.Tables import dal


class Passageiro(dal.Table):
    def __init__(self):
        super().__init__('Aeroporto', 
        {
            'ID_Passageiro':dal.Field(int,'ID_Aviao', pk =True),
            'Nome_Passageiro':dal.Field(str,'Nome_Passageiro'),
            'Morada_Passageiro':dal.Field(str,'Morada_Passageiro'),
            'Telefone_Passageiro':dal.Field(int,'Telefone_Passageiro'),
            'Email':dal.Field(str,'Email'),
            'Piloto':dal.Field(bool,'Piloto'),
            'Codigo_Postal':dal.Field(str,'Codigo_Postal'),

        }
        )

    def get_id_passageiro(self):
        return self.get_field_value('ID_Passageiro') 
    def set_id_passageiro(self,value):
        self.set_field_value('ID_Passageiro',value) 

    id_passageiro = property(get_id_passageiro,set_id_passageiro)


    def get_nome_passageiro(self):
        return self.get_field_value('Nome_Passageiro') 
    def set_nome_passageiro(self,value):
        self.set_field_value('Nome_Passageiro',value)

    nome_passageiro = property(get_nome_passageiro,set_nome_passageiro)


    def get_morada_passageiro(self):
        return self.get_field_value('Morada_Passageiro') 
    def set_morada_passageiro(self,value):
        self.set_field_value('Morada_Passageiro',value)

    morada_passageito = property(get_morada_passageiro,set_morada_passageiro)


    def get_telefone_passageiro(self):
        return self.get_field_value('Telefone_Passageiro') 
    def set_telefone_passageiro(self,value):
        self.set_field_value('Telefone_Passageiro',value)

    telefone_passageiro = property(get_telefone_passageiro,set_telefone_passageiro)


    def get_email(self):
        return self.get_field_value('Email') 
    def set_email(self,value):
        self.set_field_value('Email',value)

    email = property(get_email,set_email)


    def get_piloto(self):
        return self.get_field_value('Piloto') 
    def set_piloto(self,value):
        self.set_field_value('Piloto',value)

    piloto = property(get_piloto,set_piloto)


    def get_codigo_postal(self):
        return self.get_field_value('Codigo_Postal') 
    def set_codigo_postal(self,value):
        self.set_field_value('Codigo_Postal',value)

    codigo_postal = property(get_codigo_postal,set_codigo_postal)