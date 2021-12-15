from os import W_OK
import sqlite3
from sqlite3.dbapi2 import apilevel
from typing import Dict
import json
from flask_restful import reqparse

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
            
        return cur.fetchall()

    def execute_scalar(self,query,params = None):
        rows = self.execute_query(query,params)
        return rows[0][0]


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

        conection.execute_query(insert_query, tuple(values))



    def get_by_pk_id(self,id :int,conection:SqlLiteConection):     
        select_query = f'SELECT '
        values_pos = {}
        cnt = 0
        for field_key in self.fields.keys():
            select_query += f'{self.table_name}.{field_key}, '
            values_pos[cnt] = field_key
            cnt+=1

        cnt-=1
        select_query = select_query[:-2]
        select_query += f' FROM {self.table_name}'
        select_query += f' WHERE {self.table_name}.{self.fields[self.pk_field_key].column_name} = ?'


        rows = conection.execute_query(select_query,(id,))
        
        while cnt >= 0:
            key = values_pos[cnt]
            self.fields[key].set_value(rows[0][cnt])
            cnt-=1
    
    def update(self,conection:SqlLiteConection):
        update_query = f'UPDATE {self.table_name} SET '
        values = []

        for key in self.fields.keys():
            if(key == self.pk_field_key):
                continue

            update_query += f'{key} = ?, '
            values.append(self.fields[key].get_value())

        values.append(self.fields[self.pk_field_key].get_value())
        update_query = update_query[:-2]
        update_query += f'WHERE {self.table_name}.{self.pk_field_key} = ?'

        conection.execute_query(update_query,tuple(values))


    
    def get_json(self):
        dic_values = {}

        for key in self.fields.keys():
            dic_values[key] = self.fields[key].get_value()
        return json.dumps(dic_values)

    def get_json_without_pk(self):
        dic_values = {}

        for key in self.fields.keys():
            if(key == self.pk_field_key):
                continue

            dic_values[key] = self.fields[key].get_value()
            
        return json.dumps(dic_values)

    def add_args(self,reqparse:reqparse.RequestParser):
        for key in self.fields.keys():
            reqparse.add_argument(key,type =self.fields[key].type)


    def read_from_args(self,args):
        for key in args.keys():
            self.set_field_value(key,args[key])