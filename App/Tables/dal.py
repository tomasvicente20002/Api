import sqlite3
from sqlite3.dbapi2 import apilevel

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

    def execute_non_query(self,query,params = None):
        if(params == None):
            self.conection.executescript(query)
        else:
            self.conection.executescript(query,params)
            
    def execute_query(self,query,params = None):
        if(params == None):
            cur = self.conection.execute(query)
        else:
            cur = self.conection.execute(query,params)
            
        return cur


class Field:
    def __init__(self,type,column_name,help = '',pk = False):
        self.type = type
        self.column_name = column_name
        self.is_pk = pk
        self.help = help


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

    def get_new_pk_id():
        query = 'select max()'

    def insert(self,conection:SqlLiteConection):

        sel

        insert_query = f'INSERT INTO [{self.table_name}] ('  
        values_query = 'VALUES('

        for  fields in self.fields.keys():
            insert_query += f'{fields}, '
            values_query += '?, '


        insert_query = insert_query[:-2] + ') ' 
        insert_query += values_query [:-2] + ')'

        conection.open_transaction()
        conection.execute(insert_query, self.fields.values())
        conection.commit()

    @staticmethod
    def get_by_pk_id(id : int):
        return ''