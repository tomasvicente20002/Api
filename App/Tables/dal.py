import sqlite3
from sqlite3.dbapi2 import apilevel

class SqlLiteConection():
    def __init__(self,config):
        print(config.get_database_name())

class Field:
    def __init__(self,type,column_name,pk = False):
        self.type = type
        self.column_name = column_name
        self.is_pk = pk        

    def get_value(self):
        return self._value
    
    def set_value(self,value):
        self._value = self.type(value)


    value = property(get_value,set_value)


class Table:
    def __init__(self,name,fields):
        self.fields = fields
        self.table_name = name

    def get_field_value(self,name):
        return self.fields[name].value
    
    def set_field_value(self,name,value):
        self.field[name].value = value

    def insert(self,conection):
        insert_query = f'INSERT INTO [{self.table_name}]'