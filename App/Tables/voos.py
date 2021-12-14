from App.Tables import dal

class Voos(dal.Table):
    def __init__(self):
        super().__init__('Voos', 
        {'pkvoos':dal.Field(int,'pkvoos',True)})

    @property
    def name(self):
        return self.fields['pkvoos'].value
    
    @name.setter
    def name(self, value):
        self.fields['pkvoos'].value = value