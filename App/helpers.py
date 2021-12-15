import os
import datetime

def combine_with_base_path(path):
    base_path = os.getcwd()
    return os.path.join(base_path,path)

def parse_string_to_date(date_str):  

    try:
        ano = int(date_str[0:4])
        mes = int(date_str[5:7])
        dia = int(date_str[8:10])
        return datetime.datetime(ano,mes,dia)
    except:
        return datetime.date.min