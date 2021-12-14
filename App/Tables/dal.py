from os import W_OK
import sqlite3
from sqlite3.dbapi2 import apilevel
from typing import Dict

class SqlLiteConection():
    def __init__(self,config):
        self.conection_is_open = False
        self.database_name = config.get_database_name()

    def open_conection(self):
        if(not self.conection_is_open):
            self.conection = sqlite3.connect(self.database_name)        

    def close_conection(self):
        self.conection.close()

    def commit(self):
        self.conection.commit()

    def open_transaction(self):
        self.open_conection()
        self.conection.in_transaction

    def close_transaction(self):
        self.conection.commit()

    def roolback(self):
        self.conection.rollback()

    def execute_non_query(self,query):
        self.conection.executescript(query)



            
    def execute_query(self,query,params = None):
        if(params == None):
            cur = self.conection.execute(query)
        else:
            cur = self.conection.execute(query,params)
            
        return cur

    def execute_scalar(self,query,params = None):
        rows = self.execute_query(query,params)
        for row in rows:
            return row[0]


class Field:
    def __init__(self,type,column_name,help = '',pk = False):
        self.type = type
        self.column_name = column_name
        self.is_pk = pk
        self.help = help
        self.value = self.type()
        


    def get_value(self):
        return self._value
    
    def set_value(self,value):
        self._value = self.type(value)


    value = property(get_value,set_value)


class Table:
    def __init__(self,name,fields:Dict[str,Field]):
        self.fields = fields
        self.table_name = name        
        self.pk_field_key = ''

        for key in fields.keys():
            if(fields[key].is_pk):
                self.pk_field_key = key



    def get_field_value(self,name):
        return self.fields[name].value
    
    def set_field_value(self,name,value):
        self.fields[name].value = value

    def set_new_pk_id(self, conection:SqlLiteConection):
        column = self.fields[self.pk_field_key].column_name
        query = f'select IFNULL(max({column}),0) + 1 from {self.table_name}'
        var =  conection.execute_scalar(query)
        self.fields[self.pk_field_key].set_value(var)      


    def insert(self,conection:SqlLiteConection):
        self.set_new_pk_id(conection)
        insert_query = f'INSERT INTO [{self.table_name}] ('  
        values_query = 'VALUES('
        values = []

        for  field_key in self.fields.keys():
            insert_query += f'{field_key}, '
            values_query += '?, '
            values.append(self.fields[field_key].get_value())


        insert_query = insert_query[:-2] + ') ' 
        insert_query += values_query [:-2] + ')'

        conection.open_transaction()
        conection.execute_query(insert_query, tuple(values))
        conection.commit()

    @staticmethod
    def get_by_pk_id(id : int):
        return ''